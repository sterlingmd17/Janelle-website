from flask import Flask, request, redirect, render_template, session, flash
from models import app, Recipe,

@app.route('/', methods=['POST', 'GET'])
def index():

    #create variables a, b, c to inject active menu highlight on nav bar.
    a = 'active'
    b = 'inactive'
    c = 'inactive'

    arecipe = Recipe.

    return render_template("index.html", a=a, b=b, c=c, )

if __name__ == '__main__':
    app.run()