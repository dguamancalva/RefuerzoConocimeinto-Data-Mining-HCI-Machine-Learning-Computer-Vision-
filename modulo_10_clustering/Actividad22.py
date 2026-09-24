import pandas as pd
from sklearn.metrics import silhouette_samples
from sklearn.cluster import KMeans
import plotly.express as px

dfCargado = pd.read_csv('modulo_10_clustering/clientes_comportamiento.csv')

df = pd.DataFrame(dfCargado)

print(df)

X = df[['Ingresos_Anuales_k', 'Gasto_Tienda_k']]

for k in range(2, 0):
    kmeans = KMeans(n_clusters= k, random_state= 42)
    labels = kmeans.fit_predict(X)
    score = silhouette_samples(X, labels)
    print(f"k = {k} -> silhoutter Score: {score : ,4f}" )

k_optimo = 3

kmeans_optimo = KMeans(n_clusters=k_optimo, random_state=42)
df['Cluster']= kmeans_optimo.fit_predict(X)
df['Cluster']= df['Cluster'].astype(str) #plotly lo trate como categoria

df.to_csv('modulo_10_clustering/clientes_segmentados.csv', index=False)

grafico= px.scatter(df, x= 'Ingresos_Anuales_k', y= 'Gasto_Tienda_k', color='Cluster', title= 'Segmentacion de clientes por comportamiento')

grafico.write_html('modulo_10_clustering/clientes_Segmentados.html')

print("Grafica creada satisfactoriamente")