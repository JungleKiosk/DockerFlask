from flask import Flask, render_template
from os import environ

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home/home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=environ.get('PORT'), debug=environ.get('DEBUG'))