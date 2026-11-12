from flask import Flask, render_template

# Inicializa la aplicación Flask
app = Flask(__name__)

# Define la ruta principal que devolverá el archivo HTML
@app.route('/')
def home():
    return render_template('index.html')

# Ejecuta el servidor local
if __name__ == '__main__':
    app.run(debug=True)