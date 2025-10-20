import pandas as pd

def binary_encoding_gender(data):
    data['gender'] = data["gender"].map({"M": 1, "F": 0})
    return data