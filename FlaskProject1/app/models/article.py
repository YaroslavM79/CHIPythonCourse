from app.resources.db import db

__all__ = ['Article']


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    author = db.relationship('User', backref='articles', lazy=True)

    @classmethod
    def get_all(cls):
        """Get all articles."""
        return cls.query.all()

    @classmethod
    def find_by_id(cls, article_id):
        """Find an article by its ID."""
        return cls.query.get(article_id)

    def save_to_db(self):
        """Save the article to the database."""
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        """Delete the article from the database."""
        db.session.delete(self)
        db.session.commit()
