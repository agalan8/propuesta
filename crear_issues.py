import requests
import pandas as pd

# URL y cabeceras de la API de GitHub
API_URL_LABELS = 'https://api.github.com/repos/agalan8/E-Shelf/labels'  # URL de tu repositorio
API_URL_ISSUES = 'https://api.github.com/repos/agalan8/E-Shelf/issues'  # URL para crear issues en tu repositorio
API_URL_MILESTONES = 'https://api.github.com/repos/agalan8/E-Shelf/milestones'  # URL para crear milestones en tu repositorio
HEADERS = {
    'Authorization': 'Bearer {TOKEN}',
    "Accept": "application/vnd.github.v3+json",
    "Content-Type": "application/json"
}

# Las etiquetas que deseas usar
ETIQUETAS = {
    'Prioridad': ['Importante', 'Mínima', 'Opcional'],
    'Tipo': ['Funcional', 'Técnico'],
    'Complejidad': ['Fácil', 'Media', 'Difícil']
}

# Función para crear una nueva etiqueta
def crear_etiqueta(nombre):
    data = {
        'name': nombre,
        'color': 'ffffff',  # Puedes elegir el color que desees
        'description': f'Etiqueta {nombre}'
    }
    respuesta = requests.post(API_URL_LABELS, headers=HEADERS, json=data)

    if respuesta.status_code == 201:
        print(f"Etiqueta '{nombre}' creada con éxito.")
    else:
        print(f"Error al crear la etiqueta '{nombre}': {respuesta.status_code}")
        print(respuesta.text)

# Función para verificar y crear etiquetas necesarias
def verificar_y_crear_etiquetas():
    """Verifica si las etiquetas necesarias existen, si no, las crea."""
    respuesta = requests.get(API_URL_LABELS, headers=HEADERS)

    if respuesta.status_code == 200:
        try:
            etiquetas_existentes = [etiqueta['name'] for etiqueta in respuesta.json()]
            for grupo in ETIQUETAS.values():
                for etiqueta in grupo:
                    if etiqueta not in etiquetas_existentes:
                        crear_etiqueta(etiqueta)
        except ValueError:
            print("Error: la respuesta no es un JSON válido")
            print("Contenido de la respuesta:", respuesta.text)
    else:
        print(f"Error al obtener las etiquetas. Codigo de estado: {respuesta.status_code}")
        print("Contenido de la respuesta:", respuesta.text)

# Función para verificar y crear un milestone
def crear_milestone(nombre):
    # Primero verificamos si el milestone ya existe
    respuesta = requests.get(API_URL_MILESTONES, headers=HEADERS)

    if respuesta.status_code == 200:
        milestones = respuesta.json()
        # Comprobamos si el milestone ya existe
        for milestone in milestones:
            if milestone['title'] == nombre:
                print(f"El milestone '{nombre}' ya existe.")
                return milestone['number']
    else:
        print(f"Error al obtener los milestones. Codigo de estado: {respuesta.status_code}")
        print("Contenido de la respuesta:", respuesta.text)

    # Si no existe, lo creamos
    data = {
        'title': nombre,
        'state': 'open'  # El estado puede ser 'open' o 'closed'
    }
    respuesta = requests.post(API_URL_MILESTONES, headers=HEADERS, json=data)

    if respuesta.status_code == 201:
        print(f"Milestone '{nombre}' creado con éxito.")
        return respuesta.json()['number']
    else:
        print(f"Error al crear el milestone '{nombre}': {respuesta.status_code}")
        print(respuesta.text)

# Función para crear un issue en GitHub
def crear_issue(codigo, titulo, descripcion, etiquetas, milestone=None):
    # El título del issue será el Codigo seguido del Título
    titulo_issue = f"[{codigo}] {titulo}"
    data = {
        'title': titulo_issue,
        'body': descripcion,
        'labels': etiquetas
    }

    if milestone:
        data['milestone'] = milestone  # Asigna el milestone si existe

    respuesta = requests.post(API_URL_ISSUES, headers=HEADERS, json=data)

    if respuesta.status_code == 201:
        print(f"Issue '{titulo_issue}' creado con éxito.")
    else:
        print(f"Error al crear el issue '{titulo_issue}': {respuesta.status_code}")
        print(respuesta.text)

# Función principal
def main():
    # Lee el archivo CSV
    df = pd.read_csv('requisitos.csv')  # Ruta al archivo CSV

    # Eliminar espacios en blanco de los nombres de las columnas
    df.columns = df.columns.str.strip()

    # Verifica y crea las etiquetas necesarias
    verificar_y_crear_etiquetas()

    # Crear los issues en GitHub
    for _, row in df.iterrows():
        codigo = row['Código']  # Asumimos que la columna 'Código' existe en tu archivo CSV
        print(f"Creando issue: [{codigo}] {row['Descripción corta']}")

        # Asume que las etiquetas están en las columnas del archivo CSV
        etiquetas = [row['Prioridad'], row['Tipo'], row['Complejidad']]

        # Si 'Entrega' está en el archivo, lo usamos como milestone
        if 'Entrega' in row and pd.notnull(row['Entrega']):
            milestone = crear_milestone(row['Entrega'])
        else:
            milestone = None

        # Crea el issue con las etiquetas y el milestone
        crear_issue(codigo, row['Descripción corta'], row['Descripción larga'], etiquetas, milestone)

if __name__ == '__main__':
    main()
