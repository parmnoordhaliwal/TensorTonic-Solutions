import pandas as pd

def head_tail(data, n):
    """
    Returns: dict with 'head' and 'tail' (both dicts of column -> list)
    """
    pass

    df = pd.DataFrame(data)

    result = {
        "head": df.head(n).to_dict(orient="list"),
        "tail": df.tail(n).to_dict(orient="list")
    }
    
    return result