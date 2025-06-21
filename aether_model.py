import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib

dataSet = pd.read_excel("aet_data.xlsx")

x = dataSet.drop(columns=["System_Response(CPU)", "System_Response(RAM)"], axis=1).values
y = dataSet[["System_Response(CPU)", "System_Response(RAM)"]].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

def scale_data(train, test):
  scaler = StandardScaler()
  train_data = scaler.fit_transform(train)
  test_data = scaler.transform(test)
  return train_data, test_data

x_train, x_test = scale_data(x_train, x_test)
y_train, y_test = scale_data(y_train, y_test)

def train_model(train_1, train_2):
  model = RandomForestRegressor()
  model.fit(train_1, train_2)
  return model

aet = train_model(x_train, y_train)

def test_model(model, test_1, test_2, mse_edge):
  predictions = model.predict(test_1)
  mse = mean_squared_error(test_2, predictions)
  r_2 = r2_score(test_2, predictions)
  print(f"MSE: {mse}")
  print(f"R^2: {r_2}")

  if mse < mse_edge:
    print("Model başarılı, modeli kaydetme işlemi başladı")
    try:
      joblib.dump(model, "aether_ai.pkl")
      print("Model başarıyla kaydedildi")
    except Exception as e:
      print(f"Model kaydedilmedi!!! Hata: {e}")
  else:
    print("Model başarısız oldu")
  return predictions

test_model(aet, x_test, y_test, 0.10)
