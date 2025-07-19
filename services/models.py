from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

def current_date_str():
    return datetime.now().strftime('%d-%m-%Y')

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)
    date = db.Column(db.String(10), default=current_date_str, nullable=False)

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(120), nullable=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=True)
    resume_path = db.Column(db.String(256), nullable=True)
    date = db.Column(db.String(10), default=current_date_str, nullable=False) 