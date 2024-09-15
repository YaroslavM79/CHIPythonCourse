from app.resources.app_creator import AppCreator


if __name__ == '__main__':
    app_creator = AppCreator()
    app = app_creator.get_app()
    app.run(debug=True)
