import json

from flask import Flask, url_for, request, render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/answer')
def answer():
    auto = {'surname': 'Watny', 'name': 'Mark', 'education': 'выше среднего', 'professoin': 'штурман марсохода',
              'sex': 'male', 'motivation': 'Всегда мечтал застрять на Марсе!', 'ready': True, 'href': url_for('static', filename='css/style.css')}
    return render_template('auto_answer.html', **auto)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
