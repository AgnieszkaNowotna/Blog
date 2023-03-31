from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask import Flask
from faker import Faker

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
fake = Faker()

from . import routes, models

@app.shell_context_processor
def make_shell_context():
    return{
        "db":db,
        "Entry":models.Entry
    }