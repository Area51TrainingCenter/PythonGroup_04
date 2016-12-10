import random
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

palabra_inicial = 'el'
numero_palabras = 30

resultado = [palabra_inicial]

for numero in range(numero_palabras):
    ultima_palabra = resultado[-1]
    lista_palabras = palabras[ultima_palabra]
    if lista_palabras:
        resultado.append(random.choice(lista_palabras))

print(' '.join(resultado)[:140])
