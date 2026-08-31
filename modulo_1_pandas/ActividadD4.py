import pandas as pd

# Tabla izquierda: Empleados
tablaEmpleados = pd.DataFrame({
    'Nombre': ['Ana', 'Luis', 'Carlos', 'María'],
    'ID_Depto': [101, 102, 101, 103]
})
# Tabla derecha: Departamentos
tablaDeptos = pd.DataFrame({
    'ID_Depto': [101, 102, 104],
    'Nombre_Depto': ['Tecnología', 'Ventas', 'Finanzas']
})

tablaInner = pd.merge(tablaEmpleados, tablaDeptos, on='ID_Depto', how ='inner')

tablaLeft = pd.merge(tablaEmpleados, tablaDeptos, on ='ID_Depto', how = 'left')


print(tablaInner)
print(tablaLeft)
print('Respondiendo la pregunta, en maria con inner lo que sucede aqui es que la fuincion solo mostrara los datos que se relacionan, y al momento de querer mostrar maria no se ve por que en lastablas no habia coincidencia por eso no se muestra, mientras en left como estamos haciendo que tome todos los datos que estan en la priemra tabla por eso muestra todos los id depratamento de lapriemra tabla con los que son de la tabla dos ')
print('finanzas con inner no se muestra por que no hay datos similares en la tabla por ende no se lo tomo en cuenta, mientras en left tampoco sale por que no hay datos que lo relacion y con la tabla uno pero como mecnionamos se mostrara todos los datos de la trabla uno y los de la tabla dos solo los que tengan coincidencia')