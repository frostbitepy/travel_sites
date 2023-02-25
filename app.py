from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'empanada'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
#To redirect not logged in users to the log in page use this python code:
login_manager.login_view = 'login'



import routes, models