from flask import render_template, request, redirect,url_for, flash
from app.models import Entry, add_entry
from app.forms import EntryForm
from app import app

@app.route('/')
def home():
    posts = Entry.query.filter_by(is_published = True).order_by(Entry.publish_date.desc())
    return render_template("home.html", posts = posts)

@app.route('/add', methods = ['GET', 'POST'])
def add_post():
    form = EntryForm()
    errors = None
    if request.method == 'POST':
        if form.validate_on_submit():
            data = form.data
            add_entry(data)
            flash("New entry has been added")
        else:
            errors = form.errors
        return redirect(url_for('home'))
    
    return render_template("entry_form.html", form = form)

