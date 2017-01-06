import requests

respuesta_inicial = requests.get('http://api.fixer.io/latest')
respuesta_inicial = respuesta_inicial.json()
monedas = [respuesta_inicial['base']]

for nombre, valor in respuesta_inicial['rates'].items():
    monedas.append(nombre)

print('Tipos de moneda disponibles:')
for indice, nombre in enumerate(monedas):
    print('{}. {}'.format(indice + 1, nombre))

inicio = int(input('Seleccione moneda de inicio: '))
moneda_inicio = monedas[inicio - 1]

final = int(input('Seleccione moneda a convertir: '))
moneda_final = monedas[final - 1]

monto = float(input('Ingrese monto: '))

tipo_cambio = requests.get('http://api.fixer.io/latest',
                           params={'base': moneda_inicio})
tipo_cambio = tipo_cambio.json()
factor_cambio = tipo_cambio['rates'][moneda_final]

print('Resultado: {}'.format(monto * factor_cambio))
