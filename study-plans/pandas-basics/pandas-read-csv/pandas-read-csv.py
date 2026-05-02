import pandas as pd

def create_dataframe(data):
    """
    Returns: dict with 'data', 'shape', 'columns'
    """

    df = pd.DataFrame(data)
    shape = df.shape

    df_info_dict = {
        "data": df.to_dict(orient='list'),
        "shape": list(df.shape),
        "columns":  df.columns.tolist()
    }


    return df_info_dict