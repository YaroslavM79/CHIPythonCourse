from app.resources.db import db
from datetime import datetime


class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Relationship to User
    author = db.relationship('User', backref=db.backref('articles', lazy='dynamic'))

    @classmethod
    def get_all_articles(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, article_id):
        return cls.query.get(article_id)

    @classmethod
    def get_by_author(cls, author_id):
        return cls.query.filter_by(author_id=author_id).all()

    def save_to_db(self):
        """Save the article to the database"""
        db.session.add(self)
        db.session.commit()

    def update_in_db(self, **kwargs):
        """Update the article's data in the database"""
        for key, value in kwargs.items():
            setattr(self, key, value)
        db.session.commit()

    def delete_from_db(self):
        """Delete the article from the database"""
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'created_at': self.created_at.isoformat(),
            'author_id': self.author_id,
            'author_username': self.author.username if self.author else None
        }
