import torch

def activate(x, method="relu"):
    """
    Returns: list (activated tensor converted via .tolist())
    """
    pass
    x = torch.tensor(x, dtype = torch.float32)
    if method == "relu":
        res = torch.clamp(x, min=0)
        return res.tolist()
    elif method == "sigmoid":
        res = 1 / (1 + torch.exp(-x))
        return res.tolist()
    elif method == "tanh":
        res = (torch.exp(x) - torch.exp(-x))/(torch.exp(x) + torch.exp(-x))
        return res.tolist()
    elif method == "leaky_relu":
        res = torch.where(x > 0, x, 0.01 * x)
        return res.tolist()