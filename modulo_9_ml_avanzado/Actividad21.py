import pandas as pd
import joblib
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score, GridSearchCV

# Cargar los datos

df_Cargado = pd.read_csv('modulo_9_ml_avanzado/clientes_telecom.csv')

df_Cargado = pd.DataFrame(df_Cargado)
print(df_Cargado)

# Separar X y
X = df_Cargado[['Meses_Contrato', 'Factura_Mensual', 'Soporte_Tecnico']]
y = df_Cargado['Fuga_Cliente']

# k-ford cross validation 
modelo_base = DecisionTreeClassifier(random_state=42)
scores = cross_val_score(modelo_base, X, y, cv=5)
print(f"Exactitud promedio K-Fols (5 parametros): {scores.mean() * 100:.2f}%")

# GridSearch

datosGrid = { 
    'max_depth' : [3, 5, 10, None],
    'criterion'  : ['gini', 'entropy'],
    'min_samples_split' : [2, 4, 6]
}

grid = GridSearchCV(DecisionTreeClassifier(random_state=42), datosGrid, cv=5 )
grid.fit(X,y)

print("MEjores HIPERPARAMETROS: ", grid.best_params_)
print(f"Mejor Exactitud : {grid.best_score_ * 100: .2f}%")

# Exportar el mejor modelo

joblib.dump(grid.best_estimator_, 'modulo_9_ml_avanzado/mejorModeloChurn.joblib')
print("Mejor modelo exportado exitosamente a joblib")
