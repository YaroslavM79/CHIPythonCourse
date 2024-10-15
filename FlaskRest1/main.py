from app.resources.app_creator import AppCreator


def run_app():
    app_creator = AppCreator()
    return app_creator.get_app()


if __name__ == '__main__':
    app = run_app()
    app.run(debug=True)
