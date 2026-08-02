from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/escritorio_camilleros')
def escritorio_camilleros():
    return render_template('escritorio_camilleros.html')

@app.route('/escritorio_lavadero')
def escritorio_lavadero():
    return render_template('escritorio_lavadero.html')

@app.route('/escritorio_conmutador')
def escritorio_conmutador():
    return render_template('escritorio_conmutador.html')

@app.route('/escritorio_ascensores')
def escritorio_ascensores():
    return render_template('escritorio_ascensores.html')

@app.route('/escritorio_intendencia')
def escritorio_intendencia():
    return render_template('escritorio_intendencia.html')

@app.route('/escritorio_dalo')
def escritorio_dalo():
    return render_template('escritorio_dalo.html')

@app.route('/escritorio_admin')
def escritorio_admin():
    return render_template('escritorio_admin.html')

if __name__ == '__main__':
    app.run(debug=True)
