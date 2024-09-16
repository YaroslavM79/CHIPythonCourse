SYSTEM_APP_BLUEPRINTS = {
    # "app.api.version_info",
    # "app.api.healthcheck",
}

SUPPORTED_APP_V1_BLUEPRINTS = {
    '/users': 'app.api.v1.users.ApiUsers',
    '/user/<int:user_id>': 'app.api.v1.user.UserResources',
    '/articles': 'app.api.v1.articles.ArticleResources',
    '/article/<int:article_id>': 'app.api.v1.article.ArticleResources',

}
