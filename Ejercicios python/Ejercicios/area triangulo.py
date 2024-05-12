#Definicion de la funcion
def area_triangulo(base,altura):
    
    area = (base * altura ) / 2
    return area

# Pedimos por consola los parametros de los lados del triángulo
base  = float(input("Indique la base: "))
altura  = float(input("Indique la altura: "))

# Calcular y mostrar el área del triángulo
print("El área del triángulo es:", area_triangulo(base,altura))
