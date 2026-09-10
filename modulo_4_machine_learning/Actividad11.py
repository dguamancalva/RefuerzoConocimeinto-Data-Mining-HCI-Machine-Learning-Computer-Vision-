import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import export_text

# Dataset de entrenamiento: Edad, Salario y si Compró (1) o No (0)
datos_clientes = {
    'Edad': [22, 25, 47, 52, 46, 56, 55, 60, 28, 30, 21, 50, 49, 23, 58],
    'Salario': [20000, 25000, 80000, 110000, 75000, 90000, 120000, 140000, 32000, 45000, 18000, 95000, 88000, 22000, 130000],
    'Compro': [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1]
}

df_clientes = pd.DataFrame(datos_clientes)


X = df_clientes[['Edad', 'Salario']]
y = df_clientes['Compro']


X_train, X_test, y_train, y_test =  train_test_split(X, y, test_size=0.2, random_state=42)

primerModelo = DecisionTreeClassifier(random_state=42)
primerModelo.fit(X_train, y_train)

predicciones = primerModelo.predict(X_test)

precision = accuracy_score(y_test, predicciones)

print(f"Presicion del modelo: {precision * 100}%")

clienteJoven= [[22, 20000]]
resultadoJoven = primerModelo.predict(clienteJoven)
print(f"Comprara el cliente joven (22 anios, 20k$)?: {resultadoJoven}")

reglasIa = export_text(primerModelo, feature_names=['Edad', 'Salario'])
print("\n -- Las reglas de la Ia que aprendio por dentro --")
print(reglasIa)