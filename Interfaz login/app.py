import functools
import os # Para generar la llave aleatoria
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField
from formularios import FormSesion, FormRegistro, FormRecuperar, FormCrear, FormActualizar, FormEliminar, FormDescargar, FormContact
import yagmail
import utils
from werkzeug.utils import secure_filename # para obtener el nombre del archivo de forma segura.

app = Flask(__name__)

# Codigo para crear token de seguridad y crear carpeta de imagenes
FOLDER_CARGA = os.path.abspath("static/resources") # carpeta donde se cargarán las imágenes.
SECRET_KEY = os.urandom(32) # Para generar la llave aleatoria
app.config['SECRET_KEY'] = SECRET_KEY
app.config["FOLDER_CARGA"] = FOLDER_CARGA


####################################
# Reparar pagina para buscar imagenes
@app.route('/busquedaimagenes/')
def busqueda():
    return render_template('busquedaImagenes.html')
####################################


#############################################################
# Reparar para enviar correos electronicos con yagmail ######
@app.route('/login/', methods=['GET','POST'])
def login():
    try:
        if request.method == 'POST':
            usuario = request.form['usuario']
            clave = request.form['clave']
            email = request.form['email']
            if utils.isEmailValid(email):         
                if utils.isUsernameValid(usuario):            
                    yag = yagmail.SMTP('cdvitola@uninorte.edu.co','Jesuischriss_25')
                    yag.send(to=email,subject='Validar cuenta',
                    contents='Revisa tu correo para activar tu cuenta.') 
                    return "Correo enviado a:  " + email
                else:
                    return "Usuario no valido.  " + usuario
            else:
                return "Correo no valido.  " + usuario
        else:
            return 'Entra con GET'
    except:
        return render_template('registro.html')
##############################################################


# Pagina de Bienvenida
@app.route('/')
def Home():
    return render_template('indexNew.html', titulo='Red Social de Imagenes')


# Pagina para iniciar sesión
@app.route('/sesionnew/', methods=['GET','POST'])
def sesionnew():
    form = FormSesion()
    if(form.validate_on_submit()):
        flash('Damos la bienvenida al usuario {}'.format(form.usuarioSesion.data))
        return redirect(url_for('gestornew'))
    return render_template('sesionnew.html', titulo='Iniciar Sesión', form=form)


# Pagina para registar usuario
@app.route('/registronew/', methods=['GET','POST'])
def registronew():
    form = FormRegistro()
    if(form.validate_on_submit()):
        flash('Se ha registrado el usuario {}'.format(form.usuarioRegistro.data))
        return redirect(url_for('gracias'))
    return render_template('registroNew.html', titulo='Registrar Usuario', form=form)


# Pagina para recuperar contraseña
@app.route('/sesionnew/recuperar/', methods=['GET','POST'])
def recuperarnew():
    form = FormRecuperar()
    if(form.validate_on_submit()):
        email = form.correoRecuperar.data
        if utils.isEmailValid(email):
            yag = yagmail.SMTP('cdvitola@uninorte.edu.co','Jesuischriss_25')
            yag.send(to=email,subject='Restablecer Contraseña',
            contents="""
            Hola, querido usuario:

            Te hemos enviado un enlace para que puedas restablecer tu contraseña.

            https://www.avenidasiemprevivacalle123.com.co
            
            Que tengas un resto de dia muy agradable.

            Atentamente,

            La Administracion.""")
            flash('Se ha enviado un enlace de "restablecer contraseña" a tu correo {}'.format(form.correoRecuperar.data))
            return redirect(url_for('gracias'))
        else:
            flash('El correo {} no es valido'.format(form.correoRecuperar.data))
            return redirect(url_for('recuperarnew'))
    return render_template('recuperarcontrasenaNew.html', titulo='Registrar Usuario', form=form)





# Pagina del gestor para interactuar con las imagenes
@app.route('/gestorimagennew/')
def gestornew():
    return render_template('gestorImagenNew.html', titulo='Gestor de Imagenes')


# Pagina para crear imagenes
@app.route('/gestorimagennew/crearnew/', methods=['GET','POST'])
def crearnew():
    form = FormCrear()
    if(form.validate_on_submit()):
        flash('Se ha creado la imagen {}'.format(form.nomImgCrear.data))
        return redirect(url_for('imagenSubidaCr'))
    return render_template('crearNew.html', titulo='Crear Imagen', form=form)

# Pagina para cuando la imagen creada se sube al proyecto
@app.route('/gestorimagennew/crearnew/imagensubida', methods=('GET', 'POST') )
#@login_required
def imagenSubidaCr():
    path = ''
    form = FormCrear()
    if request.method == 'POST':
        archivo = form.crearArchivo.data
        filename = secure_filename(archivo.filename) # obtener el nombre del archivo de forma segura.
        path = os.path.join(app.config["FOLDER_CARGA"], filename) # ruta de la imagen, incluyendola.
        archivo.save(path)
        path = os.path.join('static/resources/', filename)
        flash( 'Imagen guardada con éxito.' )
        return render_template("imgCrearSubida.html", nombrearchivo=filename, path=path)
    return redirect(url_for('crearnew'))


# Pagina para actualizar imagenes
@app.route('/gestorimagennew/actualizarnew/', methods=['GET','POST'])
def actualizarnew():
    form = FormActualizar()
    if(form.validate_on_submit()):
        flash('Se ha actualizado la imagen {} a {}'.format(form.nomImgActlzar.data, form.nuevoNombre.data))
        return redirect(url_for('imagenSubidaAct'))
    return render_template('actualizarnew.html', titulo='Actualizar Imagen', form=form)

# Pagina para cuando la imagen actualizada se sube al proyecto
@app.route('/gestorimagennew/actualizarnew/imagensubida', methods=('GET', 'POST') )
#@login_required
def imagenSubidaAct():
    path = ''
    form = FormActualizar()
    if request.method == 'POST':
        archivo = form.actlzarArchivo.data
        filename = secure_filename(archivo.filename) # obtener el nombre del archivo de forma segura.
        path = os.path.join(app.config["FOLDER_CARGA"], filename) # ruta de la imagen, incluyendola.
        archivo.save(path)
        path = os.path.join('static/resources/', filename)
        flash( 'Imagen guardada con éxito.' )
        return render_template("imgActlzarSubida.html", nombrearchivo=filename, path=path)
    return redirect(url_for('actualizarnew'))


# Pagina para eliminar imagenes
@app.route('/gestorimagennew/eliminarnew/', methods=['GET','POST'])
def eliminarnew():
    form = FormEliminar()
    if(form.validate_on_submit()):
        flash('Se ha eliminado la imagen {}'.format(form.nomImgElimnar.data))
        return redirect(url_for('gracias'))
    return render_template('eliminarNew.html', titulo='Eliminar Imagen', form=form)


# Pagina para descargar imagenes
@app.route('/gestorimagennew/descargarnew/', methods=['GET','POST'])
def descargarnew():
    form = FormDescargar()
    if(form.validate_on_submit()):
        flash('Se ha descargado la imagen {}'.format(form.nomImgDescgar.data))
        return redirect(url_for('gracias'))
    return render_template('descargarNew.html', titulo='Descargar Imagen', form=form)





# Pagina de contacto
@app.route('/contactenos/', methods=['GET','POST'])
def contactenos():
    form = FormContact()
    if(form.validate_on_submit()):
        flash('Contáctenos solicitado por Nombre: {}, Correo: {}'.format(form.remitente.data, form.correoRte.data))
        return redirect(url_for('gracias'))
    return render_template('contactenos.html', titulo='Contáctenos', form=form)

# Pagina de agradecimiento
@app.route('/gracias/')
def gracias():
    return render_template('gracias.html')

# Transicion para cerrar sesion
@app.route('/logout/')
def logout():
    return redirect( url_for( 'Home' ) )

# Variables desconocidas y necesarias. No tocar
if __name__ == '__main__':
    app.run(debug=True, port=5000)