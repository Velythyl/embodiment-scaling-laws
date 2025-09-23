import torch


class RandomCommands:
    """
    Generates random velocity commands
    It returns one command regardless of number of parallelized envs
    """
    def __init__(self, env, x_vel_range, y_vel_range, yaw_vel_range, resampling_interval):
        self.env = env
        self.min_x_velocity = x_vel_range[0]
        self.max_x_velocity = x_vel_range[1]
        self.min_y_velocity = y_vel_range[0]
        self.max_y_velocity = y_vel_range[1]
        self.min_yaw_velocity = yaw_vel_range[0]
        self.max_yaw_velocity = yaw_vel_range[1]
        self.resampling_count = 0
        self.resampling_interval = resampling_interval

    def get_next_command(self):
        """
        Sample velocity command at the beginning of every new interval,
        otherwise just return the previous command
        :return:  velocity command
        """

        self.resampling_count = (self.resampling_count + 1) % self.resampling_interval
        if self.resampling_count == 1:
            self.goal_x_velocity = torch.rand(self.env.num_envs, 1).uniform_(self.min_x_velocity, self.max_x_velocity).to(self.env.device)
            self.goal_y_velocity = torch.rand(self.env.num_envs, 1).uniform_(self.min_y_velocity, self.max_y_velocity).to(self.env.device)
            self.goal_yaw_velocity = torch.rand(self.env.num_envs, 1).uniform_(self.min_yaw_velocity, self.max_yaw_velocity).to(self.env.device)
        else:
            pass

        return self.goal_x_velocity, self.goal_y_velocity, self.goal_yaw_velocity
