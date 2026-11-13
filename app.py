from flask import Flask, render_template

# Inicializa la aplicación Flask
app = Flask(__name__)

from flask import Flask, render_template

# Inicializa la aplicación Flask
app = Flask(__name__)
# Datos provisorios: borrar cuando la base esté armada
DEPOSITOS_PROVISORIOS = [
    {"id": 1, "nombre": "Depósito Central",  "tipos": 12, "unidades": 340},
    {"id": 2, "nombre": "Laboratorio",       "tipos": 8,  "unidades": 95},
    {"id": 3, "nombre": "Sala de Profesores","tipos": 5,  "unidades": 27},
    {"id": 4, "nombre": "Taller",            "tipos": 0,  "unidades": 0},  # caso depósito vacío
]

# Define la ruta principal que devolverá el archivo HTML
@app.route('/')
def home():
    depositos = DEPOSITOS_PROVISORIOS
    return render_template('index.html', depositos=depositos)

# Ejecuta el servidor local
if __name__ == '__main__':
    app.run(debug=True)