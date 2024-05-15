from flask import Flask
from os import environ

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello🌱'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=environ.get('PORT'), debug=environ.get('DEBUG'))