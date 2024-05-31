from . import db
from flask_login import UserMixin
from uuid import uuid4
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    data = db.Column(db.String(100000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.String, db.foreignKey('user.id'))
    


class User(db.Model, UserMixin):
    id = db.Column(db.String(36), primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    firstName = db.Column(db.String(150), nullable=False)
    notes = db.relationship('Note')