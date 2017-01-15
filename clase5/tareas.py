from flask import Flask, render_template, request, redirect
from pony.orm import db_session, select
from modelos import Tarea

app = Flask(__name__)


@app.route('/')
def index():
    with db_session:
        tareas_consulta = select(tarea for tarea in Tarea)[:]
    return render_template('index.html', tareas=tareas_consulta)


@app.route('/agregar', methods=['POST'])
def agregar():
    nombre_tarea = request.form['tarea']

    with db_session:
        Tarea(nombre=nombre_tarea)

    return redirect('/')


@app.route('/borrar/<int:pk>')
def borrar(pk):
    with db_session:
        tarea = Tarea[pk]
        tarea.delete()

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
