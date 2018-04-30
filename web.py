from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
from http import HTTPStatus

import os
import psycopg2
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug("INIT")

PORT = os.environ.get('PORT', 8000)
WORLD = os.environ.get('WORLD', "")
PG_CHECK = os.environ.get('PG_CHECK', "False") == "True"

logger.debug(f"{PORT}, {WORLD}")


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(f'Hello, {WORLD}!'.encode())
        # logger.debug(f"req served")
        return


def run(server_class=HTTPServer, handler_class=MyHandler):
    server_address = ('0.0.0.0', PORT)
    httpd = server_class(server_address, handler_class)

    try:
        logger.debug(f"Server works on http://localhost:{PORT}")
        httpd.serve_forever()
    except:
        logger.debug(f"Server stopped")
        httpd.socket.close()


def test_postgres_connection():
    try:
        connection = psycopg2.connect(
            database="postgres",
            user="postgres",
            host="db"
        )

        cur = connection.cursor()
        cur.execute('SELECT 1')
        logger.debug("Postgres - OK")
    except psycopg2.OperationalError:
        logger.critical(f"Postgres not ready! PG_CHECK - {PG_CHECK}")

        if PG_CHECK:
            exit(1)


if __name__ == '__main__':
    logger.debug("__main__")
    test_postgres_connection()
    run()