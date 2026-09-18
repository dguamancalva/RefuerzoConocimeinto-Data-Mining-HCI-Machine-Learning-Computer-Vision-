import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

# 1. Crear el DataFrame
data = {
    'Edad': [22, 25, 47, 52, 46, 56, 23, 40],
    'Ingresos_k': [20, 25, 70, 80, 75, 90, 22, 60],
    'Tipo_Cliente': ['Bronce', 'Bronce', 'Oro', 'Platino', 'Oro', 'Platino', 'Bronce', 'Oro'],
    'Compro_Casa': [0, 0, 1, 1, 1, 1, 0, 1]
}
df = pd.DataFrame(data)

#ONe HOt encoding

datacod = pd.get_dummies(df, columns= ['Tipo_Cliente'], dtype= int)

# Machine Learning

X = datacod.drop(columns=['Compro_Casa'])
y = datacod['Compro_Casa']

X_train, X_test, y_train, y_test =  train_test_split(X, y, test_size= 0.25, random_state=42)

modeloEntrenado = DecisionTreeClassifier(random_state=42)
modeloEntrenado.fit(X_train, y_train)

prediccion = modeloEntrenado.predict(X_test)
matrizConfusion = confusion_matrix(y_test, prediccion)
print(f"informe de presicion: {matrizConfusion}%")

presicion = accuracy_score(y_test, prediccion)
print(f"informe de presicion: {presicion}%")

#Plotly

grafico1 = px.scatter(datacod, x= 'Edad', y='Ingresos_k', color= 'Compro_Casa' )
grafico1.write_html('evaluacion_final/dashboar_Cliente.html')

print("Ejecuacion realizada con exito")