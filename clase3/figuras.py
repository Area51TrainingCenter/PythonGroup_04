class FiguraGeometrica(object):
    """
    Docstrings: Una cadena que describe la funcionalidad de una clase o una
    función
    """

    def area(self):
        """Descripción del método"""
        print('aqui iria el area')


class Rectangulo(FiguraGeometrica):
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2

    def area(self):
        return self.lado1 * self.lado2


class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super(Cuadrado, self).__init__(lado, lado)


class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

rectangulo = Rectangulo(10, 20)
print(rectangulo.area())

cuadrado = Cuadrado(5)
print(cuadrado.area())

triangulo = Triangulo(4, 5)
print(triangulo.area())

