#  Usuario y su contraseña, recordar, enviar

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FileField, TextAreaField
from wtforms.validators import DataRequired

class FormSesion(FlaskForm):
    usuarioSesion = StringField('Usuario', validators=[DataRequired(message='No dejar vacio, completar')])
    claveSesion = PasswordField('Contraseña', validators=[DataRequired(message='No dejar vacio, completar')])
    recordar = BooleanField('Recordar Usuario')
    iniciar = SubmitField('Iniciar Sesión')


class FormRegistro(FlaskForm):
    nombres = StringField('Nombres', validators=[DataRequired(message='No dejar vacio, completar')])
    apellidos = StringField('Apellidos', validators=[DataRequired(message='No dejar vacio, completar')])
    correoRegistro = StringField('Correo Electrónico', validators=[DataRequired(message='No dejar vacio, completar')])
    usuarioRegistro = StringField('Nombre de Usuario', validators=[DataRequired(message='No dejar vacio, completar')])
    claveRegistro = PasswordField('Contraseña', validators=[DataRequired(message='No dejar vacio, completar')])
    confirme = PasswordField('Confirme Contraseña', validators=[DataRequired(message='No dejar vacio, completar')])
    registrar = SubmitField('Registrar Usuario')


class FormRecuperar(FlaskForm):
    correoRecuperar = StringField('Correo Electrónico', validators=[DataRequired(message='No dejar vacio, completar')])
    recuperar = SubmitField('Enviar')


class FormCrear(FlaskForm):
    nomImgCrear = StringField('Nombre de la imagen', validators=[DataRequired(message='No dejar vacio, completar')])
    publicoCrear = BooleanField('Publica')
    privadoCrear = BooleanField('Privada')
    crearArchivo = FileField('Seleccionar archivo')
    crear = SubmitField('Crear')


class FormActualizar(FlaskForm):
    nomImgActlzar = StringField('Nombre de la imagen', validators=[DataRequired(message='No dejar vacio, completar')])
    nuevoNombre = StringField('Nuevo nombre', validators=[DataRequired(message='No dejar vacio, completar')])
    publicoActlzar = BooleanField('Publica')
    privadoActlzar = BooleanField('Privada')
    actlzarArchivo = FileField('Seleccionar archivo')
    actualizar = SubmitField('Actualizar')


class FormEliminar(FlaskForm):
    nomImgElimnar = StringField('Nombre de la imagen', validators=[DataRequired(message='No dejar vacio, completar')])
    checkborrar = BooleanField('¿Desea eliminar?')
    eliminar = SubmitField('Eliminar')


class FormDescargar(FlaskForm):
    nomImgDescgar = StringField('Nombre de la imagen', validators=[DataRequired(message='No dejar vacio, completar')])
    descargar = SubmitField('Descargar')


class FormContact(FlaskForm):
    remitente = StringField('Nombre', validators=[DataRequired(message='No dejar vacio, completar')])
    correoRte = StringField('Correo Electrónico', validators=[DataRequired(message='No dejar vacio, completar')])
    mensaje = TextAreaField('Mensaje', validators=[DataRequired(message='No dejar vacio, completar')])
    enviar = SubmitField('Enviar')