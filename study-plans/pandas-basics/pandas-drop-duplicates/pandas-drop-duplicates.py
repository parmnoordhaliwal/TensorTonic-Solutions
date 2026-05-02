import pandas as pd

def drop_duplicates(data):
    """
    Returns: list [rows_before, rows_after, cleaned_data]
    """
    pass

    df = pd.DataFrame(data)
    rows_before = df.shape[0]
    df = df.drop_duplicates()
    rows_after = df.shape[0]

    result = [rows_before, rows_after, df.to_dict(orient="list")]

    return result