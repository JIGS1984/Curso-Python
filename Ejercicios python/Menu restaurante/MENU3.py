from tkinter import *
from tkinter import messagebox
import sqlite3
import os
# Función para agregar platos a la base de datos
def agregar_plato():
    tipo_plato = tipo_plato_var.get()
    nombre_plato = nombre_plato_entry.get()

    if nombre_plato.strip() == "":
        messagebox.showerror("Error", "Por favor ingrese un nombre de plato")
        return

    if tipo_plato == "Primeros":
        cur.execute("INSERT INTO primeros (nombre) VALUES (?)", (nombre_plato,))
    elif tipo_plato == "Segundos":
        cur.execute("INSERT INTO segundos (nombre) VALUES (?)", (nombre_plato,))
    elif tipo_plato == "Postres":
        cur.execute("INSERT INTO postres (nombre) VALUES (?)", (nombre_plato,))

    conexion.commit()
    messagebox.showinfo("Éxito", "Plato agregado exitosamente")

# Conexión a la base de datos
conexion = sqlite3.connect("restaurante.db")
cur = conexion.cursor()

# Crear tablas si no existen
try:
    cur.execute("CREATE TABLE IF NOT EXISTS primeros (id INTEGER PRIMARY KEY, nombre VARCHAR)")
    conexion.commit()
    print("Tabla de primeros creada...")
except sqlite3.Error as e:
    print("Error al crear tabla de primeros:", e)

try:
    cur.execute("CREATE TABLE IF NOT EXISTS segundos (id INTEGER PRIMARY KEY, nombre VARCHAR)")
    conexion.commit()
    print("Tabla de segundos creada...")
except sqlite3.Error as e:
    print("Error al crear tabla de segundos:", e)

try:
    cur.execute("CREATE TABLE IF NOT EXISTS postres (id INTEGER PRIMARY KEY, nombre VARCHAR)")
    conexion.commit()
    print("Tabla de postres creada...")
except sqlite3.Error as e:
    print("Error al crear tabla de postres:", e)
def abrirmenu():
    os.system('menu2.py')
# Insertar datos de ejemplo si las tablas están vacías
def insertar_datos_ejemplo():
    cur.execute("SELECT COUNT(*) FROM primeros")
    if cur.fetchone()[0] == 0:
        cur.execute("INSERT INTO primeros (nombre) VALUES ('Ensalada del tiempo'), ('Zumo de Tomate')")
        print("Datos de primeros insertados...")
    
    cur.execute("SELECT COUNT(*) FROM segundos")
    if cur.fetchone()[0] == 0:
        cur.execute("INSERT INTO segundos (nombre) VALUES ('Estofado de pescado'), ('Pollo con patatas')")
        print("Datos de segundos insertados...")
    
    cur.execute("SELECT COUNT(*) FROM postres")
    if cur.fetchone()[0] == 0:
        cur.execute("INSERT INTO postres (nombre) VALUES ('Flan con nata'), ('Fruta del tiempo')")
        print("Datos de postres insertados...")

    conexion.commit()

insertar_datos_ejemplo()

# Crear ventana principal
ventana = Tk()
ventana.title("Menú del Restaurante")
ventana.geometry("400x300")

# Crear y empaquetar marco principal
marco_principal = Frame(ventana, relief=RIDGE, borderwidth=15)
marco_principal.pack(padx=10, pady=10, fill=BOTH, expand=True)

# Etiqueta para seleccionar tipo de plato
Label(marco_principal, text="Tipo de Plato:").pack()

# ComboBox para seleccionar tipo de plato
tipo_plato_var = StringVar()
tipo_plato_var.set("Primeros")  # Valor predeterminado
tipo_plato_combo = OptionMenu(marco_principal, tipo_plato_var, "Primeros", "Segundos", "Postres")
tipo_plato_combo.pack()

# Etiqueta y entrada para el nombre del plato
Label(marco_principal, text="Nombre del Plato:").pack()
nombre_plato_entry = Entry(marco_principal)
nombre_plato_entry.pack()

# Botón para agregar el plato
Button(marco_principal, text="Agregar Plato", command=agregar_plato).pack()
boton=Button(marco_principal,text="MENU",command=abrirmenu)
boton.pack()
ventana.mainloop()

