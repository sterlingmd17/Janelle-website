from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    description = db.Column(db.String(100))
    ingredients = db.Column(db.String(100))
    directions = db.Column(db.String(100))
    imagesrc = db.Column(db.String(100))
    public = db.Column(db.Boolean, default=False)

    def __init__(self, name, description, ingredients, directions, imagesrc):
        self.name= name
        self.description = description
        self.ingredients = ingredients
        self.directions = directions
        self.imagesrc = imagesrc
