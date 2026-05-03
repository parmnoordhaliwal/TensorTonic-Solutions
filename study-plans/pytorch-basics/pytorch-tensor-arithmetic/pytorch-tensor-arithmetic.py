import torch

def tensor_op(x, y, op):
    """
    Returns: list (result tensor converted via .tolist())
    """
    pass
    x = torch.tensor(x, dtype=torch.float32)
    y = torch.tensor(y, dtype=torch.float32)
    
    if op == "add":
        res = torch.add(x, y)
    elif op == "multiply":
        res = torch.mul(x, y)
    elif op == "matmul":
        res = torch.matmul(x, y)
    elif op == "power":
        res = x ** y
    elif op == "max":
        res = torch.maximum(x, y)
    else:
        res = torch.tensor([])
    return res.tolist()
        