from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .views import views
from .auth import auth
from .models import User, Note
from os import path
DB_MAME = 'mysql://root:mr_lol_123@localhost/testdatabase'
db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'bero_123'
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_MAME
    db.init_app(app)
    
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    create_database(app)
    return app
def create_database(app):
    if not path.exists('website/' + DB_MAME):
        db.create_all(app=app)
        print('Database Created!')