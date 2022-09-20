import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn import tree
from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeRegressor


DATASET_PATH = "./dataset/Housing.csv"

# Leer la tabla
table = pd.read_csv(DATASET_PATH)


# Obtener X y Y
column_y_name = "price"
column_x_name = ["area", "bedrooms", "bathrooms"]


X = table.loc[:, column_x_name]
Y = table.loc[:, column_y_name]

X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state = 0, train_size = 0.70)






