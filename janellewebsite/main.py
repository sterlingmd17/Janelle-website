from flask import Flask, request, redirect, render_template, session, flash
from app import app
from models import Recipe

@app.route('/', methods=['POST', 'GET'])
def index():

    #create variables a, b, c to inject active menu highlight on nav bar.
    a = 'active'

    recipes = Recipe.query.all()

    return render_template("testttt.html", a=a, recipes=recipes)

@app.route('/recipe', methods=['GET'])
def recipe():

    recipeid=int(request.args.get("id"))
    arecipe= Recipe.query.filter_by(id=recipeid)

    return render_template("recipe display.html", recipe=arecipe)



if __name__ == '__main__':
    app.run()