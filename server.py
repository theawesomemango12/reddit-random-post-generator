from typing import NoReturn
from randompost import RandomPost
from flask import Flask, render_template, redirect
app = Flask(__name__)

randompost = RandomPost()

@app.route('/')
def index():
  return render_template('/index.html')

@app.route('/redirect/')
def my_link():
    randompost.get_random_post()
    return render_template('/index.html')

if __name__ == '__main__':
    app.run(debug=True)

