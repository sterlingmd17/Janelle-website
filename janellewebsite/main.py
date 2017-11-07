from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://nelly:nelly@localhost:3306/nelly'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key= "nelly"

@app.route('/', methods=['POST', 'GET'])
def index():
    # index will have rolling slideshow of linkable pictures of recipes.
    return render_template("index.html")

if __name__ == '__main__':
    app.run()