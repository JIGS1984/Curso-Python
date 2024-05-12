import tkinter as tk
import os
# Funciones para los botones
def alta_articulos():
    os.system('alta_articulos.py')

def consulta_producto():
   os.system('consulta_producto.py')

def consulta_ubicacion():
    os.system('consulta_ubicacion.py')

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi Aplicación")
ventana.geometry("1920x1200")

# Crear un marco (frame)
marco_principal = tk.Frame(ventana, bg="lightgrey", bd=5)
marco_principal.place(relx=0.5, rely=0.5, anchor="center")

# Crear el título del marco
titulo_marco = tk.Label(marco_principal, text="Menú de Aplicación", font=("Arial", 24, "bold"), bg="lightgrey")
titulo_marco.pack(pady=20)

# Crear los botones
boton_alta_articulos = tk.Button(marco_principal, text="Alta de Artículos", font=("Arial", 16), command=alta_articulos)
boton_alta_articulos.pack(pady=10)

boton_consulta_producto = tk.Button(marco_principal, text="Consulta de Producto", font=("Arial", 16), command=consulta_producto)
boton_consulta_producto.pack(pady=10)

boton_consulta_ubicacion = tk.Button(marco_principal, text="Consulta de Ubicación", font=("Arial", 16), command=consulta_ubicacion)
boton_consulta_ubicacion.pack(pady=10)

ventana.mainloop()

