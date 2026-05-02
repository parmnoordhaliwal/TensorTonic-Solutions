import pandas as pd

def change_dtype(data, column, target_type):
    """
    Returns: list [dtypes_before, dtypes_after] (both dicts)
    """
    pass
    df = pd.DataFrame(data)
    dtypes_before = df.dtypes.astype(str).to_dict()
    df[column] = df[column].astype(target_type)
    dtypes_after = df.dtypes.astype(str).to_dict()
    result = [dtypes_before, dtypes_after]
    
    return result