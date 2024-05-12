import tkinter as tk
import numpy as np

def capturar_datos():
    # Capturar datos de las matrices desde las entradas de texto
    matriz1 = np.array([[int(entrada_matriz1[i][j].get()) for j in range(3)] for i in range(3)])
    matriz2 = np.array([[int(entrada_matriz2[i][j].get()) for j in range(3)] for i in range(3)])
    return matriz1, matriz2

def suma_matrices():
    matriz1, matriz2 = capturar_datos()
    resultado = matriz1 + matriz2
    mostrar_resultado(resultado)

def resta_matrices():
    matriz1, matriz2 = capturar_datos()
    resultado = matriz1 - matriz2
    mostrar_resultado(resultado)

def multiplicacion_matrices():
    matriz1, matriz2 = capturar_datos()
    resultado = np.dot(matriz1, matriz2)
    mostrar_resultado(resultado)

def division_matrices():
    matriz1, matriz2 = capturar_datos()
    resultado = np.divide(matriz1, matriz2, out=np.zeros_like(matriz1, dtype=float), where=matriz2!=0)
    mostrar_resultado(resultado)

def mostrar_resultado(resultado):
    # Crear una nueva ventana para mostrar el resultado
    ventana_resultado = tk.Toplevel(ventana)
    ventana_resultado.title("Resultado")

    # Crear un widget de etiqueta para mostrar el resultado
    etiqueta_resultado = tk.Label(ventana_resultado, text=str(resultado))
    etiqueta_resultado.pack()

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Operaciones con matrices")

# Crear matrices de entrada
entrada_matriz1 = [[tk.Entry(ventana, width=5) for _ in range(3)] for _ in range(3)]
entrada_matriz2 = [[tk.Entry(ventana, width=5) for _ in range(3)] for _ in range(3)]

# Posicionar matrices de entrada
for i in range(3):
    for j in range(3):
        entrada_matriz1[i][j].grid(row=i, column=j, padx=5, pady=5)
        entrada_matriz2[i][j].grid(row=i, column=j+4, padx=5, pady=5)

# Botones para realizar operaciones
btn_suma = tk.Button(ventana, text="Suma", command=suma_matrices)
btn_suma.grid(row=4, column=1)

btn_resta = tk.Button(ventana, text="Resta", command=resta_matrices)
btn_resta.grid(row=4, column=2)

btn_multiplicacion = tk.Button(ventana, text="Multiplicación", command=multiplicacion_matrices)
btn_multiplicacion.grid(row=4, column=3)

btn_division = tk.Button(ventana, text="División", command=division_matrices)
btn_division.grid(row=4, column=4)

ventana.mainloop()


