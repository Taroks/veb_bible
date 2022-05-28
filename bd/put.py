from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from create import books, authors, genres, book_author, book_genre, author_genre
import re
from flask import Flask

class putting():
    def __init__(self):
            app = Flask(__name__)
            app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Ощлук171@localhost:8888/Books"
            self.db = SQLAlchemy(app)
            migrate = Migrate(app, self.db)

    def put_book(self, inp):
        resultat = re.split(r", ", inp)
        data = {'name':resultat[0], 'author':resultat[1], 'genre':resultat[2], 'description':resultat[3]}
        new = books(name=data['name'], author=data['author'], genre=data['genre'], description = data['description'])
        self.db.session.add(new)
        self.db.session.commit()
        author = self.put_author(resultat[1], new.id)
        genre = self.put_genre(resultat[2],new.id)
        self.put_author_genre(author, genre)
        return {"message": f"book '{new.name}' has been created successfully."}


    def put_author(self,inp, book_id):
        resultat = re.split(r" ", inp)
        exists = self.db.session.query(self.db.exists().where(authors.last_name == resultat[1])).scalar()
        if exists == False:
            data = {'first_name':resultat[0], 'last_name':resultat[1]}
            new = authors(first_name=data['first_name'], last_name=data['last_name'])
            self.db.session.add(new)
            self.db.session.commit()
            self.put_book_author(book_id, new.id)
            return new.id
        else:
            result = self.db.session.query(authors).filter(authors.last_name==resultat[1])
            for row in result:
                self.put_book_author(book_id, row.id)
                return row.id


    def put_genre(self,inp,book_id):
        exists = self.db.session.query(self.db.exists().where(genres.name == inp)).scalar()
        if exists == False:
            data = {'name':inp}
            new = genres(name=data['name'])
            self.db.session.add(new)
            self.db.session.commit()
            self.__annotations__put_book_genre(book_id,new.id)
            return new.id
        else:
            result = self. db.session.query(genres).filter(genres.name==inp)
            for row in result:
                self.put_book_genre(book_id,row.id)
                return row.id

    def put_book_author(self, book_id, author_id):
        data = {'id_book':book_id,'id_author':author_id}
        new = book_author(id_book=data['id_book'],id_author=data['id_author'])
        self.db.session.add(new)
        self.db.session.commit()

    def put_book_genre(self, book_id, genre_id):
        data = {'id_book':book_id,'id_genre':genre_id}
        new = book_genre(id_book = data['id_book'], id_genre = data['id_genre'])
        self.db.session.add(new)
        self.db.session.commit()

    def put_author_genre(self, author_id, genre_id):
        data = {'id_author':author_id,'id_genre':genre_id}
        new = author_genre(id_author = data['id_author'], id_genre = data['id_genre'])
        self.db.session.add(new)
        self.db.session.commit()
    

# горе от ума, Лев толстой, роман, блаблабла
# Горе от ума, Александр Грибоедов, комедия, бла бла бла
# Обыкновенные истории, Александр Грибоедов, комедия, бла бла бла
