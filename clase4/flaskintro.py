from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html', nombre='Moisés')


@app.route('/saludo/<nombre>')
def saludo(nombre):
    return 'Hello ' + nombre


@app.route('/error')
def crear_error():
    a = int('jjjjj')
    return 'Hola mundo!'


@app.route('/calculadora/<operacion>/<a>/<b>')
def sumar(operacion, a, b):
    resultado = 0

    if operacion == 'sumar':
        resultado = int(a) + int(b)
    elif operacion == 'restar':
        resultado = int(a) - int(b)
    elif operacion == 'multiplicar':
        resultado = int(a) * int(b)

    return render_template('resultado.html', resultado=resultado)


@app.route('/pruebas')
def pruebas():
    contexto = {
        'verdad': True,
        'lista': ['pan', 'leche', 'huevos', 'tocino'],
        'pepito': {
            'nombre': 'Pepito',
            'edad': 18,
            'distrito': 'Puente Piedra'
        }
    }
    return render_template('pruebas.html', **contexto)


@app.route('/servicio')
def servicio():
    # logica...
    return jsonify({'exito': True})


if __name__ == '__main__':
    app.run(debug=True)
