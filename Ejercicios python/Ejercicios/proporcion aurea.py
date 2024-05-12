import math
import tkinter as tk

# Función para calcular las medidas ideales para un vehículo SUV de tres segmentos
def calcular_medidas_suv():
    anchura_base = float(anchura_entry.get())
    altura_base = float(altura_entry.get())
    longitud_base = float(longitud_entry.get())

    # Calcula las medidas para el segmento SUV pequeño
    anchura_pequeno = anchura_base
    altura_pequeno = altura_base
    longitud_pequeno = longitud_base

    # Calcula las medidas para el segmento SUV mediano
    factor_mediano = 1.618  # Proporción áurea
    anchura_mediano = anchura_base * factor_mediano
    altura_mediano = altura_base * factor_mediano
    longitud_mediano = longitud_base * factor_mediano

    # Calcula las medidas para el segmento SUV grande
    factor_grande = factor_mediano ** 2
    anchura_grande = anchura_base * factor_grande
    altura_grande = altura_base * factor_grande
    longitud_grande = longitud_base * factor_grande

    # Actualizar las etiquetas con los resultados para cada segmento
    medidas_pequeno_label.config(text=f"Pequeño: {anchura_pequeno} x {altura_pequeno} x {longitud_pequeno}")
    medidas_mediano_label.config(text=f"Mediano: {anchura_mediano} x {altura_mediano} x {longitud_mediano}")
    medidas_grande_label.config(text=f"Grande: {anchura_grande} x {altura_grande} x {longitud_grande}")

    # Calcular y mostrar la proporción áurea para cada segmento
    proporcion_aurea_pequeno = altura_pequeno / anchura_pequeno
    proporcion_aurea_mediano = altura_mediano / anchura_mediano
    proporcion_aurea_grande = altura_grande / anchura_grande

    proporcion_pequeno_label.config(text=f"Pequeño - Proporción Áurea: {proporcion_aurea_pequeno}")
    proporcion_mediano_label.config(text=f"Mediano - Proporción Áurea: {proporcion_aurea_mediano}")
    proporcion_grande_label.config(text=f"Grande - Proporción Áurea: {proporcion_aurea_grande}")

# Crear ventana
root = tk.Tk()
root.title("Calculadora de Medidas SUV")

# Crear y posicionar etiquetas y cajas de texto
tk.Label(root, text="Anchura (cm):").grid(row=0, column=0, padx=5, pady=5)
anchura_entry = tk.Entry(root)
anchura_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Altura (cm):").grid(row=1, column=0, padx=5, pady=5)
altura_entry = tk.Entry(root)
altura_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Longitud (cm):").grid(row=2, column=0, padx=5, pady=5)
longitud_entry = tk.Entry(root)
longitud_entry.grid(row=2, column=1, padx=5, pady=5)

# Botón para calcular medidas
calcular_button = tk.Button(root, text="Calcular Medidas", command=calcular_medidas_suv)
calcular_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Etiquetas para mostrar los resultados de cada segmento
medidas_pequeno_label = tk.Label(root, text="Pequeño: ")
medidas_pequeno_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

medidas_mediano_label = tk.Label(root, text="Mediano: ")
medidas_mediano_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

medidas_grande_label = tk.Label(root, text="Grande: ")
medidas_grande_label.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# Etiquetas para mostrar la proporción áurea de cada segmento
proporcion_pequeno_label = tk.Label(root, text="Pequeño - Proporción Áurea: ")
proporcion_pequeno_label.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

proporcion_mediano_label = tk.Label(root, text="Mediano - Proporción Áurea: ")
proporcion_mediano_label.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

proporcion_grande_label = tk.Label(root, text="Grande - Proporción Áurea: ")
proporcion_grande_label.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

# Ejecutar aplicación
root.mainloop()
