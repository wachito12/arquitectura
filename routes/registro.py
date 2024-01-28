from flask import Blueprint, render_template, request, redirect, url_for, flash
from utils.db import db
from models.paciente import Paciente

pacientes = Blueprint('pacientes', __name__)

@pacientes.route('/')
def home():
    mostrar_lista = request.args.get('mostrar_lista', False) == 'True'

    if mostrar_lista:
        pacientes_list = Paciente.query.all()
        return render_template('index.html', registro=pacientes_list)
    else:
        return render_template('index.html', registro=[])

@pacientes.route('/new', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        clave = request.form['clave']

        if not name or not apellido or not email or not clave:
            flash('Todos los campos son obligatorios. Por favor, complete todos los campos.', 'error')
        else:
            new_paciente = Paciente(nombre=name, apellido=apellido, email=email, clave=clave)
            db.session.add(new_paciente)
            db.session.commit()
            flash('Registro creado correctamente.', 'success')
        return redirect(url_for('pacientes.home', mostrar_lista=False, success_message='Registro creado correctamente.'))
    
    flash('Por favor, complete todos los campos.', 'error')
    return redirect(url_for('pacientes.home', mostrar_lista=False))

@pacientes.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_contact(id):
    paciente = Paciente.query.get(id)

    if not paciente:
        flash('Paciente no encontrado.', 'error')
        return redirect(url_for('pacientes.home'))

    if request.method == 'POST':
        paciente.nombre = request.form['nombre']
        paciente.apellido = request.form['apellido']
        paciente.email = request.form['email']
        paciente.clave = request.form['clave']
        db.session.commit()
        flash('Registro actualizado correctamente.', 'success')
        return redirect(url_for('pacientes.ver_lista'))

    return render_template('update.html', paciente=paciente)

@pacientes.route('/delete/<int:id>', methods=['POST'])
def delete_contact(id):
    paciente = Paciente.query.get(id)

    if paciente:
        db.session.delete(paciente)
        db.session.commit()
        flash('Registro eliminado correctamente.', 'success')
    else:
        flash('Paciente no encontrado.', 'error')

    # Redirige a la misma página después de la eliminación
    return redirect(request.referrer)

@pacientes.route('/ver-lista')
def ver_lista():
    pacientes_list = Paciente.query.all()
    return render_template('lista_pacientes.html', registro=pacientes_list)
