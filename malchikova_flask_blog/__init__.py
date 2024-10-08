from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from malchikova_flask_blog.config import Config
from flask_mail import Mail

db = SQLAlchemy()
# Battery for client authorization
login_manager = LoginManager()
bcrypt = Bcrypt()
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(Config)
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)

    # Import the application object and register it
    from malchikova_flask_blog.main.routes import main
    from malchikova_flask_blog.users.routes import users
    from malchikova_flask_blog.posts.routes import posts
    from malchikova_flask_blog.errors.handlers import errors

    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(errors)


    return app
