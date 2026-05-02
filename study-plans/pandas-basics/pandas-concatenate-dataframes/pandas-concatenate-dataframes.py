import pandas as pd

def concat_dataframes(dfs):
    """
    Returns: list [shape, data] where shape is [rows, cols]
    """
    pass
    df_list = [pd.DataFrame(d) for d in dfs]
    df = pd.concat(df_list, ignore_index=True)
    result = [df.shape, df.to_dict(orient="list")]
    return result