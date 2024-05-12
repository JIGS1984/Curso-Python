import pygame
import sys
from pygame.locals import *

# Inicialización de Pygame
pygame.init()

# Definición de colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
color1 = (199, 66, 37)
color2 = (97, 205, 53)
color3 = (13, 70, 113)

# Creación de la ventana
ventana = pygame.display.set_mode((800, 600))
ventana.fill(color3)

# Coordenadas y dimensiones del botón
boton_aceptar = pygame.Rect(100, 100, 150, 50)

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            # Verificar si se hizo clic dentro del botón
            if boton_aceptar.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

    # Dibujar el botón
    pygame.draw.rect(ventana, color1, boton_aceptar, 0)
    
    # Texto del botón
    font = pygame.font.Font(None, 36)
    texto = font.render("ACEPTAR", True, negro)
    text_rect = texto.get_rect(center=boton_aceptar.center)
    ventana.blit(texto, text_rect)

    pygame.display.flip()

        
                 
      
           
