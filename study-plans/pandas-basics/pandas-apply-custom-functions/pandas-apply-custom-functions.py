import pandas as pd

def apply_transform(data, column, operation):
    """
    Returns: dict with original columns plus column_transformed
    """
    pass
    df = pd.DataFrame(data)
    new_col = column + "_transformed"
    if operation == "normalize":
        df[new_col] = (df[column] - df[column].min()) / (df[column].max() - df[column].min())
        df[new_col] = df[new_col].round(4)

    elif operation == "rank":
        df[new_col] = df[column].rank().astype(int)

    elif operation == "cumsum":
        df[new_col] = df[column].cumsum()

    elif operation == "double":
        df[new_col] = df[column]*2

    return df.to_dict(orient="list")