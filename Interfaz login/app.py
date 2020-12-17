from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("index.html")

@app.route('/registro/')
def registro():
    return render_template('registro.html')

@app.route('/busquedaImagenes/')
def busqueda():
    return render_template("busquedaImagenes.html")

@app.route('/sesion/')
def sesion():
    return render_template("sesion.html")

@app.route('/gestorimagen/')
def gestor():
    return render_template("gestorImagen.html")


@app.route('/sesion/recuperarcontrasena')
def recuperar():
    return render_template("recuperarcontrasena.html")


@app.route('/busquedaImagenes/gestorImagen')
def gestor1():
    return render_template("gestorimagen.html")

@app.route('/busquedaImagenes/busquedaImagenes/')
def busqueda1():
    return render_template("busquedaImagenes.html")

@app.route('/gestorImagen/crearActualizar')
def actualizar():
    return render_template("crearActualizar.html")

@app.route('/gestorImagen/eliminar')
def eliminar():
    return render_template("eliminar.html")

@app.route('/gestorImagen/descargar')
def descargar():
    return render_template("descargar.html")

@app.route('/gestorImagen/busquedaImagenes')
def busqueda2():
    return render_template("busquedaImagenes.html")

