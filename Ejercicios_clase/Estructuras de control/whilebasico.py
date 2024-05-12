#1. EJEMPLO DE BUCLE WHILE BÁSICO
import math
print("APLICACIÓN DE CONSOLA PARA CALCULAR RAICES CUADRADAS")
numero = int(input("Introduzca un número POSITIVO: "))

while numero <=0:
    print("ERROR. El número es NEGATIVO O CERO.")
    numero = int(input("Introduzca un número POSITIVO: "))
    
raiz=math.sqrt(numero)
print("La raiz cuadrada de",numero,"es",raiz)
