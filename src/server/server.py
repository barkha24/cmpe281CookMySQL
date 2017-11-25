#!/usr/bin/env python

import BaseHTTPServer
import os

APP_PORT = 8084
AWS_ACCESS_ID = os.environ.get( 'AWS_ACCESS_ID' )
AWS_SECRET_KEY = os.environ.get( 'AWS_SECRET_KEY' )

assert AWS_ACCESS_ID and AWS_SECRET_KEY, 'Please set AWS keys'

class Application( BaseHTTPServer.BaseHTTPRequestHandler ):
   '''
   Basic HTTP Server
   '''
   def _headers( self ):
      self.send_header( 'Access-Control-Allow-Origin', '*' )
      self.send_header( 'Access-Control-Allow-Methods', 'OPTIONS, POST, GET, DELETE' )
      self.send_header( 'Access-Control-Allow-Headers', 'Content-type' )
      self.send_header( 'Access-Control-Allow-Headers', 'Content-length' )

   def do_POST( self ):
      ''' Handle POST request '''
      self.send_response( 200 )
      self.send_header( 'Content-type', 'text/html' )
      self._headers()
      self.end_headers()
      self.wfile.write('')

   def do_GET( self ):
      ''' Handle GET request '''
      self.send_response( 200 )
      self.send_header( 'Content-type', 'text/html' )
      self._headers()
      self.end_headers()
      self.wfile.write('')

   def do_DELETE( self ):
      ''' Handle DELETE request '''
      self.send_response( 200 )
      self.send_header( 'Content-type', 'text/html' )
      self._headers()
      self.end_headers()

   def do_OPTIONS( self ):
      ''' Handle OPTIONS request '''
      self.send_response( 200 )
      self.send_header( 'Content-type', 'text/html' )
      self._headers()
      self.end_headers()

if __name__ == '__main__':
   BaseHTTPServer.HTTPServer( ( '', APP_PORT ), Application ).serve_forever()
