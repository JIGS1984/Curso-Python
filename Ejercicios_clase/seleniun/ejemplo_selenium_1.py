#1. IMPORTAMOS LAS LIBRERÍAS NECESARIAS
import selenium
from selenium import webdriver
import time

#2. SELENIUM TIENE PODER ABSOLUTO SOBRE TODOS LOS NAVEGADORES
ventana1 = webdriver.Chrome()
ventana1.get('https://www.seat.es/')

ventana2 = webdriver.Firefox()
ventana2.get('https://www.seat.es/')

ventana3 = webdriver.Edge()
ventana3.get('https://www.seat.es/')

#3. FUNCIONES DE LA LIBRERÍA SELENIUM
ventana4 = webdriver.Chrome()
ventana4.get('https://www.audi.es/es/web/es.html')
    #REFRESH OBLIGA A REALIZAR UNA ACTUALIZACIÓN DE CONTENIDO
time.sleep(5)
ventana4.refresh()
    #QUIT OBLIGA AL NAVEGADOR A CERRARSE
ventana1.quit()
ventana2.quit()
ventana3.quit()
ventana4.quit()
