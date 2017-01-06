class Empleado(object):
    descuento = None

    def __init__(self, salario_bruto):
        self.salario_bruto = salario_bruto

    def salario_neto(self):
        return self.salario_bruto * (1 - self.descuento)


class Gerente(Empleado):
    descuento = 0.15


class Asistente(Empleado):
    descuento = 0.25

    def __init__(self, salario_bruto, servicio):
        super(Asistente, self).__init__(salario_bruto)
        self.servicio = servicio

    def salario_neto(self):
        original = super(Asistente, self).salario_neto()
        return (100 * self.servicio) + original

manuel = Gerente(10000)
print('Sueldo de Manuel: {}'.format(manuel.salario_neto()))

ronny = Asistente(250, 300)
print('Sueldo de Ronny: {}'.format(ronny.salario_neto()))
