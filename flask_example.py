from flask import Flask

app = Flask(__name__)

l = []


@app.route('/')
def yo():
    return '<h2>Yo<h2>'


@app.route('/add/<username>')
def add_str(username):
    l.append(username)
    return '<h2>The string is %s<h2>' % username


@app.route('/release')
def concatenate():
    a = "".join(l)
    return '<h2>The concatenated string is %s<h2>' % a


if __name__ == '__main__':
    app.run(debug=True)
