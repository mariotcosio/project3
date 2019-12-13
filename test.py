'''
#Import all my dependencies at once
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#Create an engine for the `hawaii.sqlite` database
engine = create_engine("sqlite:///Resources/wild_life.sqlite")

#Create the base for sqlalchemy
Base = automap_base()
Base.prepare(engine, reflect=True)

#Save the tables into variables
status = Base.classes.status

#Create the session
session = Session(engine)

#Create the app
app = Flask(__name__)

@app.route("/index")
def index():
    #Displays a homepage menu
    return "this is a test"

@app.route("/api/test")
def stations():
    #Queries and prints all the station names
    session = Session(engine)
    test = session.query(status.IUCN, status.SPEC, status.COU, status.Value).all()
    return jsonify(test)
'''
import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#################################################
# Database Setup
#################################################

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Resources/wild_life.sqlite"
db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
status = Base.classes.status

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/names")
def names():
    """Return a list of sample names."""

    # Use Pandas to perform the sql query
    stmt = db.session.query(status).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Return a list of the column names (sample names)
    return jsonify(list(df.columns)[2:])


