import tkinter as tk
from tkinter import messagebox
import time
import pygame
import datetime

# Función para calcular los días restantes hasta el próximo cumpleaños
def calcular_dias_restantes(fecha_nacimiento):
    hoy = datetime.date.today()
    cumpleaños_proximo = datetime.date(hoy.year, fecha_nacimiento.month, fecha_nacimiento.day)
    if cumpleaños_proximo < hoy:
        cumpleaños_proximo = datetime.date(hoy.year + 1, fecha_nacimiento.month, fecha_nacimiento.day)
    return (cumpleaños_proximo - hoy).days

# Función para obtener la fecha de nacimiento del usuario
# Función para obtener la fecha de nacimiento del usuario
def obtener_fecha_nacimiento():
    fecha = None
    while fecha is None:
        ventana = tk.Tk()
        ventana.title("Fecha de Nacimiento")

        label_dia = tk.Label(ventana, text="Día:")
        label_dia.grid(row=0, column=0)
        entry_dia = tk.Entry(ventana)
        entry_dia.grid(row=0, column=1)

        label_mes = tk.Label(ventana, text="Mes:")
        label_mes.grid(row=1, column=0)
        entry_mes = tk.Entry(ventana)
        entry_mes.grid(row=1, column=1)

        label_año = tk.Label(ventana, text="Año:")
        label_año.grid(row=2, column=0)
        entry_año = tk.Entry(ventana)
        entry_año.grid(row=2, column=1)

        def obtener_fecha():
            nonlocal fecha
            try:
                dia = int(entry_dia.get())
                mes = int(entry_mes.get())
                año = int(entry_año.get())
                fecha = datetime.date(año, mes, dia)
                ventana.destroy()
            except ValueError:
                messagebox.showerror("Error", "Por favor, introduce una fecha válida.")

        boton = tk.Button(ventana, text="Aceptar", command=obtener_fecha)
        boton.grid(row=3, columnspan=2)

        ventana.mainloop()

    return fecha


# Función principal
def main():
    # Ventana de captura de datos
    inicio = time.time()

    fecha_nacimiento = obtener_fecha_nacimiento()

    if fecha_nacimiento is not None:
        with open('fecha_nacimiento.txt', 'w') as file:
            file.write(fecha_nacimiento.strftime("%d/%m/%Y"))
    else:
         print("No se ha proporcionado una fecha de nacimiento válida.")

 
    tiempo_almacenamiento = time.time() - inicio

    # Cálculos y procesos internos
    dias_restantes = calcular_dias_restantes(fecha_nacimiento)
    tiempo_calculos = time.time() - inicio - tiempo_almacenamiento

    # Ventana de muestra de resultado
    pygame.init()
    pygame.font.init()

    ventana = pygame.display.set_mode((400, 200))
    pygame.display.set_caption("Días hasta tu cumpleaños")
    clock = pygame.time.Clock()

    font = pygame.font.SysFont(None, 50)

    final = time.time()
    tiempo_total = final - inicio

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ventana.fill((255, 255, 255))

        texto = font.render(str(dias_restantes), True, (0, 0, 0))
        ventana.blit(texto, (150, 75))

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

    print("Tiempo parcial ventana captura de datos:", tiempo_almacenamiento)
    print("Tiempo parcial almacenamiento:", tiempo_almacenamiento)
    print("Tiempo parcial cálculos y procesos internos:", tiempo_calculos)
    print("Tiempo parcial ventana de muestra de resultado:", tiempo_total - tiempo_almacenamiento - tiempo_calculos)
    print("Tiempo total:", tiempo_total)

if __name__ == "__main__":
    main()
