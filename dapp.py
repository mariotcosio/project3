# import necessary libraries
import os

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

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Resources/wl.db"

db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
#Samples_Metadata = Base.classes.sample_metadata
#Samples = Base.classes.samples

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/names")
def names():
    """Return a list of sample names."""

    # Use Pandas to perform the sql query
    stmt = db.session.query(Samples).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Return a list of the column names (sample names)
    return jsonify(list(df.columns)[2:])


class wild_life(db.Model):
    __tablename__ = "wild_life"
    id = db.Column(db.Integer, primary_key=True)
    iucn = db.Column(db.String(255))
    spec = db.Column(db.String(255))
    cou = db.Column(db.String(255))
    value = db.Column(db.String(255))

    def __repr__(self):
        return '<%r>' % (self.cou)

@app.before_first_request
def setup():
    # Recreate database each time for demo
    db.drop_all()
    db.create_all()

@app.route("/api/data")
def list_pets():
    results = db.session.query(wild_life.iucn, wild_life.spec, wild_life.cou, wild_life.value).all()

    test = []
    print(results)

    for result in results:
        test.append({
            "iucn": result[0],
            "spec": result[1],
            "coun": result[2],
            "value": result[3]
        })
    return jsonify(test)

@app.route("/")
def home():
    return "Welcome!"


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
