from flask import render_template, session, request, redirect,url_for, flash
from app.models import Entry, add_or_edit_entry, login_required
from app.forms import LoginForm
from app import app, db

@app.route('/')
def home():
    posts = Entry.query.filter_by(is_published = True).order_by(Entry.publish_date.desc())
    return render_template("home.html", posts = posts)

@app.route('/add', methods = ['GET', 'POST'])
@login_required
def add_post():
    return add_or_edit_entry(entry_id = None)
  
@app.route('/edit/<int:entry_id>', methods = ['GET', 'POST'])
@login_required
def edit_entry(entry_id):
    return add_or_edit_entry(entry_id)

@app.route('/drafts')
@login_required
def list_drafts():
    posts = Entry.query.filter_by(is_published = False).order_by(Entry.publish_date.desc())
    return render_template("list_drafts.html", posts = posts)

@app.route("/login", methods = ["GET", "POST"])
def login():
    form = LoginForm()
    errors = None
    next_url = request.args.get("next")
    if request.method == "POST":
        if form.validate_on_submit():
            session['logged_in'] = True
            session.pernament = True
            flash("You're logged in.", 'success')
            return redirect (next_url or url_for('home'))
        else:
            errors = form.errors
    return render_template("login_form.html", form = form, errors = errors)

@app.route("/logout", methods = ['GET','POST'])
def logout():
    if request.method == "POST":
        session.clear()
        flash('You are now logged out.', 'success')
    return redirect(url_for('home'))
    