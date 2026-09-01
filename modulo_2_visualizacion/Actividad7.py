import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

datos_ventas = {
    'Producto': ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Audífonos', 'Cam', 'Tablet'],
    'Categoria': ['Tech', 'Accesorios', 'Accesorios', 'Tech', 'Accesorios', 'Tech', 'Tech'],
    'Ventas_Totales': [12000, 1500, 3000, 8500, 2200, 4100, 6300],
    'Satisfaccion': [4.8, 4.2, 4.0, 4.6, 3.9, 4.1, 4.5]
}

df_ventas= pd.DataFrame(datos_ventas)

sns.barplot(x="Producto", y="Ventas_Totales", data=df_ventas, )
plt.title('Ventas Totales por Producto')
plt.savefig('imagen1.png')
plt.close()

sns.scatterplot(x= "Satisfaccion", y="Ventas_Totales", hue="Categoria", data=df_ventas)
plt.title('Satisfaccion de las ventas totales dividido por Categoria')
plt.savefig('imagen2.png')
plt.close()