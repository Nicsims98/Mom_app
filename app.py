from flask import Flask

DEBUG_MODE = True  # Toggle debugging mode for development and production


def create_app():
    """
    Create and configure the Flask application.
    """
    app = Flask(__name__)  # Initialize the Flask app

    # Register blueprints
    register_blueprints(app)

    return app


def register_blueprints(app):
    """
    Register all app blueprints.
    """
    # Import blueprints
    from mom_project.main import main as main_blueprint
    from mom_project.recipe import recipe as recipe_blueprint

    # Register blueprints with URL prefixes
    app.register_blueprint(main_blueprint, url_prefix="/")  # Root-level routes
    app.register_blueprint(recipe_blueprint, url_prefix="/recipe")  # Routes under '/recipe'

    # Additional blueprints can be registered here as the app grows
    # Example: app.register_blueprint(another_blueprint, url_prefix="/another")


if __name__ == "__main__":
    # Run the application
    app = create_app()
    app.run(debug=DEBUG_MODE)
