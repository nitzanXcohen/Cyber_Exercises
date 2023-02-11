from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def _send_response(self, message, status_code=200):
        self.send_response(status_code)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(message, "utf8"))

    def do_GET(self):
        try:
            params = list(map(int, self.path.split("/")[-1].split(",")))
            if self.path.startswith("/sum"):
                result = sum(params)
                message = f"The sum of {params} is: {result}"
                self._send_response(message)
            elif self.path.startswith("/average"):
                result = sum(params) / len(params)
                message = f"The average of {params} is: {result}"
                self._send_response(message)
            else:
                message = "Invalid request"
                self._send_response(message, status_code=404)
        except (ValueError, ZeroDivisionError):
            message = "Invalid parameters. Please provide numbers separated by ','"
            self._send_response(message, status_code=400)

def run(server_class=HTTPServer, handler_class=RequestHandler, port=80):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on port {port}")
    httpd.serve_forever()

run()
