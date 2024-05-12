#ejercicio bucle
import random
lista=[]
i=0
for i in range(0,10):
    lista.append(random.randint(0,100))
    i=i+1
print("Esta es la lista con los 10 valores aleatorios",lista)
lista.reverse()
print("Esta es la lista con los 10 valores invertidos",lista)
