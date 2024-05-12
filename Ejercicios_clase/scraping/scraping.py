
#1.Importamos librerías
import bs4
from bs4 import BeautifulSoup
import requests
import lxml

#2. Comenzamos a realizar un análisis web
destino=requests.get('http://www.marca.com')
sopa=BeautifulSoup(destino.text,'lxml')
    #ejecutamos el análisis
    #obtener el título de la web analizada
titulo=sopa.title
print(titulo)
print()
    #Obtener el formato de escritura
escritura=sopa.meta
print(escritura)
print()
    #Obtener los links que contiene la web analizada
enlaces=sopa.links
print (enlaces)
print()
    #Obtener comentarios
comentarios=sopa.comment
print(comentarios)
print()
    #obtener busquedas concretas
busqueda=sopa.find ('img')
print(busqueda)
print()

busqueda=sopa.find ('h1')
print(busqueda)
print()

busqueda=sopa.find ('h2')
print(busqueda)
print()

busqueda=sopa.find ('h3')
print(busqueda)
print()

busqueda=sopa.find ('h4')
print(busqueda)
print()

busqueda=sopa.find ('h5')
print(busqueda)
print()

busqueda=sopa.find ('h6')
print(busqueda)
print()
