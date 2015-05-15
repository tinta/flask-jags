from flask.ext.sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class BaseMixin(object):
    id =  db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    date_modified = db.Column(db.DateTime, default=datetime.datetime.utcnow())

class ToDoItem(db.Model, BaseMixin):
    __tablename__ = "teams"
    title = db.Column(db.String(500))
    details = db.Column(db.Text)
    due_date = db.Column(db.DateTime)
    done = db.Column(db.Boolean)
