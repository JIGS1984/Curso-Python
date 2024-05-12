import pandas as pd
import requests
from bs4 import BeautifulSoup

# Función para extraer información de una URL
def extraer_info(url):
    try:
        # Hacer la solicitud HTTP
        destino = requests.get(url)
        # Crear objeto BeautifulSoup
        sopa = BeautifulSoup(destino.text, 'lxml')

        # Obtener título
        titulo = sopa.title.text.strip()

        # Obtener h1
        h1 = sopa.find('h1')
        h1_texto = h1.text.strip() if h1 else None

        # Obtener h2
        h2 = sopa.find('h2')
        h2_texto = h2.text.strip() if h2 else None

        # Obtener h3
        h3 = sopa.find('h3')
        h3_texto = h3.text.strip() if h3 else None

        # Obtener meta
        meta = sopa.find('meta', {'name': 'keywords'})
        meta_contenido = meta.get('content') if meta else None

        return titulo, h1_texto, h2_texto, h3_texto, meta_contenido
    except Exception as e:
        print(f"Error al procesar la URL {url}: {str(e)}")
        return None, None, None, None, None

# Leer el archivo Excel que contiene las URLs
archivo_excel_entrada = "urls_ortiz.xlsx"  # Nombre de tu archivo Excel de entrada
try:
    urls_df = pd.read_excel(archivo_excel_entrada)
    urls = urls_df['URLs'].tolist()  # Columna que contiene las URLs
except Exception as e:
    print(f"No se pudo leer el archivo Excel de entrada: {str(e)}")
    urls = []

# Realizar el análisis para cada URL
resultados = []
for url in urls:
    titulo, h1, h2, h3, meta = extraer_info(url)
    resultados.append({'URL': url, 'Título': titulo, 'H1': h1, 'H2': h2, 'H3': h3, 'Meta': meta})

# Crear DataFrame con los resultados
resultados_df = pd.DataFrame(resultados)

# Guardar los resultados en un nuevo archivo Excel
archivo_excel_salida = "resultados.xlsx"  # Nombre del archivo Excel de salida
try:
    resultados_df.to_excel(archivo_excel_salida, index=False)
    print(f"Los resultados se han guardado correctamente en {archivo_excel_salida}.")
except Exception as e:
    print(f"No se pudo guardar los resultados en el archivo Excel de salida: {str(e)}")
