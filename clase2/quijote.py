import re

with open('quijote.txt') as archivo:
    contenido = archivo.read()

contenido = contenido.replace('\n', ' ')
contenido = re.sub(' {2,}', ' ', contenido)
contenido = re.sub('[^\w ]', '', contenido)
contenido = contenido.lower()
contenido = contenido.split(' ')

palabras = {}

for palabra in contenido:
    if len(palabra) > 3:
        if palabra in palabras:
            palabras[palabra] += 1
        else:
            palabras[palabra] = 1

palabras_lista = list(palabras.items())
palabras_lista.sort(key=lambda i: i[1], reverse=True)

print(palabras_lista[:30])
