import os 
import sys 
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    print(os.environ)
    return str(os.environ)