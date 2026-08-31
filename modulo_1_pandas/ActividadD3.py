import pandas as pd
import numpy as np 

datos_empleados = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'María', 'Juan', 'Sofía'],
    'Departamento': ['IT', 'Ventas', 'IT', 'Marketing', 'Ventas', 'HR'],
    'Edad': [28, np.nan, 35, 40, np.nan, 30],
    'Salario': [3000.00, 2500.00, np.nan, 4000.00, 2200.00, np.nan]
}


tablaInicial = pd.DataFrame(datos_empleados)

valoresPromedio = tablaInicial['Edad'].mean()

tablaInicial['Edad'] = tablaInicial['Edad'].fillna(valoresPromedio)

limpiarNan = tablaInicial.dropna(subset=['Salario'])

print(limpiarNan)