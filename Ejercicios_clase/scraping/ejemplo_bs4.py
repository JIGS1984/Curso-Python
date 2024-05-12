#1. IMPORTAMOS LAS LIBRERÍAS NECESARIAS
import bs4
from bs4 import BeautifulSoup
import requests
import lxml

#2. COMENZAMOS A REALIZAR UN ANÁLISIS WEB
    #MARCAMOS EL DESTINO DEL ANÁLISIS
destino = requests.get('https://www.carrefour.es/electrodomesticos/climatizacion/calor-textil/cat7210002/c')
destino2 = requests.get('https://www.carrefour.es/cuidado-personal-y-salud/estetica-masaje/manicura-y-pedicura/cat4274477/c')
sopa = BeautifulSoup(destino.text, 'lxml')
sopa2 = BeautifulSoup(destino2.text, 'lxml')
    #EJECUTAMOS EL ANÁLISIS 1
    #OBTENER EL TÍTULO DE LA WEB ANALIZADA
titulo = sopa.title
print(titulo)
print()
    #OBTENER EL FORMATO DE ESCRITURA
escritura = sopa.meta
print(escritura)
print()
    #OBTENER LOS LINKS QUE CONTIENE LA WEB ANALIZADA
enlaces = sopa.links
print(enlaces)
print()
    #OBTENER COMEHTARIOS
comentarios = sopa.comment
print(comentarios)
print()

#3. PARA HACER BÚSQUEDAS CONCRETAS
busqueda1 = sopa.find('img')
print(busqueda1)
print()

busqueda2 = sopa.find('h1')
print(busqueda2)
print()

busqueda3 = sopa.find('h2')
print(busqueda3)
print()

busqueda4 = sopa.find('h3')
print(busqueda4)
print()

busqueda5 = sopa.find('h4')
print(busqueda5)
print()

busqueda6 = sopa.find('h5')
print(busqueda6)
print()

busqueda7 = sopa.find('h6')
print(busqueda7)
print()

    #EJECUTAMOS EL ANÁLISIS 2
    #OBTENER EL TÍTULO DE LA WEB ANALIZADA
titulo2 = sopa2.title
print(titulo2)
print()
    #OBTENER EL FORMATO DE ESCRITURA
escritura2 = sopa2.meta
print(escritura2)
print()
    #OBTENER LOS LINKS QUE CONTIENE LA WEB ANALIZADA
enlaces2 = sopa2.links
print(enlaces2)
print()
    #OBTENER COMEHTARIOS
comentarios2 = sopa2.comment
print(comentarios2)
print()

#3. PARA HACER BÚSQUEDAS CONCRETAS
busqueda11 = sopa2.find('img')
print(busqueda11)
print()

busqueda22 = sopa2.find('h1')
print(busqueda22)
print()

busqueda32 = sopa2.find('h2')
print(busqueda32)
print()

busqueda42 = sopa2.find('h3')
print(busqueda42)
print()

busqueda52 = sopa2.find('h4')
print(busqueda52)
print()

busqueda62 = sopa2.find('h5')
print(busqueda62)
print()

busqueda72 = sopa2.find('h6')
print(busqueda72)
print()
