import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
from datetime import datetime, timedelta
import os
from PIL import ImageTk, ImageColor, Image

# Función para cargar los datos de Excel y procesarlos
def cargar_datos():
    try:
        # Cambia 'datos.xlsx' al nombre de tu archivo Excel
        df = pd.read_excel('datos.xlsx', parse_dates=['Fecha'])
        return df
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar los datos: {str(e)}")

# Función para graficar la evolución de la velocidad del viento en Peña Trevinca
def graficar_peña_trevinca(df):
    try:
        # Filtrar datos para Peña Trevinca
        df_peña_trevinca = df[['Fecha', 'Peña Trevinca']]

        # Crear el gráfico con Seaborn
        sns.set_theme(style="darkgrid")
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=df_peña_trevinca, x='Fecha', y='Peña Trevinca', marker='o')
        plt.title("Evolución de la velocidad del viento en Peña Trevinca")
        plt.xlabel("Fecha")
        plt.ylabel("Velocidad del viento (km/h)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo graficar los datos de Peña Trevinca: {str(e)}")

# Función para graficar la evolución de la velocidad del viento en Pico Curavacas
def graficar_pico_curavacas(df):
    try:
        # Filtrar datos para Pico Curavacas
        df_pico_curavacas = df[['Fecha', 'Pico Curavacas']]

        # Crear el gráfico con Seaborn
        sns.set_theme(style="darkgrid")
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=df_pico_curavacas, x='Fecha', y='Pico Curavacas', marker='o')
        plt.title("Evolución de la velocidad del viento en Pico Curavacas")
        plt.xlabel("Fecha")
        plt.ylabel("Velocidad del viento (km/h)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo graficar los datos de Pico Curavacas: {str(e)}")

# Función para mostrar la ventana Seaborn de Peña Trevinca
def mostrar_ventana_trevinca():
    df = cargar_datos()
    if df is not None:
        graficar_peña_trevinca(df)

# Función para mostrar la ventana Seaborn de Pico Curavacas
def mostrar_ventana_curavacas():
    df = cargar_datos()
    if df is not None:
        graficar_pico_curavacas(df)

# Función principal
def main():
    # Crear la ventana principal de Tkinter
    ventana = tk.Tk()
    ventana.title("Evolución de la velocidad del viento")
    ventana.geometry("500x300")

    # Cargar la imagen de fondo
    imagen_fondo = Image.open("imagen.jpg")
    imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

    # Mostrar la imagen de fondo en un widget Label
    lbl_fondo = tk.Label(ventana, image=imagen_fondo)
    lbl_fondo.place(x=0, y=0, relwidth=1, relheight=1)

    # Configurar para que la imagen se mantenga visible
    lbl_fondo.image = imagen_fondo

    # Botones
    btn_trevinca = tk.Button(ventana, text="Peña Trevinca", command=mostrar_ventana_trevinca)
    btn_trevinca.pack(pady=10)

    btn_curavacas = tk.Button(ventana, text="Pico Curavacas", command=mostrar_ventana_curavacas)
    btn_curavacas.pack(pady=10)

    btn_salir = tk.Button(ventana, text="Salir", command=ventana.destroy)
    btn_salir.pack(pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    main()


