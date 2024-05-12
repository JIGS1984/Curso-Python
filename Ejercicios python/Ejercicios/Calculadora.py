#importamos librerias
from tkinter import *
from tkinter import ttk
#Se crea la ventana
calculadora = Tk()
calculadora.title("Calculadora")
#medidas de la pantalla
calculadora.geometry("500x800")
#color de fondo
calculadora.configure(bg="linen")
#no se permiten el redimensionamiento
calculadora.resizable(False,False)
