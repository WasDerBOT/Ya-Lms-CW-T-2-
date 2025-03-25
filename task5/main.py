from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/login')
def login():
    return render_template('login.html', param=url_for('static', filename='img/MARS.png'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
