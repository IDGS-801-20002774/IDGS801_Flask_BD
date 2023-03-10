from wtforms import Form
from wtforms import StringField, IntegerField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    id = IntegerField('id')
    nombre = StringField('nombre')
    apellidos = StringField('apellidos')
    email = EmailField('correo')

class MaestroForm(Form):
    id = IntegerField('Id:')
    nombre = StringField('Nombre:')
    apellidos = StringField('Apellidos:')
    especialidad = StringField('Especialidad:')
    correo = EmailField('Correo:')
    telefono = StringField('Telefono:')