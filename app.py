<<<<<<< HEAD
<<<<<<< HEAD
import os
# import necessary libraries
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    send_from_directory)
from flask_cors import CORS
=======
=======
>>>>>>> 443f36adcf11d19f45e475b786a495cc9a21b7fe
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
<<<<<<< HEAD
>>>>>>> 443f36adcf11d19f45e475b786a495cc9a21b7fe
=======
>>>>>>> 443f36adcf11d19f45e475b786a495cc9a21b7fe
from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.ext.automap import automap_base
>>>>>>> 74af9ecb1e743a662d8bcbb4b0c2587e53ef1415

<<<<<<< HEAD
<<<<<<< HEAD
app = Flask(__name__, static_folder = 'static')
CORS(app)
=======
=======
>>>>>>> 443f36adcf11d19f45e475b786a495cc9a21b7fe
#Create the base for sqlalchemy
Base = automap_base()
Base.prepare(engine, reflect=True)

#Save the tables into variables
status = Base.classes.status

#Create the session
session = Session(engine)

#Create the app
app = Flask(__name__)
>>>>>>> 443f36adcf11d19f45e475b786a495cc9a21b7fe

<<<<<<< HEAD
@app.route("/index")
def index():
    #Displays a homepage menu
    return "this is a test"
=======
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Resources/wild_life.db"
>>>>>>> 74af9ecb1e743a662d8bcbb4b0c2587e53ef1415
<<<<<<< HEAD

@app.route("/api/test")
def stations():
    #Queries and prints all the station names
    session = Session(engine)
    test = session.query(status.IUCN, status.SPEC, status.COU, status.Value).all()
    return jsonify(test)

=======

@app.route("/api/test")
def stations():
    #Queries and prints all the station names
    session = Session(engine)
    test = session.query(status.IUCN, status.SPEC, status.COU, status.Value).all()
    return jsonify(test)

>>>>>>> 443f36adcf11d19f45e475b786a495cc9a21b7fe
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

@app.route('/')
def index():
    return app.send_static_file("index.html")

@app.route('/images/<path:filename>')
def serve_static_images(filename):
    return send_from_directory(os.path.join(".", 'static/images'), filename)

@app.route('/js/<path:filename>')
def serve_static_js(filename):
    return send_from_directory(os.path.join(".", 'static/js'), filename)

@app.route('/vulnerable')
def vulnerable():
    results = db.session.query(status).all()
    for r in results:
        print(r.SPEC)
>>>>>>> 74af9ecb1e743a662d8bcbb4b0c2587e53ef1415
<<<<<<< HEAD

    return jsonify(results)

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

=======
>>>>>>> 443f36adcf11d19f45e475b786a495cc9a21b7fe

if __name__ == "__main__":
    app.run()
'''
'''
import sqlite3
from flask import g

<<<<<<< HEAD
=======
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

>>>>>>> 443f36adcf11d19f45e475b786a495cc9a21b7fe
DATABASE = '/SQL/wild_life.db'
=======
@app.route("/api/test")
def test():
    test = db.sessions.query(status.IUCN, status.SPEC, status.COU, status.Value).all()
    return jsonify(test)

>>>>>>> 74af9ecb1e743a662d8bcbb4b0c2587e53ef1415


app.run(host="0.0.0.0")