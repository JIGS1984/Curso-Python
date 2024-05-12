#EJERCICIO FECHAS

#importo librerias
from datetime import date#esta para la fecha
from datetime import datetime#esta es para las horas

#creo la varialbles para la fecha actual y luego de esta elijo solo el año
#y lo guardo en año actual
fecha_actual=date.today()
año_actual=fecha_actual.year

#pido al usuario que introduzca su año de nacimiento y lo guardo en la variable
#año_nacimiento
año_nacimiento = int(input("Introduce tu año de nacimiento:"))

#imprimo por pantalla la resta del año actual y el año de nacimiento
print("Tu edad es ",año_actual-año_nacimiento)
