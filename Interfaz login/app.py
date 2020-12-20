import os # Para generar la llave aleatoria
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField
from formularios import FormSesion, FormRegistro, FormRecuperar, FormCrear, FormActualizar, FormEliminar, FormDescargar
import yagmail
import utils

app = Flask(__name__)

SECRET_KEY = os.urandom(32) # Para generar la llave aleatoria
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/indexx')
def inicio():
    return render_template('index.html')

@app.route('/registro/')
def registro():
    return render_template('registro.html')

@app.route('/busquedaimagenes/')
def busqueda():
    return render_template('busquedaImagenes.html')

@app.route('/sesion/', methods=['GET','POST'])
def sesion():
    #try:
      if request.method == 'POST':
         usuario = request.form['usuario']
         clave = request.form['contraseña']
         email = request.form['correo']
         if utils.isEmailValid(email):
            if utils.isUsernameValid(usuario):
               yag = yagmail.SMTP('penarandah@uninorte.edu.co','TuClavePersonal')
               yag.send(to=email,subject='Validar cuenta',
               contents='Revisa tu correo para activar tu cuenta.')
               return "Correo enviado a:  " + email
            else:
               return "Usuario no valido.  " + usuario
         else:
            return "Correo no valido.  " + usuario
      else:
          return render_template('sesion.html')
    #except:
       #return render_template('sesion.html')

@app.route('/gestorimagen')
def gestor():
    return render_template('gestorImagen.html')


@app.route('/sesion/recuperarcontrasena/')
def recuperar():
    return render_template('recuperarcontrasena.html')


@app.route('/gestorimagen/crear/')
def crear():
    return render_template('crear.html')

@app.route('/gestorimagen/actualizar/')
def actualizar():
    return render_template('actualizar.html')

@app.route('/gestorimagen/eliminar/')
def eliminar():
    return render_template('eliminar.html')

@app.route('/gestorimagen/descargar/')
def descargar():
    return render_template('descargar.html')


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

@app.route('/')
def Home():
    return render_template('indexNew.html', titulo='Red Social de Imagenes')

@app.route('/sesionnew/', methods=['GET','POST'])
def sesionnew():
    form = FormSesion()
    if(form.validate_on_submit()):
        flash('Damos la bienvenida al usuario {}'.format(form.usuario1.data))
        return redirect(url_for('gestornew'))
    return render_template('sesionnew.html', titulo='Iniciar Sesión', form=form)

@app.route('/registronew/', methods=['GET','POST'])
def registronew():
    form = FormRegistro()
    if(form.validate_on_submit()):
        flash('Se ha registrado el usuario {}'.format(form.usuario2.data))
        return redirect(url_for('gracias'))
    return render_template('registroNew.html', titulo='Registrar Usuario', form=form)

@app.route('/sesionnew/recuperar/', methods=['GET','POST'])
def recuperarnew():
    form = FormRecuperar()
    if(form.validate_on_submit()):
        flash('Se ha enviado el enlace al correo {}'.format(form.correo2.data))
        return redirect(url_for('gracias'))
    return render_template('recuperarcontrasenaNew.html', titulo='Registrar Usuario', form=form)

@app.route('/gestorimagennew/')
def gestornew():
    return render_template('gestorImagenNew.html', titulo='Gestor de Imagenes')

@app.route('/gestorimagennew/crearnew/', methods=['GET','POST'])
def crearnew():
    form = FormCrear()
    if(form.validate_on_submit()):
        flash('Se ha creado la imagen {}'.format(form.nombreimagen1.data))
        return redirect(url_for('gracias'))
    return render_template('crearNew.html', titulo='Crear Imagen', form=form)

@app.route('/gestorimagennew/actualizarnew/', methods=['GET','POST'])
def actualizarnew():
    form = FormActualizar()
    if(form.validate_on_submit()):
        flash('Se ha actualizado la imagen {} a {}'.format(form.nombreimagen2.data, form.nuevonombre.data))
        return redirect(url_for('gracias'))
    return render_template('actualizarnew.html', titulo='Actualizar Imagen', form=form)

@app.route('/gestorimagennew/eliminarnew/', methods=['GET','POST'])
def eliminarnew():
    form = FormEliminar()
    if(form.validate_on_submit()):
        flash('Se ha eliminado la imagen {}'.format(form.nombreimagen3.data))
        return redirect(url_for('gracias'))
    return render_template('eliminarNew.html', titulo='Eliminar Imagen', form=form)

@app.route('/gestorimagennew/descargarnew/', methods=['GET','POST'])
def descargarnew():
    form = FormDescargar()
    if(form.validate_on_submit()):
        flash('Se ha descargado la imagen {}'.format(form.nombreimagen4.data))
        return redirect(url_for('gracias'))
    return render_template('descargarNew.html', titulo='Descargar Imagen', form=form)

@app.route('/gracias/')
def gracias():
    return render_template('gracias.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)