import pygame
import pygame
import sys
from pygame.locals import *

# Inicialización de Pygame
pygame.init()

# Dimensiones de la ventana
ANCHO = 400
ALTO = 200

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)

# Crear la ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Reproductor de Música')

# Inicialización del mixer
pygame.mixer.init()

# Cargar la música
pygame.mixer.music.load('The Godfather Theme - Nino Rota.mp3')

# Funciones para controlar la música
def reproducir():
    pygame.mixer.music.play()

def detener():
    pygame.mixer.music.stop()

def pausar():
    pygame.mixer.music.pause()

def reanudar():
    pygame.mixer.music.unpause()

def fadeout():
    pygame.mixer.music.fadeout(2000)  # 2000 milisegundos de tiempo de fadeout

# Crear los botones
boton_play = pygame.Rect(50, 50, 100, 50)
boton_stop = pygame.Rect(170, 50, 100, 50)
boton_pause = pygame.Rect(50, 120, 100, 50)
boton_reanudar = pygame.Rect(170, 120, 100, 50)

# Bucle principal
while True:
    ventana.fill(blanco)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            # Verificar si se hizo clic en algún botón
            if boton_play.collidepoint(event.pos):
                reproducir()
            elif boton_stop.collidepoint(event.pos):
                detener()
            elif boton_pause.collidepoint(event.pos):
                pausar()
            elif boton_reanudar.collidepoint(event.pos):
                reanudar()
            elif boton_fadeout.collidepoint(event.pos):
                fadeout()

    # Dibujar los botones
    pygame.draw.rect(ventana, negro, boton_play)
    pygame.draw.rect(ventana, negro, boton_stop)
    pygame.draw.rect(ventana, negro, boton_pause)
    pygame.draw.rect(ventana, negro, boton_reanudar)

    # Texto en los botones
    font = pygame.font.Font(None, 36)
    texto_play = font.render("PLAY", True, blanco)
    texto_stop = font.render("STOP", True, blanco)
    texto_pause = font.render("PAUSE", True, blanco)
    texto_reanudar = font.render("REANUDAR", True, blanco)
    ventana.blit(texto_play, (boton_play.x + 20, boton_play.y + 15))
    ventana.blit(texto_stop, (boton_stop.x + 15, boton_stop.y + 15))
    ventana.blit(texto_pause, (boton_pause.x + 5, boton_pause.y + 15))
    ventana.blit(texto_reanudar, (boton_reanudar.x - 10, boton_reanudar.y + 15))

    pygame.display.flip()
