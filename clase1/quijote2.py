archivo = open('quijote.txt')
contenido = archivo.read()
archivo.close()

letras = {}

for letra in contenido:
    if letras.get(letra) == None:
        letras[letra] = 1
    else:
        letras[letra] += 1

letras_lista = list(letras.items())
letras_lista.sort(key=lambda i: i[1], reverse=True)
print(letras_lista)
