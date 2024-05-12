import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Funciones para interactuar con la base de datos
def conectar_bd():
    conn = sqlite3.connect('concesionario.db')

    c = conn.cursor()
    return conn, c

comerciales_data = conectar_bd()[1].execute("SELECT * FROM comerciales").fetchall()
def crear_tablas():
    conn, c = conectar_bd()
    c.execute('''CREATE TABLE IF NOT EXISTS comerciales (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    email TEXT NOT NULL)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS ventas (
                    id INTEGER PRIMARY KEY,
                    id_comercial INTEGER,
                    monto REAL,
                    FOREIGN KEY (id_comercial) REFERENCES comerciales(id))''')
    conn.commit()
    conn.close()

def registrar_comercial(nombre, email):
    conn, c = conectar_bd()
    c.execute("INSERT INTO comerciales (nombre, email) VALUES (?, ?)", (nombre, email))
    conn.commit()
    conn.close()

def registrar_venta(id_comercial, monto):
    conn, c = conectar_bd()
    c.execute("INSERT INTO ventas (id_comercial, monto) VALUES (?, ?)", (id_comercial, monto))
    conn.commit()
    conn.close()

def calcular_comision_anual(id_comercial):
    conn, c = conectar_bd()
    c.execute("SELECT monto FROM ventas WHERE id_comercial=?", (id_comercial,))
    ventas = c.fetchall()
    total_ventas = sum(venta[0] for venta in ventas)
    comision = total_ventas * 0.01
    conn.close()
    return comision

def obtener_ventas_comercial(id_comercial):
    conn, c = conectar_bd()
    c.execute("SELECT monto FROM ventas WHERE id_comercial=?", (id_comercial,))
    ventas = c.fetchall()
    conn.close()
    return ventas

# Funciones para las acciones de los botones
def registrar_comercial_accion():
    nombre = nombre_entry.get()
    email = email_entry.get()
    if nombre and email:
        registrar_comercial(nombre, email)
        messagebox.showinfo("Éxito", "Comercial registrado correctamente")
        # Recargar opciones del ComboBox de comerciales
        comerciales_data = conectar_bd()[1].execute("SELECT * FROM comerciales").fetchall()
        comerciales.clear()
        comerciales.extend(["Seleccione Comercial"] + [f"{row[0]} - {row[1]}" for row in comerciales_data])
        comercial_combobox['values'] = comerciales
    else:
        messagebox.showerror("Error", "Por favor, complete todos los campos")

def registrar_venta_accion():
    id_comercial = int(comercial_combobox.get().split()[0])
    monto = float(monto_entry.get())
    if monto:
        registrar_venta(id_comercial, monto)
        messagebox.showinfo("Éxito", "Venta registrada correctamente")
    else:
        messagebox.showerror("Error", "Por favor, ingrese el monto de la venta")

def calcular_comision_accion():
    id_comercial = int(comercial_combobox.get().split()[0])
    comision_anual = calcular_comision_anual(id_comercial)
    messagebox.showinfo("Comisión Anual", f"La comisión anual es: {comision_anual} €")

def mostrar_ventas_comercial_accion():
    id_comercial = int(comercial_combobox.get().split()[0])
    ventas = obtener_ventas_comercial(id_comercial)
    messagebox.showinfo("Ventas del Comercial", f"Ventas del Comercial:\n{ventas}")

# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Comisiones - Concesionario ADARSA S.L.")

# Crear y conectar a la base de datos
crear_tablas()

# Frame para registrar comerciales
frame_comercial = tk.Frame(root, padx=20, pady=20)
frame_comercial.grid(row=0, column=0)

tk.Label(frame_comercial, text="Nombre del Comercial:").grid(row=0, column=0)
nombre_entry = tk.Entry(frame_comercial)
nombre_entry.grid(row=0, column=1)

tk.Label(frame_comercial, text="Email del Comercial:").grid(row=1, column=0)
email_entry = tk.Entry(frame_comercial)
email_entry.grid(row=1, column=1)

registrar_comercial_btn = tk.Button(frame_comercial, text="Registrar Comercial", command=registrar_comercial_accion)
registrar_comercial_btn.grid(row=2, columnspan=2)

# Frame para registrar ventas
frame_venta = tk.Frame(root, padx=20, pady=20)
frame_venta.grid(row=0, column=1)
comerciales_data = conectar_bd()[1].execute("SELECT * FROM comerciales").fetchall()
tk.Label(frame_venta, text="Comercial:").grid(row=0, column=0)
comerciales = [("Seleccione Comercial",)]
comerciales = ["Seleccione Comercial"] + [f"{row[0]} - {row[1]}" for row in comerciales_data]
comercial_combobox = ttk.Combobox(frame_venta, values=comerciales)
comercial_combobox.grid(row=0, column=1)
    
tk.Label(frame_venta, text="Monto de la Venta:").grid(row=1, column=0)
monto_entry = tk.Entry(frame_venta)
monto_entry.grid(row=1, column=1)

registrar_venta_btn = tk.Button(frame_venta, text="Registrar Venta", command=registrar_venta_accion)
registrar_venta_btn.grid(row=2, columnspan=2)

# Frame para calcular comisión
frame_comision = tk.Frame(root, padx=20, pady=20)
frame_comision.grid(row=1, column=0, columnspan=2)

calcular_comision_btn = tk.Button(frame_comision, text="Calcular Comisión Anual", command=calcular_comision_accion)
calcular_comision_btn.pack()

# Frame para mostrar ventas
frame_ventas_comercial = tk.Frame(root, padx=20, pady=20)
frame_ventas_comercial.grid(row=2, column=0, columnspan=2)

mostrar_ventas_comercial_btn = tk.Button(frame_ventas_comercial, text="Mostrar Ventas del Comercial", command=mostrar_ventas_comercial_accion)
mostrar_ventas_comercial_btn.pack()

root.mainloop()
