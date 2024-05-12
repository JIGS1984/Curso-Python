import pygame
import datetime

# Inicializar Pygame
pygame.init()

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Definir dimensiones de la ventana
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

# Crear la ventana
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Cuenta Regresiva")

# Fuente para el texto
font = pygame.font.Font(None, 36)

# Obtener el tiempo actual
start_time = datetime.datetime.now()

# Bucle principal
running = True
while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calcular el tiempo restante
    current_time = datetime.datetime.now()
    time_elapsed = current_time - start_time
    time_left = max(20 - time_elapsed.seconds, 0)  # Limitar a 20 segundos

    # Limpiar la pantalla
    window.fill(WHITE)

    # Mostrar el tiempo restante en la ventana
    text = font.render(f"Tiempo restante: {time_left}", True, BLACK)
    text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
    window.blit(text, text_rect)

    # Actualizar la ventana
    pygame.display.flip()

    # Comprobar si el tiempo ha terminado
    if time_left == 0:
        # Reproducir un sonido al finalizar la cuenta regresiva
        pygame.mixer.init()
        pygame.mixer.music.load("sonido.mp3")  # Cambiar por el nombre de tu archivo de sonido
        pygame.mixer.music.play()

        # Esperar un momento para que se reproduzca el sonido
        pygame.time.wait(3000)  # 3 segundos

        # Salir del bucle
        running = False

    # Controlar la velocidad de la ejecución
    pygame.time.Clock().tick(30)

# Salir de Pygame
pygame.quit()
