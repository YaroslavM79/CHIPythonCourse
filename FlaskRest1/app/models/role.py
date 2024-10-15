from app.resources.db import db


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)

    users_role = db.relationship('User', backref='user_role', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_all_roles(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, role_id):
        return cls.query.get(role_id)

    @classmethod
    def get_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def create_role(cls, name):
        if cls.get_by_name(name):
            raise ValueError(f"Role '{name}' already exists")
        role = cls(name=name)
        db.session.add(role)
        db.session.commit()
        return role

    @classmethod
    def delete_role(cls, role_id):
        role = cls.get_by_id(role_id)
        if not role:
            return False
        db.session.delete(role)
        db.session.commit()
        return True

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }

    @classmethod
    def create_roles(cls):
        roles = ['admin', 'editor', 'viewer']
        for role_name in roles:
            try:
                cls.create_role(role_name)
            except ValueError:
                continue
