import random

# Genera un número aleatorio entre 1 y 10
numero_secreto = random.randint(1, 10)
numero_intentos = 0

print("¡Bienvenido al juego Adivina el Número!")
print("He pensado en un número entre 1 y 10. ¡Adivina cuál es!")
intento=0 
while intento != numero_secreto:
    
    intento = int(input("Introduce tu intento: "))
    numero_intentos  = numero_intentos  + 1

    if intento < numero_secreto:
            print("El número es mayor. ¡Sigue intentándolo!")
    elif intento > numero_secreto:
            print("El número es menor. ¡Sigue intentándolo!")
    else:
        print(f"¡Felicidades! Has adivinado el número en ",numero_intentos ,"intentos.")




