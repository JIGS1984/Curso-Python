import tkinter as tk
from tkinter import messagebox
import sqlite3

# Función para realizar la consulta de ubicación del producto
def consultar_ubicacion_producto():
    # Conectar a la base de datos
    conexion = sqlite3.connect("almacen.db")
    cursor = conexion.cursor()

    # Obtener el nombre del producto ingresado por el usuario
    nombre_producto = entry_nombre_producto.get()

    # Realizar la consulta a la base de datos
    cursor.execute("SELECT ubicacion_pasillo, ubicacion_estante, ubicacion_altura FROM productos WHERE descripcion = ?", (nombre_producto,))
    resultado = cursor.fetchone()

    # Cerrar la conexión a la base de datos
    conexion.close()

    # Verificar si se encontró el producto
    if resultado:
        ubicacion_pasillo, ubicacion_estante, ubicacion_altura = resultado
        mensaje = f"El producto '{nombre_producto}' se encuentra en el pasillo {ubicacion_pasillo}, estante {ubicacion_estante}, altura {ubicacion_altura}."
        messagebox.showinfo("Ubicación del Producto", mensaje)
    else:
        messagebox.showerror("Error", f"No se encontró el producto '{nombre_producto}'.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Consulta de Ubicación de Producto")

# Etiqueta y campo de entrada para el nombre del producto
tk.Label(ventana, text="Nombre del Producto:").pack()
entry_nombre_producto = tk.Entry(ventana)
entry_nombre_producto.pack()

# Botón para consultar la ubicación del producto
btn_consultar_ubicacion = tk.Button(ventana, text="Consultar Ubicación", command=consultar_ubicacion_producto)
btn_consultar_ubicacion.pack()

ventana.mainloop()
