import pygame
from pygame.locals import *
import sys
pygame.init()
ancho = 1000
alto = 618
x=0
framesporsegundo=108
velocidad = 54
posicionx =50
posiciony =200
ancho_mario = 40

ventanadejuegos = pygame.display.set_mode((ancho,alto))
pygame.display.set_caption("MARIO IN THE CITY")
icono=pygame.image.load('mario.png')
pygame.display.set_icon(icono)

fondo = pygame.image.load("city2.jpg")
ventanadejuegos.blit(fondo,(0,0))

quieto = pygame.image.load('mario.jpg')
caminaderecha=[pygame.image.load('mario.png'),
               pygame.image.load('mario.png'),
               pygame.image.load('mario.png'),
               pygame.image.load('mario.png'),
               pygame.image.load('mario.png')]

caminaizquierda=[pygame.image.load('mario.png'),
                 pygame.image.load('mario.png'),
                 pygame.image.load('mario.png'),
                 pygame.image.load('mario.png'),
                 pygame.image.load('mario.png'),
                 pygame.image.load('mario.png')]

salta=[pygame.image.load('mario.jpg'),
       pygame.image.load('mario.jpg')]

reloj= pygame.time.Clock()
izquierda=False
derecha=False
salto=False
cuentapasos=0
                 
def actualizarpantalla():
    global cuentapasos
    global x
    posicionrelativa = x % fondo.get_rect().width
    ventanadejuego.blit(fondo,(posicionrelativa-fondo.get_rect().width,0))
    if posicionrelativa < ancho:
        ventanadejuego.blit(fondo,(posicionrelativa,0))
        x-=10
        if cuentapasos +1 >=6:
            cuentapaos=0
        if izquierda:
            ventanadejuego.blit(caminaizquierda[cuentapasos // 1],(int(posicionx),int(posiciony)))
            cuentapasos +=1
        elif derecha:
            ventanadejuego.blit(caminaderecha[cuentapasos // 1],(int(posicionx),int(posiciony)))
            cuentapasos +=1
        elif salto + 1 >=2 :
            ventanadejuego.blit(salta[cuentapasos // 1],(int(posicionx),int(posiciony)))
            cuentapasos +=1
        else:
            ventanadejuego.blit(quieto[cuentapasos // 1],(int(posicionx),int(posiciony)))
    pygame.display.update()



ejecucion=True
while ejecucion:
    
    reloj.tick(54)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            ejecucion=False

    tecla=pygame.key.get_pressed()

    if tecla[pygame.K_LEFT]:
        izquierda=True
        derecha=False
    elif tecla[pygame.K_RIGHT]:
        izquierda=False
        derecha=True

    if tecla[pygame.KEYUP]:
        salto=True
    if tecla[pygame.KEYDOWN]:
        salto=False

actualizarpantalla()







    
