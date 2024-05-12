#1. IMPORTAMOS LA LIBRERÍA PANDAS
import pandas as pd

import numpy as np

import random


#2. CREACIÓN O CAPTURA DE DATOS ...

datos1 = ([["", "Glucosa en sangre 08:00", "Glucosa en sangre 14:00"],
           ["Paciente 1", 110, 98],
           ["Paciente 2", 110, 91],
           ["Paciente 3", 87, 98]])
datos2 = ([[110, 72, 100],
           [130, 91, 58],
           [87, 98, 77]])

#SI LO TRATO COMO UN ARRAY (NUMPY)
a = np.array(datos1)
print(a)
print()

#SI LO TRATO COMO UNA TABLA DE DATOS (PANDAS)
b = pd.DataFrame(datos1)
print(b)
print()

#3. PARA CREAR UNA SERIE DE DATOS EN PANDAS
#EL EQUIVALENTE A VECTOR EN NUMPY ...
#NO MUY UTILIZADO
serie = pd.Series({"Propiedad 1":"120.000 €", "Propiedad 2":"135.000 €"})
print(serie)
print()

#4. PARA SABER LAS DIMENSIONES DE UNA MATRIZ EN PANDAS
print(b.shape)
print()

#5. LA FUNCIÓN LEN NOS DA LONGITUD DE LA TABLA:
print(len(b.index))
print()

#6. PARA AVERIGUAR LOS VALORES ESTADÍSTICOS TÍPICOS DE UNA VEZ:
c = b.describe()
print(c)
print()

#7. PARA AVERIGUAR LA MEDIA DE CADA COLUMNA
d = pd.DataFrame(datos2)
e = d.mean()
print(d)
print()
print(e)
print()

#8. PARA AVERIGUAR EL VALOR MÁXIMO DE UNA TABLA (DATAFRAME)
f = d.max()
print(f)
print

#9. PARA AVERIGUAR EL VALOR MÍNIMO DE UNA TABLA (DATAFRAME)
g = d.min()
print(g)
print

#10. PARA CALCULAR LA CORRELACIÓN DE UNA TABLA DE DATOS (DATAFRAME)
h = d.corr()
print(h)
print()

#11. PARA CALCULAR DESVIACIÓN ESTÁNDAR DE UN DATAFRAME
i = d.std()
print(i)
print()

#12. PARA EXTRAER UNA O VARIAS COLUMNAS
print(d)
print()
print(d[1])
print()
print(d[[0, 2]])
print()

#13. PARA EXTRAER UNA O VARIAS FILAS
print(d)
print()
print(d.loc[1])
print()
print(d.loc[[1,2]])
print()

#14. PARA EXTRAER UN DATO CONCRETO DE UN DATAFRAME
print(d)
print()
print(d.iloc[1][1])
print(d.iloc[2][1])
z = d.iloc[1][1]
y = d.iloc[2][1]
print()
print(z)
print(y)

lista = (z,y)
print(lista)

a1 = d.iloc[0][1]
print(a1)

print()

































