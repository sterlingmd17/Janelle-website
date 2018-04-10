from flask import Flask, request, redirect, render_template, session, flash
from models import Recipe, app

@app.route('/', methods=['POST', 'GET'])
def index():

    #create variables a, b, c to inject active menu highlight on nav bar.
    a = 'active'

    recipes = Recipe.query.all()

    return render_template("index.html", a=a, recipes=recipes)


if __name__ == '__main__':
    app.run()