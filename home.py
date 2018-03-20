from flask import Flask, render_template
import pymongo

app = Flask(__name__)


@app.route('/')
def begin():
    return render_template('home.html')


app.run(host='localhost', port='5000')
