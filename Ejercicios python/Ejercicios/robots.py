class Robot:
    def __init__(self, color, altura, inteligencia):
        self.color = color
        self.altura = altura
        self.inteligencia = inteligencia
        self.activo = False

    def activar(self):
        self.activo = True
        print("El robot está ahora activo.")

    def pausar(self):
        self.activo = False
        print("El robot está ahora en pausa.")


class C3PO(Robot):
    def __init__(self):
        super().__init__(color="Dorado", altura="Alto", inteligencia="Menos inteligente")
        self.piernas = True

    def caracteristicas_especificas(self):
        print("Características específicas de C3PO:")
        print("- Color:", self.color)
        print("- Altura:", self.altura)
        print("- Inteligencia:", self.inteligencia)
        print("- Piernas:", "Sí" if self.piernas else "No")


class R2D2(Robot):
    def __init__(self):
        super().__init__(color="Blanco", altura="Bajo", inteligencia="Más inteligente")
        self.piernas = False

    def caracteristicas_especificas(self):
        print("Características específicas de R2D2:")
        print("- Color:", self.color)
        print("- Altura:", self.altura)
        print("- Inteligencia:", self.inteligencia)
        print("- Piernas:", "Sí" if self.piernas else "No")



c3po = C3PO()
r2d2 = R2D2()

print("Características generales de C3PO:")
c3po.activar()
c3po.caracteristicas_especificas()
c3po.pausar()

print("\nCaracterísticas generales de R2D2:")
r2d2.activar()
r2d2.caracteristicas_especificas()
r2d2.pausar()
