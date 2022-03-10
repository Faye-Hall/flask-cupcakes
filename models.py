"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import ForeignKey

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    """Cupcake"""

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)

    flavor = db.Column(db.Text, nullable = False)

    size = db.Column(db.Text, nullable = False)

    rating = db.Column(db.Float, nullable = False)

    image = db.Column(db.Text, nullable = False, default = "https://tinyurl.com/demo-self")

    def serialize(self):
        """Serialize a dessert SQLAlchemy object model"""
    
        return {
        "id": self.id,
        "flavor": self.flavor,
        "size": self.size,
        "rating": self.rating,
        "image": self.image
        }