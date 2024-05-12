import tkinter as tk
from tkinter import messagebox
import sqlite3
# Conexión a la base de datos
conexion = sqlite3.connect("almacen.db")
cursor = conexion.cursor()


try:
    cursor.execute("""
                CREATE TABLE productos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    codigo VARCHAR(50) NOT NULL,
                    descripcion VARCHAR(100) NOT NULL,
                    ubicacion_pasillo VARCHAR(50),
                    ubicacion_estante VARCHAR(50),
                    ubicacion_altura VARCHAR(50),
                    matricula VARCHAR(50) NOT NULL)""")
    print("Tabla articulos creada...")
     
except  sqlite3.OperationalError:
    print("La tabla ya existe")
           

def guardar_nuevo_articulo(codigo, descripcion, ubicacion_pasillo, ubicacion_estante, ubicacion_altura, matricula):
    try:
        # Insertar nuevo artículo en la tabla productos
        cursor.execute("INSERT INTO productos (codigo, descripcion, ubicacion_pasillo, ubicacion_estante, ubicacion_altura, matricula) VALUES (?, ?, ?, ?, ?, ?)", (codigo, descripcion, ubicacion_pasillo, ubicacion_estante, ubicacion_altura, matricula))

        # Confirmar la transacción y cerrar la conexión
        conexion.commit()
        conexion.close()

        messagebox.showinfo("Éxito", "Artículo guardado exitosamente.")
    except sqlite3.Error as error:
        messagebox.showerror("Error", f"Error al guardar el artículo: {error}")
 # Verificar si la tabla productos existe

        
        # Si la tabla no existe, crearla
        
def guardar_articulo():
    # Obtener los valores de las cajas de texto
    codigo = codigo_entry.get()
    descripcion = descripcion_entry.get()
    pasillo = pasillo_entry.get()
    estante = estante_entry.get()
    altura = altura_entry.get()
    matricula = matricula_entry.get()

    # Llamar a la función para guardar el artículo
    guardar_nuevo_articulo(codigo, descripcion, pasillo, estante, altura, matricula)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Alta de Artículo")

# Crear las etiquetas y cajas de texto para introducir los datos del artículo
tk.Label(ventana, text="Código:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
codigo_entry = tk.Entry(ventana)
codigo_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(ventana, text="Descripción:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
descripcion_entry = tk.Entry(ventana)
descripcion_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(ventana, text="Ubicación Pasillo:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
pasillo_entry = tk.Entry(ventana)
pasillo_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(ventana, text="Ubicación Estante:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
estante_entry = tk.Entry(ventana)
estante_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(ventana, text="Ubicación Altura:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
altura_entry = tk.Entry(ventana)
altura_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Label(ventana, text="Matrícula de Artículo:").grid(row=5, column=0, padx=10, pady=5, sticky="e")
matricula_entry = tk.Entry(ventana)
matricula_entry.grid(row=5, column=1, padx=10, pady=5)

# Botón para guardar el artículo
tk.Button(ventana, text="Guardar", command=guardar_articulo).grid(row=6, column=0, columnspan=2, pady=10)
tk.Button(ventana, text="Cerrar", command=ventana.destroy).grid(row=6, column=1, columnspan=2, pady=10)

ventana.mainloop()
