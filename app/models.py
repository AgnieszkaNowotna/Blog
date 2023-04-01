from . import db
from flask import request, render_template, redirect, url_for, flash
from app.forms import EntryForm
import datetime as dt

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable = False)
    body = db.Column(db.Text, nullable = False)
    publish_date = db.Column(db.DateTime, nullable = False, default = dt.datetime.utcnow())
    is_published = db.Column(db.Boolean, default = False)

def add_or_edit_entry(entry_id):
    errors = None

    if entry_id == None:
        form = EntryForm()
    else:
        entry = Entry.query.filter_by(id=entry_id).first_or_404()
        form = EntryForm(obj=entry)

    if request.method == "POST":
        if form.validate_on_submit():
            if entry_id == None:
                entry = Entry(
                    title = form.data['title'],
                    body = form.data['body'],
                    is_published = form.data['is_published']
                    )
                db.session.add(entry)
                flash("New entry has been added")
            else:
                form.populate_obj(entry)
                flash("Entry has been updated") 
        else:
            errors = form.errors
        db.session.commit()

        return redirect(url_for('home'))
    
    return render_template("entry_form.html", form = form)