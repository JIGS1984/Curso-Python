from tkinter import *
from tkinter import ttk
# Creamos una instancia de la ventana
ventana = Tk()

# Configuramos el tamaño de la ventana
ventana.geometry("600x600+250+250",)

# Configuramos el color de fondo de la ventana
ventana.configure(bg='#0A2342')  # Color azul oscuro en formato hexadecimal
ventana.lift()
# Configuramos el título de la ventana
ventana.title("Registro de Empleados")

# Funciones para los botones
def guardar_datos():
    # Obtenemos los datos de las cajas de texto
    codigo = cajadetexto_codigo.get()
    nombre = cajadetexto_nombre.get()
    apellido = cajadetexto_apellido.get()
    departamento = cajadetexto_departamento.get()
    
    # Escribimos los datos en un archivo de texto
    archivo = open("empleados.txt", "a") 
    archivo.write(f"Código: {codigo}, Nombre: {nombre}, Apellido: {apellido}, Departamento: {departamento}\n")
    archivo.close()
def borrar_datos():
    cajadetexto_codigo.delete(0, END)
    cajadetexto_nombre.delete(0, END)
    cajadetexto_apellido.delete(0, END)
    cajadetexto_departamento.delete(0, END)

def consultar_datos():
   
    codigo = cajadetexto_codigo.get()
    #Abrimos el archivo y buscamos el código del empleado
    #with open("empleados.txt", "r") as archivo:
    archivo = open("empleados.txt", "r") 
    
    for linea in archivo:
         if f"Código: {codigo}" in linea:
         # Encontramos el código, extraemos los datos y los mostramos en las cajas de texto
                datos = linea.split(", ")
                for dato in datos:
                    if "Nombre: " in dato:
                        nombre = dato.split(": ")[1]
                        cajadetexto_nombre.delete(0, END)
                        cajadetexto_nombre.insert(0, nombre)
                    elif "Apellido: " in dato:
                        apellido = dato.split(": ")[1]
                        cajadetexto_apellido.delete(0, END)
                        cajadetexto_apellido.insert(0, apellido)
                    elif "Departamento: " in dato:
                        departamento = dato.split(": ")[1]
                        cajadetexto_departamento.delete(0, END)
                        cajadetexto_departamento.insert(0, departamento)
    archivo.close()

            
etiqueta_introduzca_datos = Label(ventana, text="Introduzca datos y seleccione opción:", bg='#0A2342', fg='white',font=("Courier",12),anchor="center")
etiqueta_introduzca_datos.grid(row=0, column=2,padx=10, pady=10, sticky="nw")
cajadetexto = Entry(ventana,width=10,state="normal")



etiqueta_codigo_empleado = Label(ventana, text="Código Empleado:", font=("Courier",12),anchor="center")
etiqueta_codigo_empleado.grid(row=2, column=2,padx=10, pady=10, sticky="nw")
cajadetexto_codigo = Entry(ventana,width=30,state="normal")
cajadetexto_codigo.grid(row=2, column=3,padx=10, pady=10, sticky="nw")

etiqueta_nombre_empleado = Label(ventana, text="Nombre empleado:",font=("Courier",12),anchor="center")
etiqueta_nombre_empleado.grid(row=4, column=2,padx=10, pady=10, sticky="nw")
cajadetexto_nombre = Entry(ventana,width=30,state="normal")
cajadetexto_nombre.grid(row=4, column=3,padx=10, pady=10, sticky="nw")

etiqueta_apellido_empleado = Label(ventana, text="Apellido empleado:", font=("Courier",12),anchor="center")
etiqueta_apellido_empleado.grid(row=6, column=2, padx=10, pady=10, sticky="nw")
cajadetexto_apellido = Entry(ventana,width=30,state="normal")
cajadetexto_apellido.grid(row=6, column=3,padx=10, pady=10, sticky="nw")

etiqueta_departamento = Label(ventana, text="Departamento:", font=("Courier",12),anchor="center")
etiqueta_departamento.grid(row=8, column=2, padx=10, pady=10, sticky="nw")
cajadetexto_departamento = Entry(ventana,width=30,state="normal")
cajadetexto_departamento.grid(row=8, column=3,padx=10, pady=10, sticky="nw")


boton_guardar = Button(ventana, text="Guardar", bg="white", command=guardar_datos)
boton_guardar.grid(row=12, column=2, padx=10, pady=10, sticky="nw")

boton_borrar = Button(ventana, text="Borrar", bg="white", command=borrar_datos)
boton_borrar.grid(row=12, column=3, padx=10, pady=10, sticky="nw")

boton_consultar = Button(ventana, text="Consultar", bg="white", command=consultar_datos)
boton_consultar.grid(row=14, column=2, padx=10, pady=10, sticky="nw")

boton_salir = Button(ventana, text="Salir", bg="white", command=ventana.destroy)
boton_salir.grid(row=14, column=3, padx=10, pady=10, sticky="nw")

# Mostramos la ventana
ventana.mainloop()
