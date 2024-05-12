#EJECUCIÓN SECUENCIAL PARA IMPRIMIR 100 VECES CADA COLOR POR LLAMADA A FUNCIÓN

#1. IMPORTAMOS LAS LIBRERÍAS NECESARIAS
from datetime import datetime
import time

#2. CREO UNA BIBLIOTECA DE COLORES
verde = (0,255,0)
amarillo = (255,255,0)
azul = (0,0,255)
magenta = (255,0,255)
gris = (128,128,128)
blanco = (255,255,255)
rojo = (255,0,0)

#3. FUNCIÓN QUE IMPRIME LA HORA DEL COLOR QUE SE LE PIDA 100 VECES
def imprimirhora(color):
    for n in range(100):
        hora = datetime.now().strftime("%H:%M:%S.%f")
        print(f'{color}#{n}: {hora}')
        time.sleep(0.1)

#4. PRINCIPAL
tinicio = datetime.now()
imprimirhora(verde)
imprimirhora(amarillo)
imprimirhora(azul)
imprimirhora(magenta)
imprimirhora(gris)
imprimirhora(blanco)
imprimirhora(rojo)
print()
print(f'Finalizado en {(datetime.now() - tinicio).total_seconds()} segundos')

