from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://nelly:nelly@localhost:3306/nelly'
app.config['SQLALCHEMY_ECHO'] = True
app.secret_key= "nelly"
