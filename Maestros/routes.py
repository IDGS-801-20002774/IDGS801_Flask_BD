from flask import Flask, Blueprint, request, redirect, url_for, render_template, flash
from flask_sqlalchemy import SQLAlchemy
import forms
from db import *

db = SQLAlchemy()

maestros = Blueprint('maestros', __name__)

@maestros.route('/maestro', methods=['GET', 'POST'])
def maestro():
    create_form = forms.MaestroForm(request.form)

    if (request.method == 'POST'):
        nombre = create_form.nombre.data
        ape_paterno = create_form.ape_paterno.data
        ape_materno = create_form.ape_materno.data
        espec = create_form.especialidad.data
        correo = create_form.correo.data
        tel = create_form.telefono.data

        agregar_maestro(nombre, ape_paterno, ape_materno, espec, correo, tel)

        message ="¡El registro del maestro {} {} {} se guardó de manera exitosa!".format(nombre, ape_paterno, ape_materno)
        flash(message)

        return redirect(url_for('maestros.registros_maestros'))

    return render_template('maestro.html', form = create_form)


@maestros.route('/registros-maestros', methods=['GET', 'POST'])
def registros_maestros():
    create_form = forms.MaestroForm(request.form)
    registros = consultar_maestros()

    print(len(registros))

    return render_template('registros_maestros.html', form = create_form, registros = registros)


@maestros.route("/modificar-maestro", methods=['GET', 'POST'])
def modificar():
    create_form = forms.MaestroForm(request.form)
    
    if (request.method == 'GET'):
        id = request.args.get('id')
        maestro = consultar_maestro(id)
        create_form.id.data = id
        create_form.nombre.data = maestro[0][1]
        create_form.ape_paterno.data = maestro[0][2]
        create_form.ape_materno.data = maestro[0][3]
        create_form.especialidad.data = maestro[0][4]
        create_form.correo.data = maestro[0][5]
        create_form.telefono.data = maestro[0][6]

    if (request.method == 'POST'):
        id = create_form.id.data
        nombre = create_form.nombre.data
        ape_paterno = create_form.ape_paterno.data
        ape_materno = create_form.ape_materno.data
        espec = create_form.especialidad.data
        correo = create_form.correo.data
        tel = create_form.telefono.data
        actualizar_maestro(nombre, ape_paterno, ape_materno, espec, correo, tel, id)

        message ="¡El registro del maestro {} {} {} se actualizó de manera exitosa!".format(nombre, ape_paterno, ape_materno)
        flash(message)
        
        return redirect(url_for('maestros.registros_maestros'))
    
    return render_template('modificar_maestro.html', form = create_form)


@maestros.route("/eliminar-maestro", methods=['GET', 'POST'])
def eliminar():
    create_form = forms.MaestroForm(request.form)
    
    if (request.method == 'GET'):
        id = request.args.get('id')
        maestro = consultar_maestro(id)
        create_form.id.data = id
        create_form.nombre.data = maestro[0][1]
        create_form.ape_paterno.data = maestro[0][2]
        create_form.ape_materno.data = maestro[0][3]
        create_form.especialidad.data = maestro[0][4]
        create_form.correo.data = maestro[0][5]
        create_form.telefono.data = maestro[0][6]

    if (request.method == 'POST'):
        id = create_form.id.data
        nombre = create_form.nombre.data
        ape_paterno = create_form.ape_paterno.data
        ape_materno = create_form.ape_materno.data
        eliminar_maestro(id)

        message ="¡El registro del maestro {} {} {} se eliminó de manera exitosa!".format(nombre, ape_paterno, ape_materno)
        flash(message)
        
        return redirect(url_for('maestros.registros_maestros'))
    
    return render_template('eliminar_maestro.html', form = create_form)