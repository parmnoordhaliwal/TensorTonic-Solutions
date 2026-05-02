import pandas as pd

def reset_index_demo(data, index_col):
    """
    Returns: list [columns_before_reset, columns_after_reset]
    """
    pass

    df = pd.DataFrame(data)

    df = df.set_index(index_col)
    columns_before_reset = df.columns.tolist()

    df = df.reset_index()
    columns_after_reset = df.columns.tolist()

    result = [columns_before_reset, columns_after_reset]

    return result