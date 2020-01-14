import socket
from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
from decider import decide_type

#virtualenv v.16.1.0.
#install with pyinstaller --onefile --hidden-import=pyttsx3.drivers --hidden-import=pyttsx3.drivers.sapi5 remote_server.py
#Put dist exe in the same directory as of regex
#For no console:

def runserver():

    class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

        def do_GET(self):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Hello, world!')

        def do_POST(self):
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            query = body.decode('utf-8')
            res = decide_type(query)
            try:
                res = res.encode()
            except:
                res = b'We are still working on ambiguous apps remote execution. Thank you for you patience.'
            print(res, type(res))
            self.send_response(200)
            self.end_headers()
            response = BytesIO()
            # response.write(b'This is POST request. ')
            # response.write(b'Received: ')
            response.write(res)
            self.wfile.write(response.getvalue())

    class CORSRequestHandler(SimpleHTTPRequestHandler):
        def end_headers(self):
            self.send_header('Access-Control-Allow-Origin', '*')
            SimpleHTTPRequestHandler.end_headers(self)

    httpd = HTTPServer((get_ip_address(), 16286), SimpleHTTPRequestHandler, CORSRequestHandler)
    httpd.serve_forever()



def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

if __name__ == "__main__":
    runserver()
