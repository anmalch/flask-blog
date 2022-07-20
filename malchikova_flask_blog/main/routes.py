from flask import render_template, Blueprint
from malchikova_flask_blog.models import User

#инициализация Blueprint (каркас приложения)
main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html')
