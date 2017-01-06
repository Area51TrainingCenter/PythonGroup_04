class FiguraGeometrica(object):
    def __init__(self, *lados):
        self.lados = lados

    def formula(self, lados):
        # clase abstracta
        raise NotImplementedError

    def area(self):
        return self.formula(self.lados)


class Triangulo(FiguraGeometrica):
    def formula(self, lados):
        base, altura = lados
        return (base * altura) / 2


triangulo = Triangulo(3, 4)
print(triangulo.area())