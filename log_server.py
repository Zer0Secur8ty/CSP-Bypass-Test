from http.server import BaseHTTPRequestHandler, HTTPServer

class Logger(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"[+] Incoming: {self.path}")
        self.send_response(200)
        self.end_headers()

HTTPServer(('0.0.0.0', 9000), Logger).serve_forever()
