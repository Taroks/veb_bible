from unittest import result
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from create import books, authors, genres, book_author, book_genre
import re
import json
from flask import Flask

class getting():
    def __init__(self):
        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Ощлук171@localhost:8888/Books"
        self.db = SQLAlchemy(app)
        migrate = Migrate(app, self.db)

    def get_book(self, nam):
        book = self.db.session.query(books).filter(books.name==nam)
        for row in book:
            response = {
                "name": row.name,
                "author": row.author,
                "genre": row.genre,
                "descritption": row.description
            }
            return response

    def get_author(self, nam):
        bookes = []
        resultat = re.split(r" ", nam)
        author = self.db.session.query(authors).filter(authors.last_name==resultat[1])
        for row in author:
            bookz = self.db.session.query(book_author).filter(book_author.id_author==row.id)
            for row_0 in bookz:
                book = self.db.session.query(books).filter(books.id==row_0.id_book)
                for row_1 in book:
                    bookes.append(row_1.name)
                    response = {
                        "first_name":row.first_name,
                        "last_author": row.last_name,
                        "books": bookes
                    }
                    return response

    def get_genre(self, nam):
        bookes = []
        genre = self.db.session.query(genres).filter(genres.name==nam)
        for row in genre:
            bookz = self.db.session.query(book_genre).filter(book_genre.id_genre==row.id)
            for row_0 in bookz:
                 book = self.db.session.query(books).filter(books.id==row_0.id_book)
                 for row_1 in book:
                    bookes.append(row_1.name)
                    response = {
                        "name":row.name,
                        "books": bookes
                    }
                    return response

    def get_all(self):
        bookz = books.query.all()
        results = [
            {
                "name": book.name,
                "author": book.author,
                "genre": book.genre,
                "description": book.description
            } for book in bookz]

        return results

check = getting()
print(check.get_genre('повесть'))

