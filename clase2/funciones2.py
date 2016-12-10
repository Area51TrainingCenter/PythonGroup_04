def operador(operacion):
    def suma(op1, op2):
        return op1 + op2

    def resta(op1, op2):
        return op1 - op2

    def producto(op1, op2):
        return op1 * op2

    funcion = None
    if operacion == '+':
        funcion = suma
    elif operacion == '-':
        funcion = resta
    elif operacion == '*':
        funcion = producto

    return funcion

operacion = operador('*')
print(operacion(4, 5))