from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Alumnos(db.Model):
    __tablename__ = 'alumnos'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    apellidos = db.Column(db.String(100))
    email = db.Column(db.String(50))
    create_date = db.Column(db.DateTime, default = datetime.datetime.now)