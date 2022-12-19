from app import db
from datetime import datetime


class Author(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), index=True, nullable=True)
    surname = db.Column(db.String(20), index=True, nullable=True)
    birth = db.Column(db.String(15), index=True, nullable=True)
    books = db.relationship("Book", backref="author", lazy="dynamic")

    def __repr__(self):
        return f"{self.name} {self.surname}"


class Book(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), index=True, nullable=True)
    genre = db.Column(db.String(15), index=True, nullable=True)
    pages = db.Column(db.Integer, index=True, nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))

    stock = db.Column(db.Boolean, default=False)

    def __str__(self):
        return f"{self.title}"