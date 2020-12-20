#  Usuario y su contraseña, recordar, enviar

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class FormSesion(FlaskForm):
    usuario1 = StringField('Usuario', validators=[DataRequired(message='No dejar vacio, completar')])
    clave1 = PasswordField('Contraseña', validators=[DataRequired(message='No dejar vacio, completar')])
    recordar1 = BooleanField('Recordar Usuario')
    enviar1 = SubmitField('Iniciar Sesión')


class FormRegistro(FlaskForm):
    nombre1 = StringField('Nombre', validators=[DataRequired(message='No dejar vacio, completar')])
    apellido1 = StringField('Apellidos', validators=[DataRequired(message='No dejar vacio, completar')])
    correo1 = StringField('Correo Electrónico', validators=[DataRequired(message='No dejar vacio, completar')])
    usuario2 = StringField('Nombre de Usuario', validators=[DataRequired(message='No dejar vacio, completar')])
    clave2 = PasswordField('Contraseña', validators=[DataRequired(message='No dejar vacio, completar')])
    registrar = SubmitField('Registrar Usuario')

class FormRecuperar(FlaskForm):
    correo2 = StringField('Correo Electrónico', validators=[DataRequired(message='No dejar vacio, completar')])
    enviar2 = SubmitField('Enviar')

class FormCrear(FlaskForm):
    nombreimagen1 = StringField('Nombre de la imagen', validators=[DataRequired(message='No dejar vacio, completar')])
    publica1 = BooleanField('Publica')
    privada1 = BooleanField('Privada')
    crear = SubmitField('Crear')

class FormActualizar(FlaskForm):
    nombreimagen2 = StringField('Nombre de la imagen', validators=[DataRequired(message='No dejar vacio, completar')])
    nuevonombre = StringField('Nuevo nombre', validators=[DataRequired(message='No dejar vacio, completar')])
    publica2 = BooleanField('Publica')
    privada2 = BooleanField('Privada')
    actualizar = SubmitField('Actualizar')

class FormEliminar(FlaskForm):
    nombreimagen3 = StringField('Nombre de la imagen', validators=[DataRequired(message='No dejar vacio, completar')])
    confirmeliminar = BooleanField('Desea eliminar?')
    eliminar = SubmitField('Eliminar')

class FormDescargar(FlaskForm):
    nombreimagen4 = StringField('Nombre de la imagen', validators=[DataRequired(message='No dejar vacio, completar')])
    descargar = SubmitField('Descargar')

