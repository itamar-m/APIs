from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import json


class APIServer(BaseHTTPRequestHandler):

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        action = self.path[1:]

        self._set_response()

        if action == "GET_NAME":
            print(json.dumps({"name": "John"}))
            self.wfile.write(json.dumps({"name": "John"}).encode("utf-8"))
        elif action == "GET_ID":
            print(json.dumps({"id": 30}))
            self.wfile.write(json.dumps({"id": 30}).encode("utf-8"))
        elif action == "GET_ROLE":
            print(json.dumps({"role": "Developer"}))
            self.wfile.write(json.dumps({"role": "Developer"}).encode("utf-8"))
        elif action == "GET_PROFILE":
            print(json.dumps({"name": "John", "id": 30, "role": "Developer"}))
            self.wfile.write(json.dumps({"name": "John", "id": 30, "role": "Developer"}).encode("utf-8"))
        else:
            print(json.dumps({"error": 404, "message": "This action: " + action + " does not exists!"}))
            self.wfile.write(json.dumps({"error": 404, "message": "This action: " + action +
                                                                  " does not exists!"}).encode("utf-8"))

        # self._set_response()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                     str(self.path), str(self.headers), post_data.decode('utf-8'))

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))


def run(server_class=HTTPServer, handler_class=APIServer, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
    logging.info('Stopping httpd...\n')


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
