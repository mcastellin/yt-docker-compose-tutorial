from app import db
from datetime import datetime


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), index=True, unique=True)
    ingredients = db.Column(db.UnicodeText())
    directions = db.Column(db.UnicodeText())
    createdts = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return "<Recipe {}>".format(self.name)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(256), index=True, unique=True)
    email = db.Column(db.String(256), index=True, unique=True)
    name = db.Column(db.String(256), index=True)
    surname = db.Column(db.String(256), index=True)

    def __rep__(self):
        return "<User {}>".format(self.uid)
