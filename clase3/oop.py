class Juguete(object):
    marca = 'Mattel'


class Auto(object):
    motor = 'V8'
    marca = 'BMW'
    ruedas = 4


# MRO: Method resolution order
class AutoDeJuguete(Juguete, Auto):
    # inicializador de instancia
    def __init__(self, color):
        self.color = color

    # constructor de instancia
    # def __new__(cls, *args, **kwargs):
    #     pass

    def arrancar(self):
        print('run run run')

    def __str__(self):
        return '<auto {}>'.format(self.color)


max5 = AutoDeJuguete('blanco')
print(max5.ruedas)
print(max5.color)
max5.arrancar()
print(max5)
print(max5.marca)

otro = AutoDeJuguete('rojo')
print(otro.ruedas)
print(otro.color)

