archivo = open('quijote.txt')
contenido = archivo.read()
archivo.close()

letras = set()

for letra in contenido:
    letras.add(letra)

simbolos = ''
for letra in letras:
    if letra not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
        simbolos += letra

print('símbolos en el quijote:', simbolos)
