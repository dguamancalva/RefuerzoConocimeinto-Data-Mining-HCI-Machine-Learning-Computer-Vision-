import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


conexion = sqlite3.connect(':memory:')

datos_banco = {
    'Edad': [22, 25, 47, 52, 46, 56, 55, 60, 28, 30, 21, 50, 49, 23, 58],
    'Nivel_Educativo': ['Secundaria', 'Universitario', 'Postgrado', 'Postgrado', 'Universitario', 'Postgrado', 'Universitario', 'Postgrado', 'Secundaria', 'Universitario', 'Secundaria', 'Postgrado', 'Universitario', 'Secundaria', 'Postgrado'],
    'Salario': [20000, 25000, 80000, 110000, 75000, 90000, 120000, 140000, 32000, 45000, 18000, 95000, 88000, 22000, 130000],
    'Aprobado': [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1]
}

pd.DataFrame(datos_banco).to_sql('solicitudes', conexion, index = False, if_exists= 'replace')


df_datosBanco = pd.read_sql_query("SELECT * FROM solicitudes", conexion)



mapeoNivelEducativo = {'Secundaria': 0,'Universitario':1, 'Postgrado': 2 }

df_datosBanco['Nivel_Educativo'] = df_datosBanco['Nivel_Educativo'].map(mapeoNivelEducativo)

print(df_datosBanco)

matrizCorrelacion = df_datosBanco.corr()

sns.heatmap(data = matrizCorrelacion, annot=True)
plt.title('Correlacion Bancaria')
plt.savefig('correlacionBancaria.png')
plt.close()

#Entrenamiento machine learning

X= df_datosBanco[['Edad', 'Nivel_Educativo', 'Salario']] 
y= df_datosBanco['Aprobado']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2 , random_state=42)

modelo = DecisionTreeClassifier(random_state=42)
modelo.fit(X_train, y_train)

prediccion = modelo.predict(X_test)
presicion = accuracy_score(y_test, prediccion)

print(f"Precision del modelo :{presicion * 100}%")

joblib.dump(modelo, 'modelo_credito.joblib')

modeloCargado = joblib.load('modelo_credito.joblib')

clienteNuevo = pd.DataFrame([{'Edad':35, 'Nivel_Educativo': 2, 'Salario':50000}]) 

prediccion = modeloCargado.predict(clienteNuevo)

print(prediccion)