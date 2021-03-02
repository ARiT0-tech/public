from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    title = 'mars'
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    title = 'mars'
    prof_list = prof.lower()
    return render_template('base.html', title=title, prof_list=prof_list)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
