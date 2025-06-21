import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

dataSet = pd.read_excel("aet_data_2.xlsx")

x = dataSet.drop(columns=["System_Response(CPU)", "System_Response(RAM)"], axis=1).values
y = dataSet[["System_Response(CPU)", "System_Response(RAM)"]].values

x_train, x_test, y_train, y_test = train_test_split(x=x, y=y, test_size=0.2, random_state=42)

def scale_data(train, test):
    scaler = StandardScaler()
    train_data = scaler.fit_transform(train)
    test_data = scaler.transform(test)
    return train_data, test_data

x_train, x_test = scale_data(x_train, x_test)
y_train, y_test = scale_data(y_train, y_test)

def train_model(train_1, train_2):
    pass

train_model(x_train, y_train)
