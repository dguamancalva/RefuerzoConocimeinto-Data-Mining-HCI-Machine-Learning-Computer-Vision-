import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# Datos de clientes: Ingresos Anuales (en miles $) y Puntaje de Gasto (1-100)
datos_clientes = {
    'Ingresos_Anuales_k': [15, 16, 17, 18, 19, 60, 62, 65, 70, 75, 100, 105, 110, 120, 125],
    'Puntaje_Gasto': [39, 81, 6, 77, 40, 42, 55, 48, 50, 52, 17, 83, 12, 79, 15]
}
df_clientes = pd.DataFrame(datos_clientes)

X = df_clientes[['Ingresos_Anuales_k','Puntaje_Gasto']]

inercia = []

for k in range(1,7):
    kmeans = KMeans(n_clusters = k, random_state=42)
    kmeans.fit(X)
    inercia.append(kmeans.inertia_)


sns.lineplot(x = range(1, 7), y = inercia)
plt.title('Metodo del codo')
plt.savefig('metodoCodo.png')
plt.close()


modeloFinal = KMeans(n_clusters = 3, random_state = 42)
df_clientes['Cluster'] = modeloFinal.fit_predict(X)

sns.scatterplot(x ='Ingresos_Anuales_k', y = 'Puntaje_Gasto', hue= 'Cluster',data= df_clientes, palette= 'viridis')
plt.title('Segmentacion de clientes con K-means')
plt.savefig('clusterCLientes.png')
plt.close()

print(df_clientes)