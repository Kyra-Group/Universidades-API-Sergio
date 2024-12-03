import requests

url = 'https://educationdata.urban.org/api/v1/schools/ccd/directory/2022/'

# Realizamos la petición GET a la API
def extraer_centros():
    response = requests.get(url)
    
    # Verificamos si la solicitud fue exitosa
    if response.status_code == 200:
        datos = response.json()  # Convertimos la respuesta en JSON
        escuelas_info = []  # Lista para almacenar la información de las escuelas

        # Iteramos sobre los resultados y extraemos la información requerida
        for escuela in datos['results']:
            nombre_escuela = escuela.get('school_name', 'Desconocido')
            numero_profesores = escuela.get('teachers_fte', 'No disponible')
            numero_estudiantes = escuela.get('enrollment', 'No disponible')

            # Guardamos la información en un diccionario
            info = {
                'Nombre de la Escuela': nombre_escuela,
                'Número de Profesores': numero_profesores,
                'Número de Estudiantes': numero_estudiantes
            }
            escuelas_info.append(info)

        return escuelas_info
    else:
        print(f"Error en la solicitud: {response.status_code}")
        return None
    
