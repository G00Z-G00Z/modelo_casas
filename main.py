import pandas as pd


dataset_path = "./dataset/Housing.csv"

# Leer la tabla
table = pd.read_csv(dataset_path)

columnas = ["area", "bedrooms", "bathrooms", "price"]

table2 = table.loc[:, columnas]



print(table2)

