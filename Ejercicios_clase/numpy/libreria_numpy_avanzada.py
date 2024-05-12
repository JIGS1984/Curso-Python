#FUNCIONES AVANZADAS DE LA LIBRERÍA NUMPY

#1. IMPORTAMOS LA LIBRERÍA NUMPY
import numpy as np
import random

#2. CREAMOS DATOS FIJOS O CAPTURADOS (CONSOLA, TKINTER, PYGAME, TXTO PLANO O BBDDD)
contenido1 = [3213454654646,0,0,0,0,0,0,0,0]
contenido2 = [5,7,11,23,56], [3,7,23,15,21]
contenido3 = [[1,1,1], [5,5,5]], [[3,3,3], [7,7,7]], [[1,1,1], [5,5,5]], [[3,3,3], [7,7,7]]
contenido4 = [3, 5.124587, "fkkhgvhg", False, True]
contenido5 = []
#contenido5 = [[], []], [[], []]
contenido6 = ["Diego", "Raquel", "Julia"]

#3. LA FUNCIÓN NDIM()PERMITE CONOCER LAS DIMENSIONES DE UN ARRAY
a = np.array(contenido1)
print(a)
print("La dimensión del array contenido1 es: ", a.ndim)
print()

b = np.array(contenido2)
print(b)
print("La dimensión del array contenido2 es: ", b.ndim)
print()

c = np.array(contenido3)
print(c)
print("La dimensión del array contenido3 es: ", c.ndim)
print()

d = np.array(contenido5)
print(d)
print("La dimensión del array contenido5 es: ", d.ndim)
print()

#4. LA FUNCIÓN DTYPE() PERMITE CONOCER EL TIPO DE DATOS
print(a)
print("El tipo de datos del array contenido1 es: ", a.dtype)
print()

e = np.array(contenido4)
print(e)
print("El tipo de datos del array contenido1 es: ", e.dtype)
print()

f = np.array(contenido6)
print(f)
print("El tipo de datos del array contenido1 es: ", f.dtype)
print()

#5. LA FUNCIÓN SIZE() NOS INFORMA DEL NÚMERO DE ELEMENTOS QUE TIENE UN ARRAY.
print("El número de elementos de contenido2 es: ", b.size)
print("El número de elementos de contenido2 es: ", c.size)
print("El número de elementos de contenido2 es: ", e.size)


#6. LA FUNCIÓN RESHAPE(x,y) CONVIERTE FILAS EN COLUMNAS Y COLUMNAS EN FILAS. ES DECIR, LA TRANSPUESTA.
print(b)
g = b.reshape(5,2)
print(g)
print()

#7. PARA ACCEDER A UN CONTENIDO CONCRETO DE UN ARRAY (X[FILA,COLUMNA]). MUY UTILIZADO.
contenido7 = [9,100,2], [11,300,5], [1,500,8]
h = np.array(contenido7)
print(h)
print(h[1,2])
print()

#8. PARA EXTRAER UNA COLUMNA DE UNA MATRIZ. MUY UTILIZADO:
print(h[0:, 2])
print()


#9. PARA EXTRAER UNA FILA DE UNA MATRIZ. MUY UTILIZADO:
print(h[1, 0:])
print()
