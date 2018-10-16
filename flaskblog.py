from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)


posts = [
    {
        'author': 'Pranoto Budi',
        'title': 'Title 1',
        'content': "Content 1",
        'date_posted': 'August 10, 2018',
    },
    {
        'author': 'Dwi Hendro',
        'title': 'Title 2',
        'content': "Content 2",
        'date_posted': 'August 11, 2018',
    },
]


@app.route("/")
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
