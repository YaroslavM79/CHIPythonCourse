from app.models.user import User
from app.resources.db import db

__all__ = ['UserService']


class UserService:
    @staticmethod
    def get_all_users():
        return [user.to_dict() for user in User.query.all()]

    @staticmethod
    def get_user_by_id(user_id):
        user = User.query.get(user_id)
        if user:
            return user.to_dict()
        return None

    @staticmethod
    def create_user(data):
        new_user = User(
            username=data['username'],
            email=data['email'],
            role_id=data['role_id']
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user.to_dict()

    @staticmethod
    def update_user(user_id, data):
        user = User.query.get(user_id)
        if user:
            user.username = data['username']
            user.email = data['email']
            user.role_id = data['role_id']
            db.session.commit()
            return user.to_dict()
        return None

    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False
