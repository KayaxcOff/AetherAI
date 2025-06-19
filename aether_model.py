import pandas as pd

dataSet = pd.read_excel("aet_data.xlsx")

x = dataSet.drop(columns=["System_Response(CPU)", "System_Response(RAM)"], axis=1).values
y = dataSet[["System_Response(CPU)", "System_Response(RAM)"]].values

x = pd.get_dummies(x)
y = pd.get_dummies(y)
