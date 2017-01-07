from flask import Flask, render_template, request
import requests  # pip install requests

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello():
    if request.method == 'POST':
        valores = request.form
        nombre = valores.get('nombre')
        email = valores.get('email')
        mensaje = valores.get('mensaje')
        requests.post(
            'https://api.mailgun.net/v3/sandboxed7d5bcac9fd4247bb8e22e8a469eecb.mailgun.org/messages',
            auth=('api', 'key-4fab09ec3e1a3a248aaeb5ea0b02e24b'),
            data={'from': 'Moisés <moi@ses.mailgun.org>',
                  'to': ['xpktro@gmail.com'],
                  'subject': 'Formulario de contacto',
                  'text': '{} ({}) te ha enviado el siguiente mensaje: {}'.format(nombre, email, mensaje)})
    else:
        valores = {}
    return render_template('contacto.html', valores=valores)

if __name__ == '__main__':
    app.run(debug=True)
