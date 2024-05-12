#1. IMPORTAMOS LIBRERÍAS NECESARIAS
#1A. INSTALARLAS VÍA CMD Y PIP SI FUERA NECESARIO
import keyboard
import pyautogui as pa
import random

#1B. DESACTIVAMOS LA SEGURIDAD DE LA LIBRERÍA AUTOGUI
pa.FAILSAFE=False

#2. LA FUNCIÓN PA.SIZE FACILITA EL TAMAÑO DE PANTALLA
print (pa.size())

#3. LA FUNCIÓN PA.POSITION INFORMA SOBRE LA POSICIÓN ACTUAL DEL PUNTERO DE RATÓN.
print (pa.position())

#4. LA FUNCIÓN KEYBOARD.IS_PRESSED('q') DETECTA LA PULSACIÓN DE UNA TECLA DADA
while True:
    pa.moveTo(x=random.randint(100,500), y=random.randint(100,500))
    if keyboard.is_pressed('q'):
        break

