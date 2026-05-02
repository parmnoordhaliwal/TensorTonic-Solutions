import pandas as pd

def melt_dataframe(data, id_vars, value_vars):
    """
    Returns: dict with keys from id_vars plus 'variable' and 'value'
    """
    pass
    df = pd.DataFrame(data)
    df = df.melt(id_vars=id_vars, value_vars=value_vars)
    return df.to_dict(orient="list")