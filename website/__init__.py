from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'bero_123'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mr_lol_12@localhost/users'
    db.init_app(app)
    
    
    from .views import views
    from .auth import auth
    # Check if the database exists and create all tables if not
    with app.app_context():
        db.create_all()
    login_manger = LoginManager()
    login_manger.login_view = 'auth.login'
    login_manger.init_app(app)
    @login_manger.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    from .models import User, Note
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app
