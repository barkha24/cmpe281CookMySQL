from server import server
import BaseHTTPServer

APP_PORT = 8084

if __name__ == '__main__':
   BaseHTTPServer.HTTPServer( ( '', APP_PORT ), server.Application ).serve_forever()
