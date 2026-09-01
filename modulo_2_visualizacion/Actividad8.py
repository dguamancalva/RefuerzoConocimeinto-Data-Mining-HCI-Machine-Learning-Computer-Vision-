import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

datos_casas = {
    'Habitaciones': [2, 3, 3, 4, 2, 5, 3, 10], # ¡Atención al 10!
    'Metros_Cuadrados': [60, 90, 85, 120, 65, 150, 95, 500],
    'Distancia_Centro_KM': [15, 10, 8, 5, 12, 3, 9, 2],
    'Precio_Miles': [50, 85, 80, 130, 55, 170, 90, 600]
}

df_casas= pd.DataFrame(datos_casas)

sns.boxplot(data= df_casas, x="Habitaciones")
plt.title("Deteccion de outlers en Habitaciones")
plt.savefig('boxtplot_habitaciones.png')
plt.close()

#Matriz de correlacion

matrizCorrelacion = df_casas.corr()

sns.heatmap(data=matrizCorrelacion, annot=True)
plt.title("Matriz de correlacion de propiedades")
plt.savefig('heatmap_correlacion.png')
plt.close()
