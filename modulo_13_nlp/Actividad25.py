import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB

dfProductos = pd.read_csv('modulo_13_nlp/resenas_productos.csv')
print(dfProductos)


vectorizar = TfidfVectorizer(strip_accents= 'unicode', lowercase= True)
X = vectorizar.fit_transform(dfProductos['Resena'])
y = dfProductos['Sentimiento']


modelo = MultinomialNB()
modelo.fit(X, y)


nueva_frase = ["El producto es maravilloso me encanto",
                "Producto muy feo no funciona",
                "El producto es maravilloso me encanto la calidad",
                "Una porqueria total de producto salio defectuoso"]

actualizado = vectorizar.transform(nueva_frase)
prediccion = modelo.predict(actualizado)


for frase, sent in zip(nueva_frase, prediccion):
    print(f"Opinion: '{frase}' ----> Sentimiento predicho: {sent}")
