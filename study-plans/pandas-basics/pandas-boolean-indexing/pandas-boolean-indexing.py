import pandas as pd

def boolean_filter(data, column, threshold):
    """
    Returns: dict with 'filtered_data' (dict) and 'count' (int)
    """
    pass
    df = pd.DataFrame(data)
    filtered_df = df[df[column] > threshold]

    result = {
        "filtered_data": filtered_df.to_dict(orient='list'),
        "count": filtered_df.shape[0]
    }

    return result