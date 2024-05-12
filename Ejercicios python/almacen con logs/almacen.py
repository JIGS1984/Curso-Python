import tkinter as tk
from tkinter import messagebox
import sqlite3
import logging

logging.basicConfig(
    format='%(asctime)-5s %(name)-15s %(levelname)-8s %(message)s',
    level=logging.INFO,
    filename="infolog.log",
    filemode="a"
)

def crear_base_datos():
    try:
        conexion = sqlite3.connect('almacen.db')
        cursor = conexion.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS articulos (
                            id INTEGER PRIMARY KEY,
                            nombre TEXT NOT NULL,
                            cantidad INTEGER NOT NULL,
                            descripcion TEXT
                          )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS precios (
                            id INTEGER PRIMARY KEY,
                            articulo_id INTEGER,
                            precio_con_iva REAL,
                            precio_sin_iva REAL,
                            precio_promo_con_iva REAL,
                            FOREIGN KEY(articulo_id) REFERENCES articulos(id)
                          )''')

        conexion.commit()
        logging.info("Base de datos creada correctamente.")
    except sqlite3.Error as error:
        logging.error("Error al crear la base de datos: %s", error)
    finally:
        if conexion:
            conexion.close()

crear_base_datos()

def insertar_registro():
    nombre = nombre_entry.get()
    cantidad = cantidad_entry.get()
    descripcion = descripcion_entry.get()
    precio_sin_iva = float(precio_sin_iva_entry.get())

    precio_con_iva = precio_sin_iva * 1.16
    precio_promo = precio_sin_iva * 0.8
    precio_promo_con_iva = precio_promo * 1.16

    try:
        conexion = sqlite3.connect('almacen.db')
        cursor = conexion.cursor()

        cursor.execute("INSERT INTO articulos (nombre, cantidad, descripcion) VALUES (?, ?, ?)",
                       (nombre, cantidad, descripcion))
        logging.info('Registro insertado en la tabla "articulos"')

        articulo_id = cursor.lastrowid

        cursor.execute("INSERT INTO precios (articulo_id, precio_con_iva, precio_sin_iva, precio_promo_con_iva) VALUES (?, ?, ?, ?)",
                       (articulo_id, precio_con_iva, precio_sin_iva, precio_promo_con_iva))
        logging.info('Registro insertado en la tabla "precios"')

        conexion.commit()
        messagebox.showinfo("Éxito", "Registro insertado correctamente.")
    except sqlite3.Error as error:
        messagebox.showerror("Error", f"No se pudo insertar el registro: {error}")
        logging.error("Error al insertar registro: %s", error)
    finally:
        if conexion:
            conexion.close()

app = tk.Tk()
app.title("Gestión de Almacén")

# Icono de la aplicación
app.iconbitmap("icono.ico")

# Colores personalizados
color_fondo = "#F0F0F0"
color_botones = "#4CAF50"
color_texto = "#333333"

# Configuración del estilo
app.configure(bg=color_fondo)

# Frame principal
frame_principal = tk.Frame(app, bg=color_fondo)
frame_principal.pack(padx=20, pady=20)

tk.Label(frame_principal, text="Nombre:", bg=color_fondo, fg=color_texto).grid(row=0, column=0, sticky="w", padx=10, pady=5)
nombre_entry = tk.Entry(frame_principal)
nombre_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame_principal, text="Cantidad:", bg=color_fondo, fg=color_texto).grid(row=1, column=0, sticky="w", padx=10, pady=5)
cantidad_entry = tk.Entry(frame_principal)
cantidad_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame_principal, text="Descripción:", bg=color_fondo, fg=color_texto).grid(row=2, column=0, sticky="w", padx=10, pady=5)
descripcion_entry = tk.Entry(frame_principal)
descripcion_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(frame_principal, text="Precio sin IVA:", bg=color_fondo, fg=color_texto).grid(row=3, column=0, sticky="w", padx=10, pady=5)
precio_sin_iva_entry = tk.Entry(frame_principal)
precio_sin_iva_entry.grid(row=3, column=1, padx=10, pady=5)

insertar_button = tk.Button(frame_principal, text="Insertar Registro", bg=color_botones, fg="white", command=insertar_registro)
insertar_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

app.mainloop()
