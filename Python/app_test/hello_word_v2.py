from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
import os

try:
    import resource
except ImportError:
    resource = None

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)

        # Consumo de memória e CPU
        if resource:
            mem_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024  # em MB
            cpu_usage = resource.getrusage(resource.RUSAGE_SELF).ru_utime  # em segundos
        else:
            mem_usage = "N/A (Windows)"
            cpu_usage = "N/A (Windows)"

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html = f"""
        <html>
            <body>
                <h1>Hello World</h1>
                <p><strong>Hostname:</strong> {hostname}</p>
                <p><strong>IP Address:</strong> {ip_address}</p>
                <p><strong>Memoria usada:</strong> {mem_usage} MB</p>
                <p><strong>CPU usada:</strong> {cpu_usage} segundos</p>
            </body>
        </html>
        """
        self.wfile.write(html.encode("utf-8"))

if __name__ == "__main__":
    server_address = ("", 8585)
    httpd = HTTPServer(server_address, HelloHandler)
    print("Servidor rodando na porta 8585...")
    httpd.serve_forever()