def calcular(funcion, operando1, operando2):
    return funcion(operando1, operando2)


def suma(op1, op2):
    return op1 + op2


def resta(op1, op2):
    return op1 - op2


def producto(op1, op2):
    return op1 * op2

print(calcular(producto, 3, 5))

