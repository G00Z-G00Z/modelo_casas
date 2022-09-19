import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn import tree
from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeRegressor


dataset_path = "./dataset/Housing.csv"

# Leer la tabla
table = pd.read_csv(dataset_path)


# Obtener X y Y
columnYname = "price"

columnas = ["area", "bedrooms", "bathrooms", "price"]

featuresColNames = filter(lambda col : col != columnYname, columnas)
yColName = filter(lambda col : col == columnYname, columnas)

X = table.loc[:, featuresColNames]
Y = table.loc[:, yColName]

X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state = 0, train_size = 0.70)






