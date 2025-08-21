from http.server import BaseHTTPRequestHandler, HTTPServer
import socket

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html = f"""
        <html>
            <body>
                <h1>Hello World</h1>
                <p><strong>Hostname:</strong> {hostname}</p>
                <p><strong>IP Address:</strong> {ip_address}</p>
            </body>
        </html>
        """
        self.wfile.write(html.encode("utf-8"))

if __name__ == "__main__":
    server_address = ("", 8080)
    httpd = HTTPServer(server_address, HelloHandler)
    print("Servidor rodando na porta 8080...")
    httpd.serve_forever()
