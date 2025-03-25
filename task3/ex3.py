from flask import Flask, url_for, request, render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<title>')
def index(title):
    content = {
        'title': f'{title}',
        'text1': 'Миссия Колонизация Марса',
        'text2': 'И на Марсе будут яблони цвести!'
    }
    return render_template("base.html",
                           **content)


@app.route('/training/<prof>')
def training(prof):
    return render_template("list.html",
                           prof=f'{prof}')


@app.route('/list_prof/<list>')
def list_prof(list):
    return render_template("list.html",
                           list=list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
