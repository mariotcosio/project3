# import necessary libraries
from flask import (
    Flask,
    render_template,
    jsonify,
    request)

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Resources\wild_life.db"

db = SQLAlchemy(app)

status = db.Table('status', db.metadata, autoload=True, autoload_with=db.engine)

@app.route('/w')
def index():
    results = db.session.query(Status).all()
    for r in results:
        print(r.SPEC)

    return ''


