from app.resources.db import db

__all__ = ['Role']


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)

    users = db.relationship('User', backref='role', lazy=True)

    @classmethod
    def get_all(cls):
        """Get all roles."""
        return cls.query.all()

    @classmethod
    def find_by_id(cls, role_id):
        """Find a role by its ID."""
        return cls.query.get(role_id)

    def save_to_db(self):
        """Save the role to the database."""
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        """Delete the role from the database."""
        db.session.delete(self)
        db.session.commit()
