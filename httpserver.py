"""Quick local Python HTTP server that allows JS localhost fetches.

Blackened from https://stackoverflow.com/a/21957017/4376000.

Only use for dev purposes!

Run with, e.g.:

$ python3.11 httpserver.py 8100

"""

from http.server import HTTPServer, SimpleHTTPRequestHandler, test
import sys


class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        SimpleHTTPRequestHandler.end_headers(self)


if __name__ == "__main__":
    test(
        CORSRequestHandler,
        HTTPServer,
        port=int(sys.argv[1]) if len(sys.argv) > 1 else 8000,
    )
