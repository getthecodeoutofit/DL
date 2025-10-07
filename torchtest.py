import torch

# Check if CUDA is available
print("CUDA available:", torch.cuda.is_available())

# If available, print the current device
if torch.cuda.is_available():
    print("Current device:", torch.cuda.current_device())
    print("Device name:", torch.cuda.get_device_name(torch.cuda.current_device()))
else:
    print("Running on CPU")
