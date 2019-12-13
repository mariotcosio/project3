import os
# import necessary libraries
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    send_from_directory)
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.ext.automap import automap_base

app = Flask(__name__, static_folder = 'static')
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Resources/wild_life.db"

db = SQLAlchemy(app)

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

    return jsonify(results)

@app.route("/api/test")
def test():
    test = db.sessions.query(status.IUCN, status.SPEC, status.COU, status.Value).all()
    return jsonify(test)



app.run(host="0.0.0.0")