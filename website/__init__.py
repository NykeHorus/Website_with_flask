from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
<<<<<<< HEAD
from flask_login import LoginManager
=======
>>>>>>> 022ef345da09b8407efbb019c3840aaa35c0036d

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '123'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
<<<<<<< HEAD
    
    
=======
>>>>>>> 022ef345da09b8407efbb019c3840aaa35c0036d
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, Url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, Note
    
<<<<<<< HEAD
    
    with app.app_context():
        db.create_all()
        
    Login_manager = LoginManager()
    Login_manager.login_view = 'auth.login'
    Login_manager.init_app(app)
    
    @Login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
=======
    with app.app_context():
        db.create_all()
>>>>>>> 022ef345da09b8407efbb019c3840aaa35c0036d
    
    return app
