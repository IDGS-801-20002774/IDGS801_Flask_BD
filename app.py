from flask import Flask, render_template, redirect, url_for, jsonify, request
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from models import db
from Maestros.routes import maestros
from Alumnos.routes import alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

app.register_blueprint(maestros)
app.register_blueprint(alumnos)

if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.run(port = 3000)