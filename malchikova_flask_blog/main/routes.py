from flask import render_template, Blueprint
from malchikova_flask_blog.models import User

# Initialization of the Blueprint (application framework)
main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html')
