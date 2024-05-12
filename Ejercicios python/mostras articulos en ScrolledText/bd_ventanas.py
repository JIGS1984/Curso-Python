from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import sqlite3
conexion = sqlite3.connect("articulos.db")
print("Base de datos creada o abierta...")
cur = conexion.cursor()
print("Cursor creado...")

try:
    cur.execute("CREATE TABLE articulos (id INTEGER PRIMARY KEY , descripcion VARCHAR ,precio FLOAT)")
    conexion.commit()
    print("Tabla articulos creada...")
except sqlite3.OperationalError:
    print("La tabla ya existe")
    

def agregar():
    datos = (varid.get(),vardescripcion.get(),varprecio.get())
    varid.set("")
    vardescripcion.set("")
    varprecio.set("")
    ordeninsercion = "INSERT INTO articulos(id,descripcion , precio) VALUES (?,?,?)"
    cur.execute(ordeninsercion,datos)
    conexion.commit()
    mb.showinfo("Información","Articulo registrado")


ventana1 = Tk()
ventana1.title("RESTAURANTE PACO")
ventana1.geometry("550x200+550+250",)
ventana1.attributes('-topmost', True)
ventana1.configure(bg="linen")

frame1 = Frame(ventana1)

frame1.grid(column=0,row=0,padx=10,pady=10)
titulo = LabelFrame(frame1,text="Alta de Articulo")
titulo.grid(column=0,row=1,padx=4,pady=4)

etiqueta1=Label(titulo,text="ID: ")
etiqueta1.grid(column=0,row=0,padx=4,pady=4)
varid=StringVar()
cajadetextoid=Entry(titulo,textvariable=varid)
cajadetextoid.grid(column=0,row=1,padx=4,pady=4)

etiqueta2=Label(titulo,text="Descripción: ")
etiqueta2.grid(column=1,row=0,padx=4,pady=4)
vardescripcion=StringVar()
cajadetextodescripcion=Entry(titulo,textvariable=vardescripcion)
cajadetextodescripcion.grid(column=1,row=1,padx=4,pady=4)



etiqueta3=Label(titulo,text="Precio: ")
etiqueta3.grid(column=2,row=0,padx=4,pady=4)
varprecio=StringVar()
cajadetextoprecio=Entry(titulo,textvariable=varprecio)
cajadetextoprecio.grid(column=2,row=1,padx=4,pady=4)

boton1=Button(titulo,text="Confirmar",command=agregar)
boton1.grid(column=3,row=1,padx=4,pady=4)
boton2=Button(titulo,text="Salir",command=ventana1.destroy)
boton2.grid(column=4,row=1,padx=4,pady=4)

ventana1.mainloop()
conexion.close()
print("Base de datos cerrada")
