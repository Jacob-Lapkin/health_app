from flask import Flask, redirect, render_template, jsonify, request, url_for, session
from flask_bcrypt import Bcrypt, generate_password_hash, check_password_hash

from flask_sqlalchemy import SQLAlchemy
from itsdangerous import json 
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, create_access_token
from models import db, User

app = Flask(__name__)
db.init_app(app)
bcrypt = Bcrypt()

app.config['SECRET_KEY'] = "asdsdanjdanjsda"


@app.route('/register')
def register():
    first = request.json('first')
    last = request.json('last')
    email = request.json('email')
    password = request.json('password')
    if first and last and email and password:
        new_user = User.query.filter_by(email = email).first()
        if new_user:
            return jsonify(message = "user already registered"), 409
        if not new_user:
            hashed_password = bcrypt.generate_password_hash(password)
            user = User(first=first, last=last, email=email, password=password)
            db.session.add(user)
            db.session.commit()
            return jsonify(message = "user registered"), 201




if __name__ == "__main__":
    app.run()