import pandas as pd

def handle_missing(data, fill_value):
    """
    Returns: dict with 'null_counts' (dict) and 'cleaned_data' (dict)
    """
    pass
    df = pd.DataFrame(data)
    null_counts_dict = df.isnull().sum().to_dict()
    df = df.fillna(fill_value)

    result = {
        "null_counts": null_counts_dict,
        "cleaned_data": df.to_dict(orient="list")
    }

    return result