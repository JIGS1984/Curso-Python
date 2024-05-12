#1. IMPORTAMOS LA LIBRERÍA BOKEH
import bokeh
from bokeh.plotting import figure, show

#2. CAPTURAMOS DATOS O LES CREAMOS (EL ORIGEN, DATAFRAMES, BBDD, TEXTO PLANO, TKINTER, ...)
x = [1, 2, 3, 4, 5]
y1 = [6, 7, 2, 4, 5]
y2 = [2, 3, 4, 5, 6]
y3 = [4, 5, 5, 7, 2]

#3. CREAMOS EL GRÁFICO
grafico = figure(title="MI PRIMER GRÁFICO", x_axis_label="x", y_axis_label="y")

#4. REPRESENTAMOS LOS VALORES CAPTURADOS
    #BARRAS VERTICALES O BLOQUES
grafico.vbar(x=x, top=y1, legend_label="BLOQUES", width=0.25, bottom=0, color="red")

    #LÍNEAS
grafico.line(x, y3, legend_label="LÍNEAS", color="blue", line_width=10)

    #CIRCULOS
grafico.scatter(x, y2, legend_label="CÍRCULOS", size=10, fill_color="black", fill_alpha=0.5, line_color="green")

#5. MANDAMOS EJECUTAR EL GRÁFICO
show(grafico)
