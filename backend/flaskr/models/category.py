from backend.flaskr.db import db


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String)

    def __init__(self, type: str) -> None:
        self.type = type

    def format(self):
        return {
            'id': self.id,
            'type': self.type
        }
