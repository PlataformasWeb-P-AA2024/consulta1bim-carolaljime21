from pymongo import MongoClient

# Conectar a MongoDB
client = MongoClient('mongodb://localhost:27017/')  # Ajusta la URI según sea necesario
db = client['data']
collection = db['torneos']

# Realizar la consulta para obtener los ganadores únicos de cada torneo
result = collection.aggregate([
    # Agrupar por el nombre del torneo
    { '$group': { '_id': '$Tournament', 'ganadores': { '$addToSet': '$Winner' } } }
])

# Imprimir los resultados
for doc in result:
    print(f"\nNOMBRE DEL TORNEO: {doc['_id']}")
    print("GANADORES:")
    for ganador in doc['ganadores']:
        print("- " + ganador)
