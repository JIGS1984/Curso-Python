#1. IMPORTAR LIBRERÍA LOGGING
import logging
import numpy as np

#2. CREAMOS EL LOGGER
logging.basicConfig(
    format = '%(asctime)-5s %(name)-15s %(levelname)-8s %(message)s',
    level = logging.INFO,
    #LE DOY DESTINO AL ARCHIVO QUE CREO PARA ALMACENAR LOS REGISTROS
    filename = "D:\logs\infolog.log",
    filemode = "a"
)

logging.info('INICIO DE EJECUCIÓN DEL SCRIPT')
numeros = np.random.rand(1,100)
logging.info('ORDEN DE CREACIÓN DE ALEATORIOS EJECUTADA')
suma = numeros.sum()
logging.info('ORDEN DE SUMA DE ALEATORIOS EJECUTADA')
logging.info('FIN DE EJECUCIÓN DEL SCRIPT')
logging.shutdown()
