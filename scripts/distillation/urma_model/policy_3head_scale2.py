import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import os
import json
# import ipdb

class Policy(nn.Module):
    def __init__(self, initial_softmax_temperature,
                 softmax_temperature_min, stability_epsilon, policy_mean_abs_clip, policy_std_min_clip,
                 policy_std_max_clip, args_cli=None):
        super(Policy, self).__init__()
        self.softmax_temperature_min = softmax_temperature_min
        self.stability_epsilon = stability_epsilon
        self.policy_mean_abs_clip = policy_mean_abs_clip
        self.policy_std_min_clip = policy_std_min_clip
        self.policy_std_max_clip = policy_std_max_clip
        self.args_cli = args_cli

        # Constants
        dynamic_joint_des_dim = 18
        general_state_dim = 16 + 4
        dynamic_joint_state_dim = 3

        # hyper param
        scale_factor = 2

        dynamic_joint_state_mask_dim = 64 * scale_factor # For scaling_factor_0.5_v3_modelscale3_attempt2
        # dynamic_joint_state_mask_dim = 64 # For scaling_factor_0.1_v3
        dynamic_joint_state_feat = 4 * scale_factor
        nr_heads = 3
        
        # Head 1
        self.dynamic_joint_state_mask11 = nn.Linear(dynamic_joint_des_dim, dynamic_joint_state_mask_dim)
        self.dynamic_joint_layer_norm1 = nn.LayerNorm(dynamic_joint_state_mask_dim, eps=1e-6)
        self.dynamic_joint_state_mask12 = nn.Linear(dynamic_joint_state_mask_dim, dynamic_joint_state_mask_dim)
        self.joint_log_softmax_temperature1 = nn.Parameter(torch.tensor([initial_softmax_temperature - self.softmax_temperature_min]).log())
        self.latent_dynamic_joint_state1 = nn.Linear(dynamic_joint_state_dim, dynamic_joint_state_feat)
        # Head 2
        self.dynamic_joint_state_mask21 = nn.Linear(dynamic_joint_des_dim, dynamic_joint_state_mask_dim)
        self.dynamic_joint_layer_norm2 = nn.LayerNorm(dynamic_joint_state_mask_dim, eps=1e-6)
        self.dynamic_joint_state_mask22 = nn.Linear(dynamic_joint_state_mask_dim, dynamic_joint_state_mask_dim)
        self.joint_log_softmax_temperature2 = nn.Parameter(torch.tensor([initial_softmax_temperature - self.softmax_temperature_min]).log())
        self.latent_dynamic_joint_state2 = nn.Linear(dynamic_joint_state_dim, dynamic_joint_state_feat)
        # Head 3
        self.dynamic_joint_state_mask31 = nn.Linear(dynamic_joint_des_dim, dynamic_joint_state_mask_dim)
        self.dynamic_joint_layer_norm3 = nn.LayerNorm(dynamic_joint_state_mask_dim, eps=1e-6)
        self.dynamic_joint_state_mask32 = nn.Linear(dynamic_joint_state_mask_dim, dynamic_joint_state_mask_dim)
        self.joint_log_softmax_temperature3 = nn.Parameter(torch.tensor([initial_softmax_temperature - self.softmax_temperature_min]).log())
        self.latent_dynamic_joint_state3 = nn.Linear(dynamic_joint_state_dim, dynamic_joint_state_feat)

        # general state
        general_state_latent_dim = 128
        self.general_state_encoder = nn.Sequential(
            nn.Linear(general_state_dim, general_state_latent_dim),
            nn.LayerNorm(general_state_latent_dim, eps=1e-6),
        )

        combined_action_feat_dim = dynamic_joint_state_mask_dim * dynamic_joint_state_feat * nr_heads + general_state_latent_dim
        action_latent_dims = [512, 256, 128 * scale_factor]
        self.action_latent1 = nn.Linear(combined_action_feat_dim, action_latent_dims[0])
        self.action_layer_norm = nn.LayerNorm(action_latent_dims[0], eps=1e-6)
        self.action_latent2 = nn.Linear(action_latent_dims[0], action_latent_dims[1])
        self.action_latent3 = nn.Linear(action_latent_dims[1], action_latent_dims[2])

        action_des_latent_dim = 128 * scale_factor
        self.action_description_latent1 = nn.Linear(dynamic_joint_des_dim, action_des_latent_dim)
        self.action_description_layer_norm = nn.LayerNorm(action_des_latent_dim, eps=1e-6)
        self.action_description_latent2 = nn.Linear(action_des_latent_dim, action_des_latent_dim)

        policy_in_dim = (dynamic_joint_state_feat * nr_heads) + action_latent_dims[-1] + action_des_latent_dim
        policy_hidden_dim = 128 * scale_factor
        self.policy_mean_layer1 = nn.Linear(policy_in_dim, policy_hidden_dim)
        self.policy_mean_layer_norm = nn.LayerNorm(policy_hidden_dim, eps=1e-6)
        self.policy_mean_layer2 = nn.Linear(policy_hidden_dim, 1)
        self.policy_logstd_layer = nn.Linear(policy_hidden_dim, 1)

    def forward(self, dynamic_joint_description, dynamic_joint_state, general_state):
        # Head 1
        dynamic_joint_state_mask1 = self.dynamic_joint_state_mask11(dynamic_joint_description)
        dynamic_joint_state_mask1 = F.elu(self.dynamic_joint_layer_norm1(dynamic_joint_state_mask1))
        dynamic_joint_state_mask1 = torch.tanh(self.dynamic_joint_state_mask12(dynamic_joint_state_mask1))
        if self.args_cli is not None:
            if self.args_cli.description_log_file is not None:
                dynamic_joint_state_mask1_node = dynamic_joint_state_mask1.clone()
        dynamic_joint_state_mask1 = torch.clamp(dynamic_joint_state_mask1,
                                               -1.0 + self.stability_epsilon, 1.0 - self.stability_epsilon)
        latent_dynamic_joint_state1 = F.elu(self.latent_dynamic_joint_state1(dynamic_joint_state))
        joint_e_x1 = torch.exp(dynamic_joint_state_mask1 / (torch.exp(self.joint_log_softmax_temperature1) + self.softmax_temperature_min))
        dynamic_joint_state_mask1 = joint_e_x1 / (joint_e_x1.sum(dim=-1, keepdim=True) + self.stability_epsilon)
        if self.args_cli is not None:
            if self.args_cli.description_log_file is not None:
                dynamic_joint_state_mask2_node = dynamic_joint_state_mask1.clone()
        dynamic_joint_state_mask1 = dynamic_joint_state_mask1.unsqueeze(-1).repeat(1, 1, 1, latent_dynamic_joint_state1.size(-1))
        if self.args_cli is not None:
            if self.args_cli.description_log_file is not None:
                dynamic_joint_state_mask3_node = dynamic_joint_state_mask1.clone()
        masked_dynamic_joint_state1 = dynamic_joint_state_mask1 * latent_dynamic_joint_state1.unsqueeze(-2)
        masked_dynamic_joint_state1 = masked_dynamic_joint_state1.view(masked_dynamic_joint_state1.shape[:-2] + (masked_dynamic_joint_state1.shape[-2] * masked_dynamic_joint_state1.shape[-1],))
        dynamic_joint_latent1 = masked_dynamic_joint_state1.sum(dim=-2)

        # Head 2
        dynamic_joint_state_mask2 = self.dynamic_joint_state_mask21(dynamic_joint_description)
        dynamic_joint_state_mask2 = F.elu(self.dynamic_joint_layer_norm2(dynamic_joint_state_mask2))
        dynamic_joint_state_mask2 = torch.tanh(self.dynamic_joint_state_mask22(dynamic_joint_state_mask2))
        dynamic_joint_state_mask2 = torch.clamp(dynamic_joint_state_mask2,
                                               -1.0 + self.stability_epsilon, 1.0 - self.stability_epsilon)
        latent_dynamic_joint_state2 = F.elu(self.latent_dynamic_joint_state2(dynamic_joint_state))
        joint_e_x2 = torch.exp(dynamic_joint_state_mask2 / (torch.exp(self.joint_log_softmax_temperature2) + self.softmax_temperature_min))
        dynamic_joint_state_mask2 = joint_e_x2 / (joint_e_x2.sum(dim=-1, keepdim=True) + self.stability_epsilon)
        dynamic_joint_state_mask2 = dynamic_joint_state_mask2.unsqueeze(-1).repeat(1, 1, 1, latent_dynamic_joint_state2.size(-1))
        masked_dynamic_joint_state2 = dynamic_joint_state_mask2 * latent_dynamic_joint_state2.unsqueeze(-2)
        masked_dynamic_joint_state2 = masked_dynamic_joint_state2.view(masked_dynamic_joint_state2.shape[:-2] + (masked_dynamic_joint_state2.shape[-2] * masked_dynamic_joint_state2.shape[-1],))
        dynamic_joint_latent2 = masked_dynamic_joint_state2.sum(dim=-2)

        # Head 3
        dynamic_joint_state_mask3 = self.dynamic_joint_state_mask31(dynamic_joint_description)
        dynamic_joint_state_mask3 = F.elu(self.dynamic_joint_layer_norm3(dynamic_joint_state_mask3))
        dynamic_joint_state_mask3 = torch.tanh(self.dynamic_joint_state_mask32(dynamic_joint_state_mask3))
        dynamic_joint_state_mask3 = torch.clamp(dynamic_joint_state_mask3,
                                                  -1.0 + self.stability_epsilon, 1.0 - self.stability_epsilon)
        latent_dynamic_joint_state3 = F.elu(self.latent_dynamic_joint_state3(dynamic_joint_state))
        joint_e_x3 = torch.exp(dynamic_joint_state_mask3 / (torch.exp(self.joint_log_softmax_temperature3) + self.softmax_temperature_min))
        dynamic_joint_state_mask3 = joint_e_x3 / (joint_e_x3.sum(dim=-1, keepdim=True) + self.stability_epsilon)
        dynamic_joint_state_mask3 = dynamic_joint_state_mask3.unsqueeze(-1).repeat(1, 1, 1, latent_dynamic_joint_state3.size(-1))
        masked_dynamic_joint_state3 = dynamic_joint_state_mask3 * latent_dynamic_joint_state3.unsqueeze(-2)
        masked_dynamic_joint_state3 = masked_dynamic_joint_state3.view(masked_dynamic_joint_state3.shape[:-2] + (masked_dynamic_joint_state3.shape[-2] * masked_dynamic_joint_state3.shape[-1],))
        dynamic_joint_latent3 = masked_dynamic_joint_state3.sum(dim=-2)

        general_state_latent = self.general_state_encoder(general_state)
        combined_input = torch.cat([dynamic_joint_latent1, dynamic_joint_latent2, dynamic_joint_latent3, general_state_latent], dim=-1)

        action_latent = self.action_latent1(combined_input)
        action_latent = F.elu(self.action_layer_norm(action_latent))
        action_latent = F.elu(self.action_latent2(action_latent))
        action_latent = self.action_latent3(action_latent)

        action_description_latent = self.action_description_latent1(dynamic_joint_description)
        action_description_latent = F.elu(self.action_description_layer_norm(action_description_latent))
        action_description_latent = self.action_description_latent2(action_description_latent)

        action_latent = action_latent.unsqueeze(-2).repeat(1, action_description_latent.size(-2), 1)
        combined_action_latent = torch.cat([action_latent, latent_dynamic_joint_state1.detach(), latent_dynamic_joint_state2.detach(), latent_dynamic_joint_state3.detach(), action_description_latent], dim=-1)

        policy_mean = self.policy_mean_layer1(combined_action_latent)
        policy_mean = F.elu(self.policy_mean_layer_norm(policy_mean))
        policy_mean = self.policy_mean_layer2(policy_mean)
        policy_mean = torch.clamp(policy_mean, -self.policy_mean_abs_clip, self.policy_mean_abs_clip)

        if self.args_cli is not None:
            if self.args_cli.description_log_file is not None:

                # 1. Ensure the file exists and is a valid JSON file
                if not os.path.exists(self.args_cli.description_log_file):
                    with open(self.args_cli.description_log_file, 'w') as f:
                        json.dump({}, f)  # create an empty JSON object

                with open(self.args_cli.description_log_file, 'r') as f:
                    log_data = json.load(f)  # load existing content

                # 2. Build the info you want to store
                #    For example, just storing shapes (as lists) plus first slice of dynamic_joint_description
                log_data[self.args_cli.task] = {
                    "dynamic_joint_description": dynamic_joint_description.mean(dim=0).tolist(),
                    "dynamic_joint_state_mask1_node": dynamic_joint_state_mask1_node.mean(dim=0).tolist(),
                    "latent_dynamic_joint_state": latent_dynamic_joint_state1.mean(dim=0).tolist(),
                    "dynamic_joint_state_mask2_node": dynamic_joint_state_mask2_node.mean(dim=0).tolist(),
                    "dynamic_joint_state_mask3_node": dynamic_joint_state_mask3_node.mean(dim=0).tolist(),
                    "dynamic_joint_latent": dynamic_joint_latent1.mean(dim=0).tolist(),
                    "action_description_latent": action_description_latent.mean(dim=0).tolist(),
                    "action_latent": action_latent.mean(dim=0).tolist(),
                    "combined_action_latent": combined_action_latent.mean(dim=0).tolist(),
                    "policy_mean": policy_mean.mean(dim=0).squeeze(-1).tolist()
                }

                # 3. Write the updated log_data back to the file
                with open(self.args_cli.description_log_file, 'w') as f:
                    print(f"[INFO] Log description of {self.args_cli.task} to {self.args_cli.description_log_file}")
                    json.dump(log_data, f, indent=2)
        return policy_mean.squeeze(-1)


def get_policy(model_device: str, args_cli=None):
    initial_softmax_temperature = 1.0
    softmax_temperature_min = 0.015
    stability_epsilon = 0.00000001
    policy_mean_abs_clip = 10.0  # 10.0. This value should be adjusted based on data? Or the data should be normalized.
    policy_std_min_clip = 0.00000001
    policy_std_max_clip = 2.0

    policy = Policy(initial_softmax_temperature, softmax_temperature_min, stability_epsilon, policy_mean_abs_clip, policy_std_min_clip, policy_std_max_clip, args_cli)
    policy.to(model_device)

    return policy


if __name__ == "__main__":
    # define the device = 'cuda:0'
    model_device = 'cuda:0'

    policy = get_policy(model_device)

    dummy_dynamic_joint_description = torch.zeros((1, 13, 18), device=model_device, dtype=torch.float32)
    dummy_dynamic_joint_state = torch.zeros((1, 13, 3), device=model_device, dtype=torch.float32)
    dummy_dynamic_foot_description = torch.zeros((1, 4, 10), device=model_device, dtype=torch.float32)
    dummy_dynamic_foot_state = torch.zeros((1, 4, 2), device=model_device, dtype=torch.float32)
    dummy_general_policy_state = torch.zeros((1, 20), device=model_device, dtype=torch.float32)

    import time

    nr_evals = 1
    start = time.time()
    for i in range(nr_evals):
        with torch.no_grad():
            action = policy(dummy_dynamic_joint_description, dummy_dynamic_joint_state, dummy_general_policy_state)
    end = time.time()
    print("Average time per evaluation: ", (end - start) / nr_evals)
