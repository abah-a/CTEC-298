# Code cell 1: Numpy Arrays
# Note: Requires numpy installation

weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

try:
    import numpy as np

    np_weight_kg = np.array(weight_kg)
    np_weight_lbs = np_weight_kg * 2.2

    print(np_weight_lbs)
except ModuleNotFoundError:
    print("Numpy module is not installed.")


# Code cell 2: Pandas Basic
# Note: Requires pandas installation and 'cars.csv' file in the same directory

try:
    import pandas as pd

    cars = pd.read_csv('cars.csv', index_col=0)

    print(cars.iloc[2])
    print(cars.loc[['AUS', 'EG']])
except ModuleNotFoundError:
    print("Pandas module is not installed.")
except FileNotFoundError:
    print("cars.csv file is not found in the directory.")
