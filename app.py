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

@app.route("/api/test")
def test():
    test = db.session.query(status).all()
    results = db.session.execute("SELECT * FROM status where iucn in ('VULNERABLE', 'CRITICAL', 'ENDANGERED', 'THREATENED')")
    data=[]
    for result in results:
        data.append([result[0],result[1],result[2],result[3]]) 
    return jsonify(test)

@app.route("/api/vulnerable")
def vulnerable():
    results = db.session.execute("SELECT * FROM status where iucn='VULNERABLE' and spec in ('MAMMAL','BIRD', 'REPTILE') ")
    vulnerable = []
    for result in results:
        vulnerable.append({
            "cou": result[0],
            "spec": result[1],
            "icun": result[2],
            "value": result[3],
           
        })
    return jsonify(vulnerable)

@app.route("/api/critical")
def critical():
    results = db.session.execute("SELECT * FROM status where iucn='CRITICAL' and spec in ('MAMMAL','BIRD', 'REPTILE') ")
    critical = []
    for result in results:
         critical.append({
            "cou": result[0],
            "spec": result[1],
            "icun": result[2],
            "value": result[3],
           
        })
    return jsonify(critical)

@app.route("/api/threatened")
def threatened():
    results = db.session.execute("SELECT * FROM status where iucn='THREATENED' and spec in ('MAMMAL','BIRD', 'REPTILE') ")
    threatened = []
    for result in results:
        threatened.append({
            "cou": result[0],
            "spec": result[1],
            "icun": result[2],
            "value": result[3],
           
        })
    return jsonify(threatened)

@app.route("/api/endangered")

def endangered():
    results = db.session.execute("SELECT * FROM status where iucn='ENDANGERED' and spec in ('MAMMAL','BIRD', 'REPTILE') ")
    endangered = []
    for result in results:
        endangered.append({
            "cou": result[0],
            "spec": result[1],
            "icun": result[2],
            "value": result[3],
           
        })
    return jsonify(endangered)





app.run(host="0.0.0.0", debug=True) 
