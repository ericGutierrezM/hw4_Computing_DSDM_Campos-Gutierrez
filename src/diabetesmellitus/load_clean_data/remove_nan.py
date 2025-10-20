import pandas as pd

def remove_nan(x_data, y_data, columns_list):
   mask = x_data[columns_list].notna().all(axis=1)
   new_X = x_data[mask].copy()
   new_y = y_data[mask].copy()

   return new_X, new_y