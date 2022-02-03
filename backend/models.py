from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    first = db.Column(db.String(255))
    last = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))

