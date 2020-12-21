import os # Para generar el aleatorio
#importar el modulo sqlite3
import sqlite3
#importar modulo de error de sqlite3
from sqlite3 import Error
from flask import Flask, render_template, request, redirect, url_for, flash,  request
from wtforms import StringField
from flask_wtf import FlaskForm
from formularios import *

import yagmail
import utils

app = Flask(__name__)

SECRET_KEY = os.urandom(32) # Para generar la llave aleatoria
app.config['SECRET_KEY'] = SECRET_KEY

def sql_connection():
    try:
        con =  sqlite3.connect('mydatabase.sql')
        return con
    except Error:
        print(Error)

def sql_insert_usuarios(id, nombre, apellido, usuario, correo, clave):
    id = str(id)
    strsql = "INSERT INTO usuarios (id, nombre, apellido, usuario, correo, clave)  VALUES ('" + id + "', '" +  nombre +  "', '"  + apellido  + "', '" +  usuario +  "', '" +  correo +  "', '" +  clave +  "');"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(strsql)
    con.commit()
    con.close()
    return "OK"

def sql_select_usuarios():
	strsql = "select * from usuarios;"
	con = sql_connection()
	cursorObj = con.cursor()
	cursorObj.execute(strsql)
	usuarios = cursorObj.fetchall()
	return usuarios

def sql_edit_usuarios(id, nombre):
    id = str(id)
    strsql = "UPDATE usuarios SET nombre = '" + nombre +"' WHERE id = '" + id + "';"
    #strsql2 = "SELECT id FROM usuarios (id, nombre, apellido, usuario, correo, clave)  VALUES ('" + id + "', '" +  nombre +  "', '"  + apellido  + "', '" +  usuario +  "', '" +  correo +  "', '" +  clave +  "');"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(strsql)
    con.commit()
    con.close()

def sql_delete_usuarios(id):
    id = str(id)
    strsql = "DELETE FROM usuarios WHERE id = '" + id + "';"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(strsql)
    con.commit()
    con.close()

@app.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    if  request.method == "GET": #Si la ruta es accedida a través del método GET entonces
        form = Producto() #Crea un nuevo formulario de tipo producto
        return render_template('nuevo.html', form=form) #redirecciona vista nuevo.html enviando la variable form
    if  request.method == "POST": #Si la ruta es accedida a través del método POST entonces
	    cod = request.form["codigo"] #captura vble cod enviada a través del formulario en la vista html
	    nom = request.form["nombre"] #captura vble nom enviada a través del formulario en la vista html
	    cant = request.form["cantidad"] #captura vble cant enviada a través del formulario en la vista html
	    sql_insert_producto(cod, nom, cant) #llamado de la función para insertar el nuevo producto
    return "OK"


@app.route('/edit', methods=['GET'])
def editar_producto():
    id = request.args.get('id') #captura de la variable id enviada a través de la URL
    codigo = request.args.get('codigo') #captura de la vble código enviada a través de la URL
    nombre = request.args.get('nombre') #captura de la vble nombre enviada a través de la URL
    cantidad = request.args.get('cantidad') #captura de la vble cantidad enviada a través de la URL
    sql_edit_producto(id, codigo, nombre, cantidad) #llamado de la función de edición de la base de datos
    return "OK"


@app.route('/delete', methods=['GET'])
def borrar_producto():
	id = request.args.get('id') #captura de la variable id enviada a través de la URL
	sql_delete_producto(id) #llamado a la función de borrado de la base de datos
	return "OK"
