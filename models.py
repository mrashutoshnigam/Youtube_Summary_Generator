from datetime import datetime

from app import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class VideoLib(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    video_url = db.Column(db.String(100))
    title = db.Column(db.String(200))
    summary = db.Column(db.String(5000))
    search_date = db.Column(db.DateTime, default=datetime.utcnow)
