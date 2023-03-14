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
    id = IntegerField('Id:', [
        validators.DataRequired(message = '¡El campo es requerido!'),
    ], render_kw={"readonly": True})
    nombre = StringField('Nombre(s):', [
        validators.DataRequired(message = '¡El campo es requerido!')
    ])
    ape_paterno = StringField('Apellido paterno:', [
        validators.DataRequired(message = '¡El campo es requerido!')
    ])
    ape_materno = StringField('Apellido materno:', [
        validators.DataRequired(message = '¡El campo es requerido!')
    ])
    especialidad = StringField('Especialidad:', [
        validators.DataRequired(message = '¡El campo es requerido!')
    ])
    correo = EmailField('Correo:', [
        validators.DataRequired(message = '¡El campo es requerido!')
    ])
    telefono = StringField('Teléfono:', [
        validators.Length(min = 10, max = 10),
        validators.DataRequired(message = '¡El campo es requerido!')
    ])