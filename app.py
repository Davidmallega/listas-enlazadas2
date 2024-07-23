from flask import Flask, request, render_template, redirect, url_for
from controllers.paquete_controller import PaqueteController
from views.paquete_view import render_index, render_paquete, render_paquete_form

app = Flask(__name__)
paquete_controller = PaqueteController()

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/paquetes')
def index():
    paquetes = paquete_controller.obtener_todos_los_paquetes()
    return render_index(paquetes)

@app.route('/paquete/<codigo_seguimiento>')
def mostrar_paquete(codigo_seguimiento):
    paquete = paquete_controller.obtener_paquete(codigo_seguimiento)
    return render_paquete(paquete)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar_paquete():
    if request.method == 'POST':
        codigo_seguimiento = request.form['codigo_seguimiento']
        origen = request.form['origen']
        destino = request.form['destino']
        estado = request.form['estado']
        paquete_controller.insertar_paquete(codigo_seguimiento, origen, destino, estado)
        return redirect(url_for('index'))
    return render_paquete_form()

@app.route('/eliminar/<codigo_seguimiento>')
def eliminar_paquete(codigo_seguimiento):
    paquete_controller.eliminar_paquete(codigo_seguimiento)
    return redirect(url_for('index'))

@app.route('/actualizar/<codigo_seguimiento>', methods=['GET', 'POST'])
def actualizar_paquete(codigo_seguimiento):
    if request.method == 'POST':
        nuevo_estado = request.form['estado']
        paquete_controller.actualizar_estado(codigo_seguimiento, nuevo_estado)
        return redirect(url_for('mostrar_paquete', codigo_seguimiento=codigo_seguimiento))
    paquete = paquete_controller.obtener_paquete(codigo_seguimiento)
    return render_paquete_form(paquete=paquete, actualizar=True)

@app.route('/buscar', methods=['GET'])
def buscar_paquete():
    codigo = request.args.get('codigo')
    if codigo:
        paquete = paquete_controller.obtener_paquete(codigo)
        if paquete:
            return render_index([paquete])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
