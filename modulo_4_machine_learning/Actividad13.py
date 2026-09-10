import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report

# Datos de clientes bancarios: Ingresos, Deudas y Riesgo (1=Alto Riesgo, 0=Sin Riesgo)
datos_banco = {
    'Ingresos': [1500, 2000, 4000, 1200, 3000, 5000, 1800, 2500, 4500, 1100, 3200, 2800, 1600, 4100, 2200],
    'Deudas': [800, 1500, 200, 900, 500, 100, 1200, 600, 300, 1000, 400, 700, 1100, 250, 950],
    'Riesgo': [1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1]
}
df_banco = pd.DataFrame(datos_banco)

X = df_banco[['Ingresos', 'Deudas']]
y = df_banco['Riesgo']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.3, random_state= 42 )

modelo= DecisionTreeClassifier(random_state=42)
modelo.fit(X_train, y_train)

prediccion = modelo.predict(X_test)
matriz = confusion_matrix(y_test, prediccion)

print(matriz)

reporte = classification_report(y_test, prediccion)
print(reporte)

sns.heatmap(matriz, annot=True, cmap='Blues')
plt.title('Matriz de confusion del model Bancario')
plt.savefig('matriz.png')
plt.close()

