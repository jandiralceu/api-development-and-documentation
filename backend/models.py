from db import db

database_path = 'postgresql://{}/{}'.format('udacity:udacity2024@localhost:5432', 'trivia')


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

