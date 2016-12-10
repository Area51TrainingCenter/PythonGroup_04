def decorar(uno, dos):
    ####
    def decorar_real(funcion):
        #####
        def funcion_decorada(*args):
            print(uno)
            retorno = funcion(*args)
            print(dos)
            return retorno
        #####
        return funcion_decorada
    ####
    return decorar_real


@decorar('hola', 'mundo')
def suma(op1, op2):
    return op1 + op2

# suma = decorar('hola', 'mundo')(suma)

print(suma(4, 5))