import pandas as pd

def generate_dummies(data, columns_list):
    return pd.get_dummies(data, columns=columns_list, dtype=int)