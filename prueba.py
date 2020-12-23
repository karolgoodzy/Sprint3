import functools
import os # Para generar la llave aleatoria
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField
from formularios import FormSesion, FormRegistro, FormRecuperar, FormCrear, FormActualizar, FormEliminar, FormDescargar, FormContact
from db import get_db, close_db
from message import mensaje
import yagmail
import utils
from werkzeug.utils import secure_filename # para obtener el nombre del archivo de forma segura.

app = Flask(__name__)

SECRET_KEY = os.urandom(32) # Para generar la llave aleatoria
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
def Home():
    return render_template('index.html', titulo='Red Social de Imagenes')


@app.route('/sesion', methods=['GET', 'POST'])
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
                return redirect(url_for('message'))
            flash(error)
        form = FormSesion()
        return render_template('sesion.html', titulo='Iniciar Sesión', form=form)
    #except:
    #    form = FormSesion()
    #    return render_template('sesion.html', titulo='Iniciar Sesión', form=form)


@app.route('/registro', methods=['GET', 'POST'])
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
@app.route('/recuperar/', methods=['GET','POST'])
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



@app.route('/message', methods=['GET', 'POST'])
def message():
    print("Retrieving info")
    return jsonify( {'mensaje':mensaje} )

if __name__ == '__main__':
    app.run(debug=True, port=5000)