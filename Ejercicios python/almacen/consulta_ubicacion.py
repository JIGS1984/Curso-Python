import tkinter as tk
from tkinter import messagebox
import sqlite3

def buscar_producto_por_ubicacion():
    pasillo = pasillo_entry.get()
    estante = estante_entry.get()
    altura = altura_entry.get()

    try:
        # Conexión a la base de datos
        conexion = sqlite3.connect("almacen.db")
        cursor = conexion.cursor()

        # Buscar el producto por ubicación
        cursor.execute("SELECT codigo, descripcion FROM productos WHERE ubicacion_pasillo = ? AND ubicacion_estante = ? AND ubicacion_altura = ?", (pasillo, estante, altura))
        producto = cursor.fetchone()

        conexion.close()

        if producto:
            messagebox.showinfo("Producto Encontrado", f"Código: {producto[0]}\nDescripción: {producto[1]}")
        else:
            messagebox.showinfo("Producto No Encontrado", "No se encontró ningún producto en esa ubicación.")
    except sqlite3.Error as error:
        messagebox.showerror("Error", f"Error al buscar producto por ubicación: {error}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Consulta de Producto por Ubicación")
ventana.geometry("300x300")

# Crear caja de texto para el pasillo
pasillo_label = tk.Label(ventana, text="Pasillo:")
pasillo_label.pack(pady=5)
pasillo_entry = tk.Entry(ventana)
pasillo_entry.pack(pady=5)

# Crear caja de texto para el estante
estante_label = tk.Label(ventana, text="Estante:")
estante_label.pack(pady=5)
estante_entry = tk.Entry(ventana)
estante_entry.pack(pady=5)

# Crear caja de texto para la altura
altura_label = tk.Label(ventana, text="Altura:")
altura_label.pack(pady=5)
altura_entry = tk.Entry(ventana)
altura_entry.pack(pady=5)

# Botón para buscar producto por ubicación
buscar_btn = tk.Button(ventana, text="Buscar Producto", command=buscar_producto_por_ubicacion)
buscar_btn.pack(pady=10)

ventana.mainloop()
