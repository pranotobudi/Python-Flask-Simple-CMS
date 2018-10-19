from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#import secrets
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a9705bdad25a1836d4c5d849dd028ecb'
# print(secrets.token_hex(16))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes
