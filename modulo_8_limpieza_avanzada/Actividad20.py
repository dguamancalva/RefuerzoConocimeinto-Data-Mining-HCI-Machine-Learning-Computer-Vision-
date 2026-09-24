import pandas as pd
from sklearn.impute import SimpleImputer
import plotly.express as px

dfCargado = pd.read_csv('modulo_8_limpieza_avanzada/empleados_sucios.csv')

dfCargado = pd.DataFrame(dfCargado)
print("--------------------DATAFRAME SUCIO----------------------------")
print(dfCargado)

## Imputacion de nulos con mediana

imputer = SimpleImputer(strategy = 'median')
dfCargado[['Edad', 'Salario_USD']] = imputer.fit_transform(dfCargado[['Edad', 'Salario_USD']])
print("--------------------DATAFRAME SIN NULOS---------------------------")
print(dfCargado)


## Filtrado OUTLIERS CON IQR

Q1 = dfCargado['Salario_USD'].quantile(0.25)
Q3 = dfCargado['Salario_USD'].quantile(0.75)

IQR = Q3 - Q1
limite_inf = Q1 - 1.5 * IQR
limite_sup = Q3 + 1.5 * IQR

df_limpio = dfCargado[(dfCargado['Salario_USD'] >= limite_inf) & (dfCargado['Salario_USD'] <= limite_sup)]

print("--------------------DATAFRAME LIMPIO SIN OUTLIERS---------------------------")
print(df_limpio)

##Guardar archivo csv

df_limpio.to_csv('modulo_8_limpieza_avanzada/empleados_limpios.csv', index = False)

# Plotly grafica 

grafica1 = px.box(df_limpio, y='Salario_USD', title = 'Slario Limpios MEtodo IQR')
grafica1.write_html('modulo_8_limpieza_avanzada/salarios_boxplot.html')
print("Grafico generado satisfactoriamente")

