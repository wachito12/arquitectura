# models/paciente.py

from utils.db import db

class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    clave = db.Column(db.String(50), nullable=False)

    def __init__(self, nombre, apellido, email, clave):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.clave = clave
