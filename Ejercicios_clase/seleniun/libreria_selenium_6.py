#1. IMPORTAMOS LAS LIBRERÍAS NECESARIAS
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
import pandas as pd

#2. CONFIGURAMOS LAS OPCIONES DE NEVAGACIÓN
opciones = webdriver.ChromeOptions()
opciones.add_argument('--start-maximized')
opciones.add_argument('--disable-extensions')

#3. INICIAMOS EL ANÁLISIS
navegador = '"C:\Program Files\Google\Chrome\Application\chrome.exe"'
ventanaaanalizar = webdriver.Chrome(navegador, chrome_options=opciones)
ventanaaanalizar.maximize_window()
time.sleep(1)

#4. NAVEGO COMO YO DETERMINE HACERLO
ventanaaanalizar.get = 'https://www.eltiempo.es/'
WebDriverWait(ventanaaanalizar, 5)\
    .until(EC.element_to_be_clickable(By.CSS_SELECTOR
                                      'xxxxxxxxxxxxxxxxxx.replace(' '.'.')))\
    .click()

WebDriverWait(ventanaaanalizar, 5)\
    .until(EC.element_to_be_clickable(By.CSS_SELECTOR
                                      'input#inputSearch')))\
    .send_keys('Madrid')

WebDriverWait(ventanaaanalizar, 5)\
    .until(EC.element_to_be_clickable(By.CSS_SELECTOR
                                      'i.icon_weather_s.icon.icon_local')))\
    .click()

WebDriverWait(ventanaaanalizar, 5)\
    .until(EC.element_to_be_clickable(By.XPATH
                                      'xxxxxxxxxxxxxxxxxxxxxxxxx')))\
    .click()

#5. ALMACENO RESULTADOS y LOS MUESTRO
texto_columnas = driver.find_element_by_xpath('xxxxxxxxxxxxxx')
texto_columnas = texto_columnas.text

tiempo_hoy = texto_columnas.split('Mañana')[0].split('\n')[1:-1]
print(tiempo_hoy)


horas = list()
temp = list()
v_viento = list()

for i in range(0, len(tiempo_hoy), 4):
    horas.append(tiempo_hoy[i])
    temp.append(tiempo_hoy[i+1])
    v_viento.append(tiempo_hoy[i+2])

df = pd.DataFrame('Horas': horas, 'Temperatura': temp, 'Velocidad del viento': v_viento)
print(df)
df.to_csv('tiempo_hoy.csv', index = False)

ventanaaanalizar.quit()


