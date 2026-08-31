import pandas as pd

datos_clientes = {
    'Cliente': ['Juan', 'Pedro', 'Sofía', 'Ana', 'Carlos'],
    'Nivel_Educativo': ['Secundaria', 'Postgrado', 'Universitario', 'Secundaria', 'Universitario'],
    'Ciudad': ['Quito', 'Guayaquil', 'Cuenca', 'Quito', 'Guayaquil']
}

tablaClientes = pd.DataFrame(datos_clientes)



mapeoNivel = {'Secundaria': 0, 'Universitario': 1, 'Postgrado':2}

tablaClientes['Nivel_Educativo_Cod'] = tablaClientes['Nivel_Educativo'].map(mapeoNivel)

oneHot = pd.get_dummies(tablaClientes, columns=['Ciudad'], dtype = int)

print(tablaClientes)
print(oneHot)