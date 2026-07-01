import http.server
import os

class UTF8Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Force UTF-8 for text files
        ct = self.headers.get('Content-Type', '')
        if 'text/' in ct or ct == '' or '.md' in self.path or '.html' in self.path:
            self.send_header('Content-Type', f'{ct or "text/plain"}; charset=utf-8')
        super().end_headers()

os.chdir(r'E:\openhanako\story')
server = http.server.HTTPServer(('127.0.0.1', 18724), UTF8Handler)
print('Server on http://127.0.0.1:18724 (UTF-8)')
server.serve_forever()
