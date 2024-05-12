from tkinter import *
import sqlite3

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

# Crear ventana
ventana = Tk()
ventana.title("Menú del Restaurante")
ventana.geometry("400x400")
ventana.attributes('-topmost', True)

# Crear marco principal
marco_principal = Frame(ventana, relief=RIDGE, borderwidth=15)
#frame1.config(relief="flat")
#frame1.config(relief="flat")
#frame1.config(relief="sunken")
#frame1.config(relief="raised")
#frame1.config(relief="groove")
#frame1.config(relief="ridge")
marco_principal.pack(padx=10, pady=10, fill=BOTH, expand=True)

# Función para mostrar los platos en el marco
def mostrar_platos():
    primeros = cur.execute("SELECT nombre FROM primeros").fetchall()
    segundos = cur.execute("SELECT nombre FROM segundos").fetchall()
    postres = cur.execute("SELECT nombre  FROM postres").fetchall()

    # Etiqueta "Primeros" dentro del marco
    Label(marco_principal, text="Primeros:", font=("Arial", 12, "bold")).pack()

    # Mostrar platos de primeros dentro del marco
    for plato in primeros:
        Label(marco_principal, text=plato[0]).pack()

    # Etiqueta "Segundos" dentro del marco
    Label(marco_principal, text="\nSegundos:", font=("Arial", 12, "bold")).pack()

    # Mostrar platos de segundos dentro del marco
    for plato in segundos:
        Label(marco_principal, text=plato[0]).pack()

    # Etiqueta "Postres" dentro del marco
    Label(marco_principal, text="\nPostres:", font=("Arial", 12, "bold")).pack()

    # Mostrar platos de postres dentro del marco
    for plato in postres:
        Label(marco_principal, text=f"{plato[0]} ").pack()

# Etiqueta "Bar Don Costa" dentro del marco principal
Label(marco_principal, text="Bar Don Costa:", font=("Arial", 24, "bold"), fg="#006400").pack()

# Etiqueta "Menú del día" dentro del marco principal
Label(marco_principal, text="Menú del día:", font=("Arial", 16, "bold"), fg="#008000").pack()

# Llamar a la función para mostrar los platos dentro del marco principal
mostrar_platos()

# Etiqueta "12€ Menu (IVA inc)" dentro del marco principal
Label(marco_principal, text="12€ Menu (IVA inc)", font=("Arial", 12), fg="#008000", anchor="e").pack()

ventana.mainloop()

