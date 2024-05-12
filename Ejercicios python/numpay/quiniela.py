import pygame
import sys
import numpy as np
from pygame.locals import *

# Inicializar Pygame
pygame.init()

# Definir colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Configuración de la ventana
ANCHO_VENTANA = 400
ALTO_VENTANA = 200
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption('Pronósticos')

# Fuente para el texto
fuente = pygame.font.Font(None, 36)

# Lista para almacenar los pronósticos
pronosticos = []

# Función principal del programa
def main():
    while True:
        ventana.fill(BLANCO)
        
        # Dibujar texto para ingresar pronóstico
        texto_ingresar = fuente.render('Ingrese pronóstico (1, 2 o X):', True, NEGRO)
        rect_texto_ingresar = texto_ingresar.get_rect()
        rect_texto_ingresar.center = (ANCHO_VENTANA // 2, ALTO_VENTANA // 2 - 20)
        ventana.blit(texto_ingresar, rect_texto_ingresar)
        
        # Dibujar texto de la media
        if len(pronosticos) > 0:
            pronosticos_array = np.array(pronosticos)
            media = np.mean(pronosticos_array)
            texto_media = fuente.render(f'Media: {media:.2f}', True, NEGRO)
            rect_texto_media = texto_media.get_rect()
            rect_texto_media.center = (ANCHO_VENTANA // 2, ALTO_VENTANA // 2 + 20)
            ventana.blit(texto_media, rect_texto_media)
        
        # Actualizar la pantalla
        pygame.display.flip()
        
        # Manejar eventos
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_1:
                    pronosticos.append(1)
                elif event.key == K_2:
                    pronosticos.append(2)
                elif event.key == K_x:
                    pronosticos.append(0)
                elif event.key == K_RETURN:
                    print('Pronósticos:', pronosticos_array)
                    print('Media:', media)
                    pronosticos.clear()

if __name__ == '__main__':
    main()
