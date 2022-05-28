from sqlite3 import Row
from unittest import result
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from create import books, authors, genres, book_author, book_genre
import re
import json
from flask import Flask


class deleting():
    def __init__(self):
        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Ощлук171@localhost:8888/Books"
        self.db = SQLAlchemy(app)
        migrate = Migrate(app, self.db)

    def delete_book(self,nam):
        book = self.db.session.query(books).filter(books.name==nam)
        for row in book:
            self.db.session.delete(row)
            self.db.session.commit()

    def delete_author(self,nam):
        resultat = re.split(r" ", nam)
        author = self.db.session.query(authors).filter(authors.last_name==resultat[1])
        for row in author:
            bookz = self.db.session.query(book_author).filter(book_author.id_author==row.id)
            for row_0 in bookz:
                book = self.db.session.query(books).filter(books.id==row_0.id_book)
                for row_1 in book:
                    self.db.session.delete(row)
                    self.db.session.delete(row_0)
                    self.db.session.delete(row_1)
                    self.db.session.commit()

    def delete_genre(self,nam):
        genre = self.db.session.query(genres).filter(genres.name==nam)
        for row in genre:
            bookz = self.db.session.query(book_genre).filter(book_genre.id_genre==row.id)
            for row_0 in bookz:
                book = self.db.session.query(books).filter(books.id==row_0.id_book)
                for row_1 in book:
                    self.db.session.delete(row)
                    self.db.session.delete(row_0)
                    self.db.session.delete(row_1)
                    self.db.session.commit()
                

