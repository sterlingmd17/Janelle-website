from enum import Enum
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import *
from sqlalchemy.ext.mutable import MutableDict
from app import app

db = SQLAlchemy(app)


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    description = db.Column(db.String(500))
    ingredients = db.relationship("Ingredients", backref=("recipe"), lazy=True)
    directions = db.Column(db.String(500))
    imagesrc = db.Column(db.String(500))
    public = db.Column(db.Boolean, default=False)

    def __init__(self, name, description, directions, imagesrc):
        self.name = name
        self.description = description
        self.directions = directions
        self.imagesrc = imagesrc


# Measurement type enum for defining types of measurements for drop down menu
class MeasType(Enum):
    CUP = "Cup"
    TABLESPOON = "Tablespoon"
    TEASPOON = "Teaspoon"
    PINT = "Pint"
    QUART = "Quart"
    GALLON = "Gallon"


class Ingredients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipe.id"))
    name = db.Column(db.String(100))
    amount = db.Column(db.Integer)
    measurement_type = db.Column(db.Enum(MeasType))
