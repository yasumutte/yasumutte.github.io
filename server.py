import sys
from http.server import SimpleHTTPRequestHandler, HTTPServer
from functools import partial

ROOT_DIR = './public'
HOST = '127.0.0.1'
PORT = 8000

def run(HandlerClass=SimpleHTTPRequestHandler,
        ServerClass=HTTPServer):
    HandlerClass.extensions_map.update({
        ".js": "text/javascript",
        ".wasm": "application/wasm",
    })
    httpd = ServerClass((HOST, PORT), partial(HandlerClass, directory=ROOT_DIR))

    sa = httpd.socket.getsockname()
    print("up", sa[0], "port", sa[1])
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('down', sa[0], "port", sa[1])
        sys.exit(0)


if __name__ == "__main__":
    run()
