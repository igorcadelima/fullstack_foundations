from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class WebserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            output = ""
            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output += "<html><body>Hello!</body></html>"
                self.wfile.write(output)
            elif self.path.endswith("/hola"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output += "<html><body>&#161Hola! <a href='/hello'>Back to Hello</a></body></html>"
                self.wfile.write(output)
                print output
        except IOError:
            self.send_error(404, "File Not Found %s" % self.path)

def main():
    try:
        port = 8080
        server_address = ('', port)
        server = HTTPServer(server_address, WebserverHandler)
        print("Web server running on port %s" % port)
        server.serve_forever()

    except KeyboardInterrupt:
        print("^C entered, stopping web server...")
        server.socket.close()

if __name__ == '__main__':
    main()
