from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def primerPaso():
    return '¡Hola, mundo!'

@app.route('/vista')
def rutas():
    return 'Esto es una vista'

@app.route('/plantillas')
def plantillas():
    data = [
            {'nombre':"Gonzalo", 'apellido':"Lecumberri"},
            {'nombre':"Pepito", 'apellido':"popito"}
        ]
    return render_template('index.html', data = data)

if __name__ == '__main__':
    app.run(debug=True, port=5001)