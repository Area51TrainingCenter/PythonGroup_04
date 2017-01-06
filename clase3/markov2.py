import random
import pickle

with open('markov.bin', 'rb') as f:
    palabras = pickle.loads(f.read())

palabra_inicial = 'el'
numero_palabras = 30

resultado = [palabra_inicial]

for numero in range(numero_palabras):
    ultima_palabra = resultado[-1]
    lista_palabras = palabras[ultima_palabra]
    if lista_palabras:
        resultado.append(random.choice(lista_palabras))

print(' '.join(resultado)[:140])
