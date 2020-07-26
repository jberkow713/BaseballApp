from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Blueprint
import sqlite3
import pandas as pd 
import os
import json
import jsonify 
import sqlite3
import numpy as np 
from flask import Flask 



DATABASE_URI = "MLBdb.sqlite3"

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI


@app.route("/")
def about():
    return "Time to evaluate some players!"

@app.route("/player/<x>", methods=["GET","POST"])
def player(x):
    connection = sqlite3.connect("MLBdb.sqlite3")
    cursor = connection.cursor()
    player = f'''select PLAYER, hr, AB, salary , RBI, r , Tb   
    from mlb_table where PLAYER = '{x}';'''  

    r1 = cursor.execute(player)
    data = (r1.fetchall())
    df = pd.DataFrame(data, columns=[ 'Player','HR', 'AB','salary',
    'RBI', 'Runs', 'Total Bases'])

    result = df.to_json(orient='records')
    
    return result 

@app.route("/salary/<x>", methods=["GET", "POST"])
def salary(x):
    connection = sqlite3.connect("MLBdb.sqlite3")
    cursor = connection.cursor()
    salary = f'''select Avg(HR), AVG(AB), Avg(RBI), AVG(R), AVG(TB) from 
    mlb_table where salary > '{x}';'''
   
    r2 = cursor.execute(salary)
    data = (r2.fetchall())
    df = pd.DataFrame(data, columns=[ 'Avg HR', 'Avg AB', 'Avg RBI',
    'Avg R', 'Avg TB'])

    result = df.to_json(orient='records')
    return result 

@app.route("/productivity/<x>", methods=["GET", "POST"])
def productivity(x):
    connection = sqlite3.connect("MLBdb.sqlite3")
    cursor = connection.cursor()
    productivity = f'''select PLAYER, Avg(AB)/ (Avg(H) + Avg(RBI) + Avg(TB)) from 
    mlb_table WHERE PLAYER = '{x}';'''

    r3 = cursor.execute(productivity)
    data = (r3.fetchall())
    df = pd.DataFrame(data, columns=[ 'Player', 'Productivity'])

    result = df.to_json(orient='records')
    
    return result     


