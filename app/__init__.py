from flask import Flask
from flask import request
from flask import jsonify as flask_jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

class Project(db.Model):
  __tablename__ = 'projects'
  project = db.Column(db.String(255), primary_key=True)
  count  = db.Column(db.Integer)

  def __init__(self,project, count):
    self.project = project
    self.count = count



def jsonify(*args, **kwargs):
    response = flask_jsonify(*args, **kwargs)
    if not response.data.endswith(b'\n'):
        response.data += b'\n'
    return response

@app.route('/')
def index():
  return jsonify(origin=request.headers.get('X-Forwarded-For', request.remote_addr))

@app.route('/api/<project>')
def show_project(project):
  p =Project.query.filter_by(project=project).first()
  if p:
    p.count = p.count + 1
    db.session.add(p)
    db.session.commit()
    return str(p.count)
  else:
    p = Project(project, 1)
    db.session.add(p)
    db.session.commit()
    r = Project.query.filter_by(project=project).first()
    return str(r.count)

