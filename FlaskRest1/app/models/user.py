from app.models.role import Role
from app.resources.db import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)

    role_users = db.relationship('Role', backref=db.backref('role_users', lazy='dynamic'))

    def __init__(self, username, password, role_id):
        self.username = username
        self.set_password(password)
        self.role_id = role_id

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @classmethod
    def get_all_users(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, user_id):
        return cls.query.get(user_id)

    @classmethod
    def get_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'role_id': self.role_users.name if self.role_users else None
        }

    def save_to_db(self):
        """Save the user to the database"""
        db.session.add(self)
        db.session.commit()

    def update_in_db(self, **kwargs):
        """Update the user's data in the database"""
        if 'username' in kwargs:
            self.username = kwargs['username']
        if 'password' in kwargs:
            self.set_password(kwargs['password'])
        if 'role_id' in kwargs:
            self.role_id = kwargs['role_id']
        db.session.commit()

    def delete_from_db(self):
        """Delete the user from the database"""
        db.session.delete(self)
        db.session.commit()
