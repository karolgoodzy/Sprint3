import functools
import os # Para generar la llave aleatoria
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField
from formularios import FormSesion, FormRegistro, FormRecuperar, FormCrear, FormActualizar, FormEliminar, FormDescargar, FormBuscar, FormContact
from db import get_db, close_db
import yagmail
import utils
from werkzeug.utils import secure_filename # para obtener el nombre del archivo de forma segura.

app = Flask(__name__)

# Codigo para crear token de seguridad y crear carpeta de imagenes
#FOLDER_CARGA = os.path.abspath("static/resources") # carpeta donde se cargarán las imágenes.
SECRET_KEY = os.urandom(32) # Para generar la llave aleatoria
app.config['SECRET_KEY'] = SECRET_KEY
app.config["UPLOAD_FOLDER"] = 'static/resources'


# Pagina de Bienvenida
@app.route('/')
def Home():
    return render_template('index.html', titulo='Red Social de Imagenes')


# Pagina para iniciar sesión
@app.route('/sesion/', methods=['GET', 'POST'])
def sesion():
    #try:
        if request.method == 'POST':
            form = FormSesion()
            db = get_db()
            error = None
            username = request.form['usuarioSesion']
            password = request.form['claveSesion']

            if not username:
                error ='Debes ingresar el usuario'
                flash(error)
                return render_template('sesion.html', titulo='Iniciar Sesión', form=form)
            
            if not password:
                error = 'contraseña requerida'
                flash(error)
                return render_template('sesion.html', titulo='Iniciar Sesión', form=form)
            
            user = db.execute('SELECT * FROM Usuarios WHERE usuario = ? AND clave = ?',(username, password)).fetchone()
            print(user)
            if user is None:
                error = 'usuario o contraseña inválidos'
            else:
                return redirect(url_for('gestor'))
            flash(error)
        form = FormSesion()
        return render_template('sesion.html', titulo='Iniciar Sesión', form=form)
    #except:
    #    form = FormSesion()
    #    return render_template('sesion.html', titulo='Iniciar Sesión', form=form)


# Pagina para registar usuario
@app.route('/registro/', methods=['GET', 'POST'])
def registro():
    #try:
        if request.method == 'POST':
            form = FormRegistro()
            db = get_db()
            error = None
            name = request.form['nombres']
            lastname = request.form['apellidos']
            email = request.form['correoRegistro']
            username = request.form['usuarioRegistro']
            password = request.form['claveRegistro']

            if not name:
                error ='Debes ingresar tu nombre'
                flash(error)
                return render_template('registro.html', titulo='Registrar Usuario', form=form)
            
            if not lastname:
                error = 'Debes ingresar tus apellidos'
                flash(error)
                return render_template('registro.html', titulo='Registrar Usuario', form=form)
            
            if not email:
                error = 'Debes ingresar tu correo'
                flash(error)
                return render_template('registro.html', titulo='Registrar Usuario', form=form)
            
            if not username:
                error ='Debes ingresar el usuario'
                flash(error)
                return render_template('registro.html', titulo='Registrar Usuario', form=form)
            
            if not password:
                error = 'contraseña requerida'
                flash(error)
                return render_template('registro.html', titulo='Registrar Usuario', form=form)
            
            if db.execute( 'SELECT * FROM Usuarios WHERE correo = ?', (email,) ).fetchone() is not None:
                error = 'El correo {} ya existe'.format( email )
                flash( error )
                return render_template('registro.html', titulo='Registrar Usuario', form=form)

            db.execute(
                'INSERT INTO Usuarios (nombre, apellidos, usuario, correo, clave) VALUES (?,?,?,?,?)',
                (name, lastname, username, email, password)
            )
            db.commit()

            if utils.isEmailValid(email):         
                if utils.isUsernameValid(username):            
                    yag = yagmail.SMTP('cdvitola@uninorte.edu.co','Jesuischriss_25')
                    yag.send(to=email,subject='Activar cuenta',
                    contents="""
                    Bienvenido/a  """+ name +""":


                    Te agradecemos por ser parte de nuestra gran red de imagenes.

                    Usa este link para activar tu cuenta y gozar de nuestro servicios:

                    https://www.avenidasiemprevivacallefalsa123.com.co

                    Que tengas un resto de dia muy agradable.


                    Atentamente,

                           La Administracion.""")
                else:
                    flash( "Usuario no valido " + name ) 
                    return render_template('registro.html', titulo='Registrar Usuario', form=form)
            else:
                flash( "Correo no valido " + name )
                return render_template('registro.html', titulo='Registrar Usuario', form=form)
            # yag = yagmail.SMTP('micuenta@gmail.com', 'clave') #modificar con tu informacion personal
            # yag.send(to=email, subject='Activa tu cuenta',
            #        contents='Bienvenido, usa este link para activar tu cuenta ')
            #mensaje = 'Revisa tu correo para activar tu cuenta'
            flash( 'Revisa tu correo para activar tu cuenta' )
            form = FormSesion()
            return redirect(url_for('sesion'))
        form = FormRegistro()
        return render_template('registro.html', titulo='Registrar Usuario', form=form)
    #except:
    #    form = FormSesion()
    #    return render_template('registro.html', titulo='Registrar Usuario', form=form)


# Pagina para recuperar contraseña
@app.route('/sesion/recuperar/', methods=['GET','POST'])
def recuperar():
    form = FormRecuperar()
    if(form.validate_on_submit()):
        email = request.form['correoRecuperar']
        db = get_db()
        error = None
        #email = form.correoRecuperar.data
        if not email:
            error = 'Debes ingresar tu correo'
            flash(error)
            return render_template('recuperarClave.html', titulo='Recuperar Clave', form=form)
        if db.execute( 'SELECT * FROM Usuarios WHERE correo = ?', (email,) ).fetchone() is None:
            error = 'El correo {} no hace parte de nuestras base de datos'.format( email )
            flash( error )
            return render_template('recuperarClave.html', titulo='Recuperar Clave', form=form)
        if utils.isEmailValid(email):
            yag = yagmail.SMTP('cdvitola@uninorte.edu.co','Jesuischriss_25')
            yag.send(to=email,subject='Restablecer Contraseña',
            contents="""
            Hola, querido usuario:


            Te hemos enviado un enlace para que puedas restablecer tu contraseña.

            https://www.avenidasiemprevivacallefalsa123.com.co

            Que tengas un resto de dia muy agradable.


            Atentamente,

                   La Administracion.""")
            flash('Se ha enviado un enlace de "restablecer contraseña" a tu correo {}'.format(form.correoRecuperar.data))
            return redirect(url_for('gracias'))
        else:
            flash('El correo {} no es valido'.format(form.correoRecuperar.data))
            return redirect(url_for('recuperar'))
    return render_template('recuperarClave.html', titulo='Recuperar Clave', form=form)





# Pagina del gestor para interactuar con las imagenes
@app.route('/gestor/')
def gestor():
    return render_template('gestorImagen.html', titulo='Gestor de Imagenes')


# Pagina para crear imagenes
@app.route('/gestor/crear/', methods=['GET','POST'])
def crear():
    form = FormCrear()
    if(form.validate_on_submit()):
        flash('Se ha creado la imagen {}'.format(form.nomImgCrear.data))
        return redirect(url_for('imagenSubidaCr'))
    return render_template('crear.html', titulo='Crear Imagen', form=form)

# Pagina para cuando la imagen creada se sube al proyecto
@app.route('/gestor/crear/imagensubida/', methods=('GET', 'POST') )
#@login_required
def imagenSubidaCr():
    path = ''
    form = FormCrear()
    if request.method == 'POST':
        file = request.files['crearArchivo']
        filename = secure_filename(file.filename) # obtener el nombre del archivo de forma segura.
        path = os.path.join(app.config["UPLOAD_FOLDER"],filename) # ruta de la imagen, incluyendola.
        file.save(path)
        flash( 'Imagen guardada con éxito.' )
    return render_template('imagenSubidaCr.html', nombrearchivo=filename, path=path)
    #return redirect(url_for('crear'))


# Pagina para actualizar imagenes
@app.route('/gestor/actualizar/', methods=['GET','POST'])
def actualizar():
    form = FormActualizar()
    if(form.validate_on_submit()):
        flash('Se ha actualizado la imagen {} a {}'.format(form.nomImgActulzar.data, form.nuevoNombre.data))
        return redirect(url_for('imagenSubidaAct'))
    return render_template('actualizar.html', titulo='Actualizar Imagen', form=form)

# Pagina para cuando la imagen actualizada se sube al proyecto
@app.route('/gestor/actualizar/imagensubida/', methods=('GET', 'POST') )
#@login_required
def imagenSubidaAct():
    path = ''
    form = FormActualizar()
    if request.method == 'POST':
        file = request.files['actulzarArchivo']
        filename = secure_filename(file.filename) # obtener el nombre del archivo de forma segura.
        path = os.path.join(app.config["UPLOAD_FOLDER"], filename) # ruta de la imagen, incluyendola.
        file.save(path)
        flash( 'Imagen actualizada con éxito.' )
    return render_template("imagenSubidaAct.html", nombrearchivo=filename, path=path)
    #return redirect(url_for('actualizar'))


# Pagina para eliminar imagenes
@app.route('/gestor/eliminar/', methods=['GET','POST'])
def eliminar():
    form = FormEliminar()
    if(form.validate_on_submit()):
        flash('Se ha eliminado la imagen {}'.format(form.nomImgElimnar.data))
        return redirect(url_for('gracias'))
    return render_template('eliminar.html', titulo='Eliminar Imagen', form=form)


# Pagina para descargar imagenes
@app.route('/gestor/descargar/', methods=['GET','POST'])
def descargar():
    form = FormDescargar()
    if(form.validate_on_submit()):
        flash('Se ha descargado la imagen {}'.format(form.nomImgDescgar.data))
        return redirect(url_for('gracias'))
    return render_template('descargar.html', titulo='Descargar Imagen', form=form)


# Pagina para buscar imagenes
@app.route('/gestor/buscar/', methods=['GET','POST'])
def buscar():
    form = FormBuscar()
    if(form.validate_on_submit()):
        flash('Se ha encontrado la imagen {}'.format(form.nomImgBuscar.data))
        return redirect(url_for('gracias'))
    return render_template('buscarImagen.html', titulo='Buscar Imagenes', form=form)



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
