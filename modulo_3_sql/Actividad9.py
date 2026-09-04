import sqlite3
import pandas as pd

conexion = sqlite3.connect(':memory:')

datos_empleados = {
    'ID': [1, 2, 3, 4, 5, 6],
    'Nombre': ['Ana', 'Luis', 'Carlos', 'María', 'Juan', 'Sofía'],
    'Departamento': ['IT', 'Ventas', 'IT', 'Marketing', 'Ventas', 'IT'],
    'Salario': [3500, 2200, 4000, 3100, 2500, 3800],
    'Ciudad': ['Quito', 'Guayaquil', 'Quito', 'Cuenca', 'Guayaquil', 'Quito']
}

df_base= pd.DataFrame(datos_empleados)

df_base.to_sql('empleados', conexion, index= False , if_exists= 'replace')

primerREsultadoPRueba = pd.read_sql_query("SELECT * FROM empleados WHERE Salario > 3000",conexion)
print(primerREsultadoPRueba)

segundoREsul= pd.read_sql_query("SELECT Nombre,Salario FROM empleados WHERE Ciudad = 'Quito' ORDER BY Salario DESC", conexion)
print(segundoREsul)

tercerResult= pd.read_sql_query("SELECT Departamento,AVG(Salario), COUNT(ID) FROM empleados GROUP BY Departamento ", conexion)
print(tercerResult)