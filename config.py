import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET_KEY = os.environ.get("SECRET_KEY") or "secret"
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DATABASE_URL") or
        'sqlite:///' + os.path.join(BASE_DIR, 'mikroblog.db')
    )
    
    SQLALCHEMY_TARCK_MODIFICATIONS = False