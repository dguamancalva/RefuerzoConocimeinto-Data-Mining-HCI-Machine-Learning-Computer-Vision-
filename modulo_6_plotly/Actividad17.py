import pandas as pd
import plotly.express as px

# 1. Crear el DataFrame
data = {
    'Producto': ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Audífonos', 'Silla Gamer'],
    'Categoria': ['Tecnología', 'Accesorios', 'Accesorios', 'Tecnología', 'Accesorios', 'Muebles'],
    'Ventas': [1500, 300, 450, 800, 200, 600],
    'Satisfaccion': [4.8, 4.2, 4.5, 4.6, 3.9, 4.4]
}
df = pd.DataFrame(data)

fig1 = px.scatter(df, x= 'Satisfaccion', y = 'Ventas', color='Categoria', hover_data=['Producto'], title='Relacion de Satisfaccion vs Ventas')
fig1.write_html('modulo_6_plotly/ventas_scatter.html')

fig2 = px.bar(df, x = 'Ventas', y = 'Producto', color='Categoria', title='Ventas totales por producto')
fig2.write_html('modulo_6_plotly/ventas_barras.html')

print("Archivos interactivos creados con exito")