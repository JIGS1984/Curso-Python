import pyautogui as pa
import random

# Definir los límites del área de movimiento
x_min = 0
x_max = 300
y_min = 0
y_max = 300

#Hacemos el for 50 veces para mover el ratón
for _ in range(50):
    # Generar coordenadas aleatorias dentro del área delimitada
    x = random.randint(x_min, x_max)
    y = random.randint(y_min, y_max)
    
    # Mover el ratón a las coordenadas generadas
    pa.moveTo(x, y)
    input()
