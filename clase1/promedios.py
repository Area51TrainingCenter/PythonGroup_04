cantidad_notas = input('cuantas notas deseas ingresar?: ')
cantidad_notas = int(cantidad_notas)

notas = []

for nota in range(cantidad_notas):
    nota_ingresada = input('ingrese la nota numero {}: '.format(nota + 1))
    notas.append(int(nota_ingresada))

suma = sum(notas)
promedio = suma / len(notas)
print('tu promedio es', promedio)
if promedio > 12:
    print('aprobaste')
else:
    print('jalaste')
