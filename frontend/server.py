from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class MyHTTPRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()

if __name__ == '__main__':
    os.chdir('/app')
    server = HTTPServer(('0.0.0.0', 3000), MyHTTPRequestHandler)
    print('Server running on http://0.0.0.0:3000')
    server.serve_forever()
