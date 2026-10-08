import pandas as pd
import joblib
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_predict, GridSearchCV
import plotly.express as px

dtframe = pd.read_csv('evaluacion_semanal_2/ventas_clientes_sucias.csv')
print("DATA FRAME SUCIOOOO")
print(dtframe)

# simple imputer
imputer_nulos = SimpleImputer(strategy= 'median')
dtframe[['Ingresos_k']] = imputer_nulos.fit_transform(dtframe[['Ingresos_k']])
print("DATA FRAME SIN NULOSSSS")
print(dtframe)

##FIltrar outliers con IQR

Q1 = dtframe['Monto_Gasto'].quantile(0.25)
Q3 =dtframe['Monto_Gasto'].quantile(0.75)

IQR = Q3-Q1

limite_inf = Q1 - 1.5 * IQR
limite_sup = Q3 + 1.5 * IQR

df_limpio = dtframe[(dtframe['Monto_Gasto']>= limite_inf) & (dtframe['Monto_Gasto']<= limite_sup)]
print("DATA FRAME LIMPIECITO")
print(df_limpio)

df_limpio.to_csv('evaluacion_semanal_2/ventas_clientes_limpiecito.csv', index= False)

#SEPARAR X , Y

X= df_limpio[['Cliente_ID','Edad','Ingresos_k','Monto_Gasto']]
y= df_limpio['Cliente_Frecuente']
## ML CON GRIDSEARCH CV

datosGrid = { 
    'max_depth' : [3, 5, 10, None],
    'criterion'  : ['gini', 'entropy'],
    'min_samples_split' : [2, 4, 6]
}

grid = GridSearchCV(DecisionTreeClassifier(random_state= 42),  datosGrid, cv=3)
grid.fit(X,y)

print("MEjores HIPERPARAMETROS: ", grid.best_params_)
print(f"Mejor Exactitud : {grid.best_score_ * 100: .2f}%")

joblib.dump(grid.best_estimator_, 'evaluacion_semanal_2/mejorModelo.joblib')
print("Mejor modelo exportado exitosamente a joblib")

grafica1 = px.scatter(df_limpio, x='Ingresos_k', y='Monto_Gasto', color='Cliente_Frecuente', title='Ingressos vs Monto')
grafica1.write_html('evaluacion_semanal_2/ingresos_scatter.html')

print("Grafica creada correctamente")
