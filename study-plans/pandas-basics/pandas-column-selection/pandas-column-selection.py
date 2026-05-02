import pandas as pd

def select_column(data, column):
    """
    Returns: dict with 'values' (list) and 'length' (int)
    """
    pass
    df = pd.DataFrame(data)
    values = df[column].values.tolist()
    length = len(values)

    result = {
        "values": values,
        "length": length
    }
    return result