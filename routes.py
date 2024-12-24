from flask import Blueprint

# Import blueprints from other modules
from mom_project.main import main as main_blueprint
from mom_project.recipe import recipe as recipe_blueprint

# Optionally add more blueprints later here, e.g.,
# from mom_project.another_module import another_blueprint

# Organize blueprints in a list for easy registration
blueprints = [
    (main_blueprint, '/'),  # Blueprint, URL prefix for `main`
    (recipe_blueprint, '/recipe')  # Blueprint, URL prefix for `recipe`
]
