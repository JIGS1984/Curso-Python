from tkinter import *
from tkinter import ttk
ventana = Tk ()
ventana.title("Calculadora de IVA")
ventana.geometry("500x500+800+20")
ventana.configure(bg="linen")

def calcular():
    try:
        precio_sin_iva = float(var_texto.get())
        precio_con_iva = precio_sin_iva +(precio_sin_iva*var_iva/100)
    except ValueError:
        var_lbl.set("Introduce un precio correcto")
       
    else: 
        var_lbl.set(f"El precio con el IVA es: {precio_con_iva:.2f}")


var_texto = StringVar()
var_lbl = StringVar()
var_lbl_iva= StringVar()
var_iva = 21

etiqueta = Label(ventana, textvariable=var_lbl,bg="green")
var_lbl.set("Precio sin IVA")
etiqueta.grid(row=0, column=1)

etiqueta_iva = Label(ventana, textvariable=var_lbl_iva,bg="green")
var_lbl_iva.set(f"El IVA ES:  {var_iva}")
etiqueta_iva.grid(row=0, column=2)

cajatexto = Entry(ventana, textvariable=var_texto)
cajatexto.grid(row=1, column=0, columnspan=2)

boton = Button(ventana, text="Calcular precio con IVA", bg="red",command=calcular)
boton.grid(row=1, column=2)
ventana.mainloop()
