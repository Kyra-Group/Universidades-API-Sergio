from pymongo import MongoClient

# Conexion URI base de datos
MONGO_URI = 'mongodb+srv://smartinez:12345ASDFG@cluster0.fl0s4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
client = MongoClient(MONGO_URI)

# Elegir base datos
db = client['Centros']

# Funcion con parametro de entrada diccionario
def guardar_centros_mongo(universidades:list):
    print(universidades)
    if not isinstance(universidades, list) or not universidades:
        raise ValueError("El argumento 'universidades' debe ser un diccionario no vacío")
    collection = db['Centros']
    try:
        resultados = collection.insert_many(universidades,ordered=False)
        print(type(resultados))
    except Exception as e:
        print(f"Error al guardar en MongoDB: {e}")
        return []
    