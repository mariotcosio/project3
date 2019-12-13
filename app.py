#Import all my dependencies at once
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#Create an engine for the `hawaii.sqlite` database
engine = create_engine("sqlite:///SQL/wild_life.db")

#Create the base for sqlalchemy
Base = automap_base()
Base.prepare(engine, reflect=True)

#Save the tables into variables
Measure = Base.classes.Wild_Life

#Create the session
session = Session(engine)

#Create the app
app = Flask(__name__)

print(db)

class Wild_Life(db.Model):
    __tablename__ = "Wild_Life"
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
    results = db.session.query(Wild_Life.STATUS, Wild_Life.spec, Wild_Life.cou, Wild_Life.value).all()
    test = []
    print(results)

    for result in results:
        test.append({
            "iucn": result[0],
            "spec": result[1],
            "coun": result[2],
            "valu": result[3]
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
