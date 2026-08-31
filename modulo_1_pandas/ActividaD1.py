import pandas as pd

datos = {
    'Producto': ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Audífonos'],
    'Categoría': ['Tecnología', 'Accesorios', 'Accesorios', 'Tecnología', 'Accesorios'],
    'Precio': [850.00, 25.50, 45.00, 300.00, 60.00],
    'Stock': [15, 100, 50, 8, 0]
}

lista_creada = pd.DataFrame(datos)

datos_condicionados = (lista_creada['Precio'] > 50.00) & (lista_creada['Stock'] > 0)

datos_filtrados = lista_creada[datos_condicionados]


print(datos_filtrados[['Producto', 'Precio']])