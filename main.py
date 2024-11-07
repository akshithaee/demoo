from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/admin')
def admin():
    return 'hello admin'


@app.route('/user/<name>')
def user(name):
    return f"hello {name}"


@app.route('/guest/<name>')
def guest(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('user', name=name))


if __name__ == "__main__":
    app.run(debug=True)