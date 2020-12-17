from flask import Flask, render_template, request
import yagmail
import utils
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/registro/')
def registro():
    return render_template('registro.html')

@app.route('/busquedaimagenes/')
def busqueda():
    return render_template('busquedaImagenes.html')

@app.route('/sesion/', methods=['GET', 'POST'])
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
               contents='Revisa tur correo para activar tu cuenta.') 
               return "Correo enviado a:  " + email
            else:
               return "Usuario no valido.  " + usuario
         else:
            return "Correo no valido.  " + usuario
      else:         
          return 'Entra con GET'
    #except: 
       #return render_template('sesion.html')

@app.route('/gestorimagen/')
def gestor():
    return render_template('gestorImagen.html')


@app.route('/sesion/recuperarcontrasena/')
def recuperar():
    return render_template('recuperarcontrasena.html')


@app.route('/gestorimagen/crearactualizar/')
def actualizar():
    return render_template('crearActualizar.html')

@app.route('/gestorimagen/eliminar/')
def eliminar():
    return render_template('eliminar.html')

@app.route('/gestorimagen/descargar/')
def descargar():
    return render_template('descargar.html')

