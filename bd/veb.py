from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask, jsonify
from flask import render_template, request
from put import putting
from delete import deleting
from get import getting
import re

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Ощлук171@localhost:8888/Books"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/input', methods=['GET', 'POST'])
def input():
    message = ''
    if request.method == 'POST':
        input = request.form.get('input')
        if input != '':
            resultat = re.split(r", ", input)
            if len(resultat)!=4:
                message = 'Неверно введены данные '
            else:
                print(type(input), input)
                put = putting()
                put.put_book(input)
                message = 'Книга успешно добавлена'
        else:
            delete_name = request.form.get('delete_name')
            if delete_name != '':
                delete = deleting()
                delete.delete_book(delete_name)
                message = 'Книга успешно удалена'
            else:
                delete_author = request.form.get('delete_author')
                if delete_author !='':
                    delete = deleting()
                    delete.delete_author(delete_author)
                    message = f'Книги автора {delete_author} успешно удалены'
                else:
                    delete_genre = request.form.get('delete_genre')
                    if delete_genre != '':
                        delete = deleting()
                        delete.delete_genre(delete_genre)
                        message = f'Книги жанра {delete_genre} успешно удалены'
    return render_template('index.html', message = message)

@app.route('/output', methods=['Get','POST'])
def output():
    otvet = ''
    get = getting()
    if request.method == 'POST':
        input = request.form.get('get_name')
        if input != '':
            otvet = get.get_book(input)
        else:
            get_author = request.form.get('get_author')
            if get_author != '':
                otvet = get.get_author(get_author)
            else:
                get_genre = request.form.get('get_genre')
                if get_genre !='':
                    print(input)
                    otvet = get.get_genre(get_genre)

    return render_template('index2.html', otvet = otvet)

@app.route('/all', methods = ['GET', 'POST'])
def all():
    get = getting()
    return render_template('index3.html', otvet = get.get_all())

