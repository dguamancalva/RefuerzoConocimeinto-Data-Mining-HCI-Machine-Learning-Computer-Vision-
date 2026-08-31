import pandas as pd
import numpy as np

# Tabla 1: Datos Personales de Clientes
datos_clientes = {
    'ID_Cliente': [1, 2, 3, 4, 5],
    'Edad': [25, np.nan, 45, 30, np.nan],
    'Nivel_Membresia': ['Bronce', 'Oro', 'Plata', 'Bronce', 'Oro'],
    'Ciudad': ['Quito', 'Guayaquil', 'Cuenca', 'Quito', 'Guayaquil']
}

# Tabla 2: Historial de Compras
datos_compras = {
    'ID_Cliente': [1, 2, 3, 3, 5, 6],
    'Monto_Compra': [120.00, 450.00, 50.00, 80.00, 300.00, 150.00],
    'Descuento_Aplicado': [10.00, np.nan, 5.00, np.nan, 30.00, 15.00]
}



tablaClientes = pd.DataFrame(datos_clientes)
tablaCompras = pd.DataFrame(datos_compras)



promedioEdad = tablaClientes['Edad'].mean()

#Primera parte
tablaClientes['Edad'] = tablaClientes['Edad'].fillna(promedioEdad)

tablaCompras['Descuento_Aplicado']= tablaCompras['Descuento_Aplicado'].fillna(0)

#Segunda parte
dt_frame = pd.merge(tablaClientes, tablaCompras, on='ID_Cliente', how='left')

#Tercera Parte
dt_frame['Monto_Neto'] = (dt_frame['Monto_Compra'])-(dt_frame['Descuento_Aplicado'])

dt_frame['Monto_Neto'] = dt_frame['Monto_Neto'].fillna(0)

#Cuarta Parte
tablaCiudades = dt_frame.groupby('Ciudad')['Monto_Neto'].sum()

#QUinta parte
NivelMembresia = {'Bronce': 0, 'Plata': 1, 'Oro': 2}
dt_frame['Nivel_Membresia'] = dt_frame['Nivel_Membresia'].map(NivelMembresia)

dt_master = pd.get_dummies(dt_frame, columns=['Ciudad'], dtype= int)

print(tablaClientes)
print(tablaCompras)
print(dt_frame)
print(tablaCiudades)
print(dt_master)