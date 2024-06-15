import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///contacts.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app_config = Config
