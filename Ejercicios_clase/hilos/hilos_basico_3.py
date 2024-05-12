#1. IMPORTAMOS LAS LIBRERÍAS NECESARIAS 
import threading
import time
import datetime
import logging


#2. CREO 2 FUNCIONES Y LAS EJECUTO PARA VER CUANTO TARDA EN EJECUIÓN SIMPLE O SECUENCIAL. (TARDA 7 SEGUNDOS + X)
def consultar(id_persona):
    time.sleep(2)
    pass

def guardar(id_persona, data):
    time.sleep(5)
    pass

tiniciosec = datetime.datetime.now()

consultar(1)
guardar(1, "Hola, mundo de hilos...")

tejecucionsec = datetime.datetime.now() - tiniciosec
print(tejecucionsec)

#3. HAGO LO MISMO UTILIZANDO HILOS (APROVECHO MEJOR RECURSOS CPU Y RAM) (TARDA 5 SEGUNDS + X)
tinicioh = datetime.datetime.now()
hilo1 = threading.Thread(name="hilo1", target=consultar, args=(1, ))
hilo2 = threading.Thread(name="hilo2", target=guardar, args=(1, "Ejecución del Hilo 2..."))

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

tejecucionh = datetime.datetime.now() - tinicioh
print(tejecucionh)
