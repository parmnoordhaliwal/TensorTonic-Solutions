import pandas as pd

def select_columns(data, columns):
    """
    Returns: dict mapping selected column names to value lists
    """
    pass
    df = pd.DataFrame(data)
    new_df = df[columns]

    return new_df.to_dict(orient='list')