from flask import Blueprint

# Create the "main" blueprint
main = Blueprint('main', __name__)


@main.route('/')
def home():
    return "Welcome to the start of your cookbook creation I provide the recipes and music then the rest is up to you!"
