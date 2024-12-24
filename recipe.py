from flask import Blueprint

# Define the 'recipe' blueprint
recipe = Blueprint("recipe", __name__)


# Route for the base of the recipe blueprint
@recipe.route("/")
def recipe_home():
    return "Welcome to the Start of Making your Own Cookbook!"


# Route for displaying recipe information
@recipe.route("/info")
def recipe_info():
    return (
        "Here is some recipe information! "
        "They will be random every day, so make sure to write down the ones you like!"
    )
