import socket
from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
from decider import decide_type

#virtualenv v.16.1.0.
#install with pyinstaller --onefile --hidden-import=pyttsx3.drivers --hidden-import=pyttsx3.drivers.sapi5 --noconsole remote_server.py --icon=divi_logo.ico
#Put dist exe in the same directory as of regex
#For no console:

####################### Hosts http server on client machine to listen to remote requests ##########################

def runserver():

    class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

        ###### GET mode is made for testing purpose #######

        def do_GET(self):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Hello, world!')

        ###### Takes POST mode query data and initites decider on own device ######

        def do_POST(self):
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            query = body.decode('utf-8')
            if query == "YOU_WILL_NEVER_KNOW$*@#":
                res = "true"
            else:
                res = decide_type(query)
            try:
                res = res.encode()
            except:

                ############## Can't work on MultiMatch of application on remote device for now ##############

                res = b'We are still working on ambiguous apps remote execution. Thank you for you patience.'
            print(res, type(res))
            self.send_response(200)
            self.end_headers()
            response = BytesIO()
            # response.write(b'This is POST request. ')
            # response.write(b'Received: ')
            response.write(res)
            self.wfile.write(response.getvalue())

    ############# CORS enables httpserver connection with third party services, like DIVI ##############

    class CORSRequestHandler(SimpleHTTPRequestHandler):
        def end_headers(self):
            self.send_header('Access-Control-Allow-Origin', '*')
            SimpleHTTPRequestHandler.end_headers(self)

######################### Hosts Http Server at client machine on port no. 16286 ###########################

    httpd = HTTPServer((get_ip_address(), 16286), SimpleHTTPRequestHandler, CORSRequestHandler)
    httpd.serve_forever()



def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

if __name__ == "__main__":
    runserver()
