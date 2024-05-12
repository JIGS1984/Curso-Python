#1. IMPORTAMOS LAS LIBRERÍAS NECESARIAS
import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#2. ELEGIMOS HERRAMIENTA Y VÍCTIMA
    #OBLIGO AL S.O. A ABRIR UNA WEB EN CHROME
ventana = webdriver.Chrome()
ventana.get("https://www.python.org/")
    #CLAÚSULAS DE SEGURIDAD (SI ENCUENTRA LA PLABARA CLAVE, CONTINÚA. SI NO, SALE DEL BUCLE)
    #NORMALMENTE NO SE UTILIZAN, YA QUE RESTAN TIEMPO (HAY QUE CONOCER SU EXISTENCIA ...)
assert "Python" in ventana.title
    #TENDREMOS EL ELEMENTO A MANEJAR PREVIAMENTE RECONICIDO COMO Q
busqueda1 = ventana.find_element(By.NAME, "q")
busqueda1.send_keys("MI PRIMER ATAQUE")
time.sleep(5)
busqueda1.clear()
time.sleep(5)
busqueda1.send_keys("SELENIUM")
    #MÉTODO 1 DE HACER CLIC (ES EL MÁS CONCRETO)
#busqueda1.send_keys(Keys.RETURN)
    #MÉTODO 2 DE HACER CLIC (A GUSTO DE CADA CUAL...)
busqueda2 = ventana.find_element(By.NAME, "submit")
busqueda2.click()

#3. CIERRO EL ATAQUE (CON QUIT() CIERRO LA VENTANA. CON CLOSE() CIERRO LA VENTANA Y BORRO LOGS DEL S.O.)
#ventana.close()
