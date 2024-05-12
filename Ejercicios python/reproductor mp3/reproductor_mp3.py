from tkinter import *
from tkinter import *
import os
import keyboard

def ejecutar_archivo():
    # Ruta al archivo facilitado en la tarea
    ruta_archivo = "djdsp_openset_rank1_7instead8_trancesession.mp3"
    
    # Verificar si el archivo existe
    if os.path.exists(ruta_archivo):
        # Ejecutar el archivo
        os.system(ruta_archivo)
    else:
        print("El archivo no existe")

def on_key_press(event):
    if event.name == "m":
        ejecutar_archivo()

# Crear la ventana
root = Tk()
root.title("Reproductor mp3")
root.geometry("400x200")
root.resizable(False, False)
root.configure(bg="lightblue")

# Crear un marco principal
frame = Frame(root, bg="lightblue")
frame.pack(expand=True)

# Crear un botón para ejecutar el archivo
button = Button(frame, text="Ejecutar Archivo", command=ejecutar_archivo, width=20, height=2)
button.grid(row=0, column=0, padx=10, pady=10)

# Crear un botón para salir
boton_salir = Button(frame, text="Salir", command=root.destroy, width=20, height=2)
boton_salir.grid(row=1, column=0, padx=10, pady=10)

# Asociar la pulsación de tecla "m" a la función ejecutar_archivo
keyboard.on_press(on_key_press)

# Ejecutar el bucle principal de la ventana
root.mainloop()
