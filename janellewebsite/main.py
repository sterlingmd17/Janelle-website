from flask import Flask, request, redirect, render_template, session, flash
from models import app

@app.route('/', methods=['POST', 'GET'])
def index():
    a = 'active'
    b = 'inactive'
    c = 'inactive'
    return render_template("test.html", a=a, b=b, c=c, )

if __name__ == '__main__':
    app.run()