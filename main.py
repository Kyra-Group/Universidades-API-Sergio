import traceback
from fastapi import FastAPI, HTTPException
from education_data import extraer_centros
from mongodb import guardar_centros_mongo

app = FastAPI()

@app.get('/')
def read_root():
    return{'Mensaje':'La aplicacion esta funcionando'}

@app.get('/buscar/')
def buscar_centros():
    try:

        centros = extraer_centros()
        print("Los centros son: ", centros)
        centros_guardados = guardar_centros_mongo(centros)
        print('Estos son los centros guardados', centros_guardados)
    except Exception as e:
        print("Error procesando la solicitud:")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
    return{'Mensaje':'La aplicacion esta buscando'}