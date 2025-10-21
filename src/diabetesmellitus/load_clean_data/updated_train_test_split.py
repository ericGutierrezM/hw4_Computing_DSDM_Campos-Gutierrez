import pandas as pd
from sklearn.model_selection import train_test_split

def updated_train_test_split(data, y_column_name):
    X = data.drop(y_column_name, axis=1)
    y = data[y_column_name]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=23, stratify=y
    )
    return X_train, X_test, y_train, y_test