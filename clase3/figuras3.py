class FiguraGeometrica(object):
    def __init__(self, *lados):
        self.lados = lados

    def area(self, formula):
        return formula(*self.lados)

triangulo = FiguraGeometrica(3, 4)
print(
    triangulo.area(lambda b, h: (b * h) / 2)
)