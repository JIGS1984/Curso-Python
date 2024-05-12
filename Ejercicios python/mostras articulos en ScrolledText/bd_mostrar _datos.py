from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import sqlite3
conexion=sqlite3.connect("articulos.db")
print("Base de datos abierta")
cur=conexion.cursor()
print("Cursor cerrado...")

def listar():
    ordenconsulta="SELECT * FROM articulos"
    cur.execute(ordenconsulta)
    return cur.fetchall()




ventana1=Tk()
ventana1.title("Listado de articulos")
ventana1.geometry("570x800+250+200")
#ventana1.resizable(False,False)
ventana1.attributes('-topmost', True)
frame1=Frame(ventana1,bg="linen")
frame1.grid(column=0,row=0,padx=5,pady=10)

titulo=LabelFrame(frame1,bg="linen",text="Listado")
titulo.grid(column=0,row=1,padx=5,pady=10)
etiqueta1=Label(titulo,text="Los articulos registrados son:")
etiqueta1.grid(column=0,row=2,padx=5,pady=10)

listatexto1=st.ScrolledText(titulo,width=60,height=40)
listatexto1.grid(column=0,row=3,padx=5,pady=10)

respuesta=listar()
listatexto1.delete("1.0",END)

for fila in respuesta:
    listatexto1.insert(END,"ID: " +str(fila[0])+"\nDescripcion "+str(fila[1])+"\nPrecio:"+str(fila[2])+"\n\n")




boton1=Button(titulo,text="Salir",command=ventana1.destroy)
boton1.grid(column=1,row=4,padx=5,pady=10)
ventana1.mainloop()

conexion.close()
print("BBDD CERRADA")
