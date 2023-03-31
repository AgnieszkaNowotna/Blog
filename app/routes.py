from flask import render_template, request, redirect,url_for, flash
from app.models import Entry, add_or_edit_entry
from app.forms import EntryForm
from app import app, db

@app.route('/')
def home():
    posts = Entry.query.filter_by(is_published = True).order_by(Entry.publish_date.desc())
    return render_template("home.html", posts = posts)

@app.route('/add', methods = ['GET', 'POST'])
def add_post():
    return add_or_edit_entry(entry_id = None)
  
@app.route('/edit/<int:entry_id>', methods = ['GET', 'POST'])
def edit_entry(entry_id):
    return add_or_edit_entry(entry_id)
