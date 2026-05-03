import torch

def reshape_tensor(x, op):
    """
    Returns: list
    """
    pass
    x = torch.tensor(x, dtype=torch.float32)
    if op == "flatten":
        res = torch.flatten(x)
    elif op == "squeeze":
        res = torch.squeeze(x)
    elif op == "transpose":
        res = x.t()
    return res.tolist()
        
