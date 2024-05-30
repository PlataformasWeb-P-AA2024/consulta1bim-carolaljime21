import pandas as pd
from pymongo import MongoClient

# Ruta al archivo CSV
archivo = 'atp_tennis.csv'

# Leer el archivo CSV
df = pd.read_csv(archivo)

# Conectar a MongoDB
client = MongoClient('mongodb://localhost:27017/')  # Conectamos a nuestra URI de MOngoDB en este casi sería el LocalHost
db = client['data'] #Conectamos con nuestra base de datos, en este caso "data", sino existe, Mongo la creará.
collection = db['torneos'] #Accede a la colección con el nombre de "torneos", y si es que no existe, Mongo la creará.

# Convertir el DataFrame de pandas a una lista de diccionarios
data = df.to_dict(orient='records')

# Insertar los datos en la colección de MongoDB
collection.insert_many(data)
