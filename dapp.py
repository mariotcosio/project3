# import necessary libraries
import os

import sqlite3
from flask import g
import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import (
    Flask,
    render_template,
    jsonify,
    request)

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Resources/wild_life.db"

db = SQLAlchemy(app)

# reflect an existing database into a new model
db.Model.metadata.reflect(db.engine)

# Save references to each table
#Samples_Metadata = Base.classes.sample_metadata
#Samples = Base.classes.samples

class Wild_Life(db.Model):
    __tablename__ = 'status'
    __table_args__ = { 'extend_existing': True }  

@app.route("/api/data")
def list_status():
    results = db.session.query(Wild_Life.iucn, Wild_Life.spec, Wild_Life.cou, Wild_Life.value).all()

    status = []
    print(results)

    for result in results:
        test.append({
            "iucn": result[0],
            "spec": result[1],
            "coun": result[2],
            "value": result[3]
        })
    return jsonify(status)

@app.route('/list')
def list():
   con = sql.connect("Resources/wl.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from Wild_Life")
   
   rows = cur.fetchall();
   return render_template("list.html",rows = rows)


@app.route("/a")
def home():
    print("total number of items is", Wild_Life.query.count())
    return "Welcome!"

@app.route("/")
def index():
    """Return the homepage."""
    return "Hello!"

if __name__ == "__main__":
    app.run()
'''
import sqlite3
from flask import g

DATABASE = '/SQL/wild_life.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
'''
