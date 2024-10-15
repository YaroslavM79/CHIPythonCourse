from app.resources.app_creator import AppCreator
from app.resources.db import db
from app.models import User, Article, Role

app = AppCreator().get_app()


def seed_roles():
    Role.create_roles()
    print("Roles seeded successfully.")


def seed_users():
    users_data = [
        {'username': 'admin', 'password': 'admin123', 'role_name': 'admin'},
        {'username': 'editor', 'password': 'editor123', 'role_name': 'editor'},
        {'username': 'viewer', 'password': 'viewer123', 'role_name': 'viewer'}
    ]

    for user_data in users_data:
        if User.get_by_username(user_data['username']):
            print(f"User '{user_data['username']}' already exists.")
            continue

        role = Role.get_by_name(user_data['role_name'])
        if not role:
            print(f"Role '{user_data['role_name']}' does not exist.")
            continue

        user = User(username=user_data['username'], password=user_data['password'], role_id=role.id)
        user.save_to_db()
        print(f"User '{user_data['username']}' created successfully.")


def seed_articles():
    articles_data = [
        {'title': 'Welcome to the blog', 'content': 'This is the first article', 'author_username': 'admin'},
        {'title': 'Editing Tips', 'content': 'Tips on how to edit articles', 'author_username': 'editor'}
    ]

    for article_data in articles_data:
        author = User.get_by_username(article_data['author_username'])
        if not author:
            print(f"Author '{article_data['author_username']}' does not exist.")
            continue

        existing_articles = Article.query.filter_by(title=article_data['title']).first()
        if existing_articles:
            print(f"Article '{article_data['title']}' already exists.")
            continue

        article = Article(title=article_data['title'], content=article_data['content'], author_id=author.id)
        article.save_to_db()
        print(f"Article '{article_data['title']}' created successfully.")


def run_seeding():
    print("Starting the seeding process...")
    seed_roles()
    seed_users()
    seed_articles()
    print("Seeding completed.")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        run_seeding()
