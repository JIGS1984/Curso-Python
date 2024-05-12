class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        area = self.base * self.altura
        print("El área del rectángulo es:", area)

    def calcular_perimetro(self):
        perimetro = 2 * (self.base + self.altura)
        print("El perímetro del rectángulo es:", perimetro,"\nFin")



base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

rectangulo = Rectangulo(base, altura)
rectangulo.calcular_area()
rectangulo.calcular_perimetro()
