import logging
import sys
import socket

from app.resources import create_app

app_logger = logging.getLogger("app.py")


def start_app():
    rest_app = create_app()

    cli = sys.modules['flask.cli']
    cli.show_server_banner = lambda *x: None

    ip_address = socket.gethostbyname(socket.gethostname())
    app_logger.info(f"======== REST service available at http://{ip_address}:{5000}/ ========")
    rest_app.run(host='0.0.0.0')


if __name__ == "__main__":
    start_app()
