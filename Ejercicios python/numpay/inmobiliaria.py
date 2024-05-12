
import tkinter as tk

# Datos de los pisos
pisos = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'}, 
         {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'}, 
         {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'}, 
         {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'}, 
         {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'},
         {'año': 2014, 'metros': 80, 'habitaciones': 1, 'garaje': True, 'zona': 'C'},
         {'año': 2016, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'C'}]

# Función para calcular precios y buscar pisos según presupuesto
def busca_piso(pisos, presupuesto):
    TOLERANCIA = 10000  # Tolerancia de +/- 10000 en el presupuesto
    
    def añadir_precio(piso):
        precio = (piso['metros'] * 1000 + piso['habitaciones'] * 5000 + int(piso['garaje']) * 15000) * (1 - (2020 - piso['año']) / 100)
        if piso['zona'] == 'B':
            precio *= 1.5
        elif piso['zona'] == 'C':
            precio *= 1.8
        piso['precio'] = precio
        return piso
    
    def filtro(piso):
        return abs(piso['precio'] - presupuesto) <= TOLERANCIA
    
    return list(filter(filtro, map(añadir_precio, pisos)))

# Función para mostrar los resultados en una ventana Tkinter
def mostrar_resultados():
    presupuesto = int(entry_presupuesto.get())
    resultados = busca_piso(pisos, presupuesto)
    
    resultado_text.config(state=tk.NORMAL)
    resultado_text.delete('1.0', tk.END)
    
    if resultados:
        resultado_text.insert(tk.END, "Resultados:\n\n")
        for piso in resultados:
            resultado_text.insert(tk.END, f"Año: {piso['año']}, Metros: {piso['metros']}, Habitaciones: {piso['habitaciones']}, Garaje: {piso['garaje']}, Zona: {piso['zona']}, Precio: {piso['precio']}\n")
    else:
        resultado_text.insert(tk.END, "No se encontraron resultados aproximados al presupuesto dado.")
    
    resultado_text.config(state=tk.DISABLED)

# Crear ventana Tkinter
root = tk.Tk()
root.title("Búsqueda de Inmuebles")
root.configure(bg="black")
root.iconbitmap("casa.ico")  # Asignar el icono a la ventana
root.lift()  # Elevar la ventana a primer plano

# Crear y configurar elementos en la ventana
label_presupuesto = tk.Label(root, text="Presupuesto:", bg="black", fg="orange")
label_presupuesto.grid(row=0, column=0, padx=10, pady=10)

entry_presupuesto = tk.Entry(root, bg="black", fg="orange")
entry_presupuesto.grid(row=0, column=1, padx=10, pady=10)

buscar_button = tk.Button(root, text="Buscar", command=mostrar_resultados, bg="orange", fg="black")
buscar_button.grid(row=0, column=2, padx=10, pady=10)

resultado_text = tk.Text(root, wrap=tk.WORD, width=50, height=10, bg="black", fg="orange")
resultado_text.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
resultado_text.config(state=tk.DISABLED)

# Ejecutar la ventana
root.mainloop()
