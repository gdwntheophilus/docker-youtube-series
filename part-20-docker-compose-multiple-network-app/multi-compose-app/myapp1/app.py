import os 
import psycopg2
import json

import time
from flask import Flask

app = Flask(__name__)

def getDatabaseDate():
    conn = psycopg2.connect(
        host="mydb",
        database="dbadmin",
        user="dbadmin",
        password="postgres123")
    cur=conn.cursor()
    cur.execute("select now()")
    return cur.fetchall()

@app.route('/')
def hello():
    data = '{ "date":"' + str(getDatabaseDate())+'"}'
    return json.dumps(data)