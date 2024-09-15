from sqlalchemy import MetaData

from app.resources.db import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    # password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'admin', 'editor', 'viewer'
    articles = db.relationship('Article', backref='author', lazy='dynamic')

    @classmethod
    def get_all_users(cls):
        """Get all users"""
        return cls.query.all()

    @classmethod
    def get_user_by_id(cls, user_id):
        """Get user by user_id"""
        return cls.query.get(user_id)


    # def set_password(self, password):
    #     self.password_hash = generate_password_hash(password)
    #
    # def check_password(self, password):
    #     return check_password_hash(self.password_hash, password)
