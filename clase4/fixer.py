from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def fixer():
    monedas_response = requests.get(
        'http://api.fixer.io/latest'
    ).json()
    monedas = [monedas_response['base']] + list(monedas_response['rates'].keys())

    resultado = ''

    if request.method == 'POST':
        origen = request.form['origen']
        destino = request.form['destino']
        monto = request.form['monto']
        resultado_response = requests.get('http://api.fixer.io/latest',
                                          params={'base': origen}).json()
        resultado = resultado_response['rates'][destino] * float(monto)

    return render_template('fixer.html', monedas=monedas, resultado=resultado)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
