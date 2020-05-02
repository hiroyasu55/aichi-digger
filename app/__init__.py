from flask import Flask
import os
from app.controllers.home import app_home
from app.controllers.persons import app_persons
from app.controllers.tree import app_tree
from app.controllers.summary import app_summary

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config')
app.config.from_pyfile('secret.cfg')

app.secret_key = os.urandom(12)

app.register_blueprint(app_home)
app.register_blueprint(app_persons)
app.register_blueprint(app_tree)
app.register_blueprint(app_summary)
