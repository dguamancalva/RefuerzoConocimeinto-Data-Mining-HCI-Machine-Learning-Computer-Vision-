import sqlite3
import pandas as pd

conexion = sqlite3.connect(':memory:')

# Tabla 1: Clientes (Tabla Izquierda)
df_clientes = pd.DataFrame({
    'id_cliente': [1, 2, 3, 4],
    'nombre': ['Ana', 'Luis', 'Carlos', 'María'],
    'ciudad': ['Quito', 'Guayaquil', 'Cuenca', 'Quito']
})

# Tabla 2: Pedidos (Tabla Derecha)
df_pedidos = pd.DataFrame({
    'id_pedido': [101, 102, 103, 104],
    'id_cliente': [1, 1, 2, 5], # El cliente 5 no existe en la tabla de clientes
    'monto': [150.00, 200.00, 50.00, 300.00]
})

df_clientes.to_sql('clientes', conexion, index=False, if_exists='replace')

df_pedidos.to_sql('pedidos', conexion, index=False, if_exists='replace' )

primerREsul = pd.read_sql_query(
    "SELECT * FROM clientes  INNER JOIN pedidos ON  clientes.id_cliente = pedidos.id_cliente", conexion)
print(primerREsul)

segunResultado = pd.read_sql_query("SELECT * FROM clientes LEFT JOIN pedidos ON clientes.id_cliente = pedidos.id_cliente", conexion)
print(segunResultado)

tercerREsult = pd.read_sql_query("SELECT clientes.nombre, SUM(pedidos.monto) FROM clientes INNER JOIN pedidos ON clientes.id_cliente = pedidos.id_cliente GROUP BY clientes.nombre ", conexion)
print(tercerREsult)