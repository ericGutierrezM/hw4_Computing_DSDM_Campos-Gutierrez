import pandas as pd

def load_data(csv_file):
    data = pd.read_csv(csv_file)
    return data