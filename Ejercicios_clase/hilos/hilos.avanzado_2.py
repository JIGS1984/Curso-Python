#EJECUCIÓN POR HILOS PARA IMPRIMIR 100 VECES CADA COLOR

#1. IMPORTAMOS LAS LIBRERÍAS NECESARIAS
import threading
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
    idhiloactual = threading.current_thread()
    nombrehiloactual = threading.current_thread().name
    for n in range(100):
        numerohilos = threading.active_count()
        hora = datetime.now().strftime("%H:%M:%S.%f")
        print(f'{color}#{n}: A la hora {hora} se he ejecutado el {nombrehiloactual} con ID {idhiloactual}. Es el hilo {nombrehiloactual}\n')
        time.sleep(0.1)

#4. EJECUCIÓN PRINCIPAL
tinicio = datetime.now()
idhiloprincipal = threading.main_thread()
nombrehiloprincipal = threading.main_thread().name
numerohilos = threading.active_count()
print("ID del hilo principal: ", idhiloprincipal)
print("NOMBRE del hilo principal: ", nombrehiloprincipal)
print("Número de hilos activos: ", numerohilos)
input("Pulsa ENTER para empezar la ejecución: ")

hilo1 = threading.Thread(name="Hilo1", target=imprimirhora, args=(verde,))
hilo2 = threading.Thread(name="Hilo2", target=imprimirhora, args=(amarillo,))
hilo3 = threading.Thread(name="Hilo3", target=imprimirhora, args=(azul,))
hilo4 = threading.Thread(name="Hilo4", target=imprimirhora, args=(magenta,))
hilo5 = threading.Thread(name="Hilo5", target=imprimirhora, args=(gris,))
hilo6 = threading.Thread(name="Hilo6", target=imprimirhora, args=(blanco,))
hilo7 = threading.Thread(name="Hilo7", target=imprimirhora, args=(rojo,))

#LA FUNCIÓN START() NOS PERMITE INICIAR LA EJECUCIÓN DE UN HILO PREVIAMENTE CREADO.
hilo1.start()
hilo2.start()
hilo3.start()
hilo4.start()
hilo5.start()
hilo6.start()
hilo7.start()

#LA FUNCIÓN JOIN() "ENTIERRA" (BORRA DE REGISTRO) A UN HILO TRAS EJECUTARSE PARA LIBERAR RECURSOS (CPU Y RAM).
hilo1.join()
hilo2.join()
hilo3.join()
hilo4.join()
hilo5.join()
hilo6.join()
hilo7.join()

print()
print("Tras matar a todos los hilos con join(), los hilos activos que quedan son: ", threading.active_count())
print(f'Finalizado en {(datetime.now() - tinicio).total_seconds()} segundos')

