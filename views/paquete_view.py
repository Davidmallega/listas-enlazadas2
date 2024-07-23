from flask import render_template

def render_index(paquetes):
    return render_template('index.html', paquetes=paquetes)

def render_paquete(paquete):
    return render_template('paquete.html', paquete=paquete)

def render_paquete_form(paquete=None, actualizar=False):
    return render_template('paquete_form.html', paquete=paquete, actualizar=actualizar)
