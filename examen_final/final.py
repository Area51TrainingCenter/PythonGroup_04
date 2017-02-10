import re

apostoles = ['Andres', 'Bartolome', 'Santiago', 'Juan', 'Judas', 'Mateo', 'Pedro', 'Felipe', 'Simon', 'Tomas']
apostoles = map(str.lower, apostoles)

with open('nuevo_testamento.txt', encoding='utf-8') as f:
    contenido = f.read()

contenido = contenido.replace('\n', ' ')
contenido = re.sub('[^\w ]', '', contenido)
contenido = re.sub(' {2,}', ' ', contenido)
contenido = contenido.lower()
contenido = re.sub('á', 'a', contenido)
contenido = re.sub('é', 'e', contenido)
contenido = re.sub('í', 'i', contenido)
contenido = re.sub('ó', 'o', contenido)
contenido = re.sub('ú', 'u', contenido)
contenido = contenido.split(' ')

apostoles_ranking = {apostol: 0 for apostol in apostoles}

for palabra in contenido:
    if palabra in apostoles_ranking:
        apostoles_ranking[palabra] += 1

apostoles = list(apostoles_ranking.items())
apostoles.sort(key=lambda i: i[1], reverse=True)

print(apostoles)
