import pandas as pd

def fill_nan_mean(data, columns_list):
    data[columns_list] = data[columns_list].fillna(data[columns_list].mean())
    return data