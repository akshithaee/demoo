from flask import Flask, render_template




@app.route('/')
def home():
    return render_template('index.html')

app = Flask(__name__)
if __name__ == "__main__":
    app.run(debug=True)