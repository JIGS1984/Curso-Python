#1. IMPORTAMOS LAS LIBRERÍAS NECESARIAS
import numpy as np
import cv2
import matplotlib.pyplot as plt

#2. CARGAMOS LA IMAGEN
img = cv2.imread('person_of_interest.jpg')

#3. FUNCIONES BÁSICAS
    #MOSTRAR UNA IMAGEN
cv2.imshow('Imagen 1 (BASE)', img)
    #REDIMENSIONAR UNA IMAGEN
img_redimensionada = cv2.resize(img, (500, 500))
cv2.imshow('Imagen 2 (REDIMENSIONAMIENTO)',img_redimensionada)
    #SE QUEDA A LA ESPERA PARA CERRAR LA IMAGEN
img3 = cv2.resize(img_redimensionada, (250, 250))
cv2.imshow('Imagen 3 (REDIMENSIONAMIENTO Y ESPERA)',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
    #PERMITE ALMACENAR EL RESULTADO
cv2.imwrite('imagen4.jpg', img3)
    #PARA DARLE UN UMBRAL DE ENTRADA A LA IMAGEN (OSCURECER)
img4 = cv2.imread('person_of_interest.jpg', 0)
ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('IMAGEN UMBRAL', img4)
