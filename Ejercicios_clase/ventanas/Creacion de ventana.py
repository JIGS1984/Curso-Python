from tkinter import *
from tkinter import ttk
listaprovincias = ["Murcia","Galicia","Cataluña","Valencia","Andalucia"]
#crea una ventana
ventana= Tk()
ventana2= Tk()
ventana.title("Mi primrera ventana")
ventana2.title("Mi segunda ventana")

#LAS MEDIDA VAN EN PIXELES(ANCHO x ALTO + posicion eje X + posicion eje Y)
ventana.geometry("500x500+0+0")
ventana2.geometry("500x500+0+0")

#COLOR DE FONDO
ventana.configure(bg="linen")
ventana2.configure(bg="blue")

#Transparencia y opacidad

ventana.attributes("-alpha",1)

#Traer al frente una ventana entre varias
#ventana2.transient("ventana")

#ocultar una ventana 
ventana.withdraw()

#permiten minimizar (con presencia en barra de tareas) y mostrar ventanas en pantalla
ventana2.iconify()
ventana.deiconify()

#maxsize y minisiza definen tamaño maximo y minimo de pantalla
ventana.maxsize(1080,1080)
ventana.minsize(300,150)

#no permite redimensionar la ventana
ventana.resizable(True,True)

#Un frame es una caja/contenedor donde situar widgets

frame1 = Frame(ventana)
frame1.configure(width=350,height=350,bg="red",bd=5)
frame1.config(relief="flat")
#frame1.config(relief="sunken")
#frame1.config(relief="raised")
#frame1.config(relief="groove")
#frame1.config(relief="ridge")

frame2 = Frame(ventana)
frame2.configure(width=350,height=350,bg="blue",bd=500)
frame1.pack()
frame2.pack()
#widgets

#etiquetas
etiqueta=Label(frame1,text="Introduzca su Nombre",bg="green",fg="yellow",font=("Courier",24),anchor="center")
etiqueta.pack()

#entry(cajas de textgo)
cajadetexto = Entry(frame1,width=10,state="normal") #,textvariable(varA))
cajadetexto.pack()

#BOTONES
boton=Button(frame1,text="Aceptar",command=ventana.destroy,bg="white")
boton.pack()

#Lista desplegables
listadesplegable = Listbox(frame1)
listadesplegable.insert(0,"Galicia")
listadesplegable.insert(1,"Murcia")
listadesplegable.insert(2,"Valencia")
listadesplegable.insert(3,"Madrid")
listadesplegable.insert(4,"Barcelona")
listadesplegable.insert(5,"Sevilla")

listadesplegable2 = Listbox(frame1)
listadesplegable2.insert(0,*listaprovincias)

listadesplegable.pack()
listadesplegable2.pack()

etiqueta2=Label(frame1,text=listadesplegable.get(3),bg="green",fg="yellow",font=("Courier",24),anchor="center")
etiqueta2.pack()
listadesplegable.delete(3)
etiqueta3=Label(frame1,text=listadesplegable.get(3),bg="green",fg="yellow",font=("Courier",24),anchor="center")
etiqueta3.pack()

#boton check (checkbutton)
botondecheck = Checkbutton(frame1,text="Opcion 1")
botondecheck.invoke()
botondecheck.pack()

#radiosbuttons
opcion = IntVar()
botondeselecion  = Radiobutton(frame1,text="Opcion 1",variable=opcion,value=1)
botondeselecion2 = Radiobutton(frame1,text="Opcion 2",variable=opcion,value=2)
botondeselecion3 = Radiobutton(frame1,text="Opcion 3",variable=opcion,value=3)
botondeselecion4 = Radiobutton(frame1,text="Opcion 4",variable=opcion,value=4)
botondeselecion5 = Radiobutton(frame1,text="Opcion 5",variable=opcion,value=5)

botondeselecion.pack()
botondeselecion2.pack()
botondeselecion3.pack()
botondeselecion4.pack()
botondeselecion5.pack()


ventana2.mainloop()
ventana.mainloop()




#formulario = ttk.Frame(ventana)
#formulario.grid()



#etiquetas de una ventana (label)
#ttk.Label(ventana,text="Hola, mundo1.").grid(column=0,row=0)
#ttk.Label(ventana,text="Hola, mundo2.").grid(column=1,row=0)

#boton siempre llevan asociado un comando a ejecutar
#ttk.Button(ventana,text="Cerrar",command=ventana.destroy).grid(column=1,row=1)

#Caja de texto
#ttk.Entry().grid(column=1,row=2)
