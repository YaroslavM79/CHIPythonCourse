from app.resources.server import create_app
from app.resources.db import db
from app.models import User, Article, Role

app = create_app()

with app.app_context():
    db.create_all()

    admin_role = Role(name='admin')
    editor_role = Role(name='editor')
    viewer_role = Role(name='viewer')

    admin_user = User(username='admin', email='admin@example.com', role=admin_role)
    editor_user = User(username='editor', email='editor@example.com', role=editor_role)
    viewer_user = User(username='viewer', email='viewer@example.com', role=viewer_role)

    article1 = Article(title='First Article', content='This is the first article.', author=admin_user)
    article2 = Article(title='Second Article', content='This is the second article.', author=editor_user)

    db.session.add(admin_role)
    db.session.add(editor_role)
    db.session.add(viewer_role)
    db.session.add(admin_user)
    db.session.add(editor_user)
    db.session.add(viewer_user)
    db.session.add(article1)
    db.session.add(article2)

    db.session.commit()
