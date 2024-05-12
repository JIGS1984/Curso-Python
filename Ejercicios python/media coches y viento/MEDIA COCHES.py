from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource

# Datos en diccionarios
datos_espana = {
    "Año": [2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014],
    "Edad media": [14, 14, 13.5, 13.2, 12.9, 12.6, 12.3, 12, 11.7, 11.4],
}

datos_mundo = {
    "Año": [2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014],
    "Edad media": [12.3, 12.1, 11.9, 11.7, 11.5, 11.3, 11.1, 10.9, 10.7, 10.5],
}

# Fuente de datos de Bokeh
source_espana = ColumnDataSource(data=datos_espana)
source_mundo = ColumnDataSource(data=datos_mundo)

# Creación de la figura
grafico = figure(title="Evolución de la edad media de los vehículos", x_axis_label="Año", y_axis_label="Edad media (años)")

# Líneas para España y el mundo
grafico.line("Año", "Edad media", source=source_espana, legend_label="España", color="red")
grafico.line("Año", "Edad media", source=source_mundo, legend_label="Mundo", color="bLUE")

#grafico.vbar("Año", "Edad media", legend_label="Mundo", width=0.5, bottom=0, color="BLUE")
# Leyenda
grafico.legend.location = "top_left"
grafico.legend.title = "LEYENDA"
grafico.legend.label_text_font = "arial"
grafico.legend.label_text_font_style = "italic"
grafico.legend.label_text_color = "white"
grafico.legend.border_line_width = 2
grafico.legend.border_line_color = "red"
grafico.legend.border_line_alpha = 0.8
grafico.legend.background_fill_color = "red"
grafico.legend.background_fill_alpha = 0.2

# Mostrar la gráfica
show(grafico)

