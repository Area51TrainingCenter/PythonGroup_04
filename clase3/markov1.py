import pickle
import re

with open('quijote.txt', encoding='utf-8') as archivo:
    contenido = archivo.read()

contenido = contenido.replace('\n', ' ')
contenido = re.sub(' {2,}', ' ', contenido)
contenido = re.sub('[^\w ]', '', contenido)
contenido = contenido.lower()
contenido = contenido.split(' ')

palabras = {}

for posicion, palabra in enumerate(contenido[:-1]):
    if palabra not in palabras:
        palabras[palabra] = []
    palabras[palabra].append(contenido[posicion + 1])

with open('markov.bin', 'wb') as f:
    f.write(pickle.dumps(palabras))
