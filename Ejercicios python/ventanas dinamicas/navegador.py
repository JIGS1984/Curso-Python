import webbrowser
import time
import pygame
from pygame.locals import *

import sys
contador = 0
total = 5
webbrowser.open("https://www.toyota.es/")
time.sleep(10)
print("El programa se abrio por primera vez a las " + time.ctime())

pygame.init()
blanco=(255,255,255)
verde=(0,255,0)
azul=(0,0,255)
ventanapublicidad = pygame.display.set_mode((600,600))

ventanapublicidad.fill(verde)

font = pygame.font.Font(None, 36)
texto_publicidad = font.render("Publicidad", True, blanco)
ventanapublicidad.blit(texto_publicidad, (20,  15))
#6. BUCLE DE CIERRE Y ACTUALIZACIÓN
while True:
    for event in pygame.event.get():
        if event.type ==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
