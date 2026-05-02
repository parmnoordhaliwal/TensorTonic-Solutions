import pandas as pd

def multi_groupby(data, group_cols, value_col, aggfunc):
    """
    Returns: dict of lists (flat table with group columns + value column)
    """
    pass
    df = pd.DataFrame(data)
    result = df.groupby(group_cols, as_index=False)[value_col].agg(aggfunc)
    return result.to_dict(orient="list")