from . import db
import datetime as dt
from app.forms import EntryForm

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable = False)
    body = db.Column(db.Text, nullable = False)
    publish_date = db.Column(db.DateTime, nullable = False, default = dt.datetime.utcnow())
    is_published = db.Column(db.Boolean, default = False)

def add_entry(data):
    entry = Entry(
        title = data['title'],
        body = data['body'],
        is_published = data['is_published']
    )
    db.session.add(entry)
    db.session.commit()


