import torch

def create_tensor(method, shape, value=0.0):
    """
    Returns: list
    """
    pass
    if method == "zeros":
        res = torch.zeros(shape)
    elif method == "ones":
        res = torch.ones(shape)
    elif method == "full":
        res = torch.full(shape, value)
    else:
        res = torch.tensor([])

    return res.tolist()

    