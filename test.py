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
