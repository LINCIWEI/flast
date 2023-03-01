import flask
from flask import Flask

app = Flask(__name__)
from faker import Faker
def fstory():
    mystory = "是大家打架啊四大萨斯哦"
    return mystory
@app.route('/')
def index():
    mystory = fstory()
    return  flask.render_template("index.html",story=mystory)

if __name__ == '__main__':
    app.run()