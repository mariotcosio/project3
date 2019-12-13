#Import all my dependencies at once
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

<<<<<<< HEAD
#Create an engine for the `hawaii.sqlite` database
engine = create_engine("sqlite:///Resources/wild_life.sqlite")
=======
from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.ext.automap import automap_base
>>>>>>> 74af9ecb1e743a662d8bcbb4b0c2587e53ef1415

#Create the base for sqlalchemy
Base = automap_base()
Base.prepare(engine, reflect=True)

#Save the tables into variables
status = Base.classes.status

#Create the session
session = Session(engine)

#Create the app
app = Flask(__name__)

<<<<<<< HEAD
@app.route("/index")
def index():
    #Displays a homepage menu
    return "this is a test"
=======
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Resources/wild_life.db"
>>>>>>> 74af9ecb1e743a662d8bcbb4b0c2587e53ef1415

@app.route("/api/test")
def stations():
    #Queries and prints all the station names
    session = Session(engine)
    test = session.query(status.IUCN, status.SPEC, status.COU, status.Value).all()
    return jsonify(test)

<<<<<<< HEAD

'''class Wild_Life(db.Model):
    __tablename__ = "Wild_Life"
    id = db.Column(db.Integer, primary_key=True)
    iucn = db.Column(db.String(255))
    spec = db.Column(db.String(255))
    cou = db.Column(db.String(255))
    value = db.Column(db.String(255))
=======
status = db.Table('status', db.metadata, autoload=True, autoload_with=db.engine)

@app.route('/assests/critical')
def index():
    results = db.session.query(status).all()
    for r in results:
        print(r.SPEC)
>>>>>>> 74af9ecb1e743a662d8bcbb4b0c2587e53ef1415

    return ''

<<<<<<< HEAD
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
'''
import sqlite3
from flask import g

DATABASE = '/SQL/wild_life.db'
=======
@app.route("/api/test")
def test():
    test = db.sessions.query(status,IUCN, status.SPEC, status.COU, status.Value).all()
    return jsonify(test)

>>>>>>> 74af9ecb1e743a662d8bcbb4b0c2587e53ef1415


app.run()