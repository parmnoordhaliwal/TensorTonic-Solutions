import pandas as pd

def merge_dataframes(left, right, on, how):
    """
    Returns: dict of column to value lists
    """
    pass
    left_df = pd.DataFrame(left)
    right_df = pd.DataFrame(right)
    merged_df = pd.merge(left_df, right_df, on=on, how=how)

    return merged_df.to_dict(orient="list")