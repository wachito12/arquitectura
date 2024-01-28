# app.py
from flask import Flask
from routes.registro import pacientes
from utils.db import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:Samsungh.w@localhost:3306/registropacientes"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "Samsungh.w"

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(pacientes)

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
