import os

from flask import Flask, render_template
from flask_mongoengine import MongoEngine


def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ['SECRET_KEY']
    return app


def config_db(app):
    app.config['MONGODB_SETTINGS'] = {
        'host': '172.19.0.2',
    }
    db = MongoEngine(app)
    return app, db


def register_routes(app):
    from app.routes import blueprints
    for blue in blueprints:
        app.register_blueprint(blue)
    return app


app = create_app()
app, db = config_db(app)
app = register_routes(app)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
