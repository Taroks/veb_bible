from enum import unique
import flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Ощлук171@localhost:8888/Books"
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class books(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, unique=True, primary_key=True,  autoincrement=True)
    name = db.Column('name', db.String)
    author = db.Column('author', db.String)
    genre = db.Column('genre', db.String)
    description = db.Column('description', db.String)

    def __repr__(self):
        return "".format(self.code)


class genres (db.Model):
    __tablename__ = 'genres'

    id = db.Column(db.Integer, unique=True, primary_key=True,  autoincrement=True)
    name = db.Column('name', db.String, unique=True)

    def __repr__(self):
        return "".format(self.code)

class authors (db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, unique=True, primary_key=True,  autoincrement=True)
    first_name = db.Column('first_name', db.String)
    last_name = db.Column('last_name', db.String, unique=True)

    def __repr__(self):
        return "".format(self.code)

class book_genre(db.Model):
    __tablename__ = 'book_genre'

    id = db.Column(db.Integer, unique=True, primary_key=True,  autoincrement=True)
    id_book = db.Column(db.Integer, db.ForeignKey('books.id'))
    id_genre = db.Column(db.Integer,  db.ForeignKey('genres.id'))
    books = db.relationship(books, backref="quote_books")
    genres = db.relationship(genres, backref="quote_genres")

    def __repr__(self):
        return "".format(self.code)

class author_genre(db.Model):
    __tablename__ = 'author_genre'

    id = db.Column(db.Integer, unique=True, primary_key=True,  autoincrement=True)
    id_author = db.Column(db.Integer, db.ForeignKey('authors.id'))
    id_genre = db.Column(db.Integer, db.ForeignKey('genres.id'))
    authors = db.relationship(authors, backref="quote_authors")
    genres = db.relationship(genres, backref="genres")
   
    def __repr__(self):
        return "".format(self.code)


class book_author(db.Model):
    __tablename__ = 'book_author'

    id = db.Column(db.Integer, unique=True, primary_key=True,  autoincrement=True)
    id_book = db.Column(db.Integer, db.ForeignKey('books.id'))
    id_author = db.Column(db.Integer, db.ForeignKey('authors.id'))
    books = db.relationship(books, backref="books")
    authors = db.relationship(authors, backref="authors")
   
    def __repr__(self):
        return "".format(self.code)