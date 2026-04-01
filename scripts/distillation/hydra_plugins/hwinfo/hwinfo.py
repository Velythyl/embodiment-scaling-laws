from omegaconf import OmegaConf

def gpu():
    import torch

    if torch.cuda.is_available():
        print(f"CUDA device count: {torch.cuda.device_count()}")
        devices = [torch.cuda.get_device_name(i) for i in range(torch.cuda.device_count())]
    else:
        devices = ["No GPU available"]

    return ", ".join(devices)

hwinfo_dict = {
    "gpu": gpu()
}


OmegaConf.register_new_resolver(
    "hwinfo", lambda key: hwinfo_dict[key]
)
