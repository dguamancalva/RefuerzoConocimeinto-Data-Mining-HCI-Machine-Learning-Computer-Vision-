import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

# Dataset de casas
datos_casas = {
    'Metros_Cuadrados': [50, 65, 80, 90, 110, 120, 140, 160, 180, 200],
    'Habitaciones': [1, 2, 2, 3, 3, 3, 4, 4, 5, 5],
    'Precio_Dolares': [45000, 58000, 72000, 85000, 98000, 110000, 125000, 142000, 160000, 180000]
}
df_casas = pd.DataFrame(datos_casas)

X = df_casas[['Metros_Cuadrados', 'Habitaciones']]
y = df_casas['Precio_Dolares']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2 ,random_state= 42)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

predicciones = modelo.predict(X_test)
r2 = r2_score(y_test, predicciones)

print(r2)
mediaError = mean_absolute_error(y_test, predicciones)
print(mediaError)

casa_nueva = pd.DataFrame([{'Metros_Cuadrados': 100, 'Habitaciones': 3}])

modelo.predict(casa_nueva)
print(modelo.predict(casa_nueva))