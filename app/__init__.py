# __init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import Session, sessionmaker
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)

# Config
app.config.from_object('config')

# SQL Alchemy
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Create Session
Session = sessionmaker()
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Session.configure(bind=engine)
session = Session()

from app import routes, models

if __name__ == "__main__":
    app.run()
