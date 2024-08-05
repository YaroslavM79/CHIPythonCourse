from app.models.article import Article
from app.resources.db import db


class ArticleService:
    @staticmethod
    def get_all_articles():
        return [article.to_dict() for article in Article.query.all()]

    @staticmethod
    def get_article_by_id(article_id):
        article = Article.query.get(article_id)
        if article:
            return article.to_dict()
        return None

    @staticmethod
    def create_article(data):
        new_article = Article(
            title=data['title'],
            content=data['content'],
            author_id=data['author_id']
        )
        db.session.add(new_article)
        db.session.commit()
        return new_article.to_dict()

    @staticmethod
    def update_article(article_id, data):
        article = Article.query.get(article_id)
        if article:
            article.title = data['title']
            article.content = data['content']
            db.session.commit()
            return article.to_dict()
        return None

    @staticmethod
    def delete_article(article_id):
        article = Article.query.get(article_id)
        if article:
            db.session.delete(article)
            db.session.commit()
            return True
        return False
