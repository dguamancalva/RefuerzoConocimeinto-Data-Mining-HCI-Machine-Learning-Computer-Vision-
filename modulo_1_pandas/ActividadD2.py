import pandas as pd

datos_ventas = {
    'Tienda': ['Norte', 'Sur', 'Norte', 'Sur', 'Centro', 'Centro', 'Norte'],
    'Producto': ['Laptop', 'Mouse', 'Teclado', 'Laptop', 'Monitor', 'Teclado', 'Mouse'],
    'Cantidad': [2, 10, 5, 1, 3, 8, 12],
    'Precio_Unitario': [800.00, 20.00, 40.00, 850.00, 250.00, 45.00, 22.00]
}

tablaValores = pd.DataFrame(datos_ventas)

tablaValores['ValorTotal'] = (tablaValores['Cantidad']) * (tablaValores['Precio_Unitario'])

tablaUnida = tablaValores.groupby('Tienda')['ValorTotal'].sum()

print(tablaValores)

print(tablaUnida)
