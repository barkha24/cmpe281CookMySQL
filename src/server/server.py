#!/usr/bin/env python

import BaseHTTPServer

class HTTPHandler( BaseHTTPServer.BaseHTTPRequestHandler ):
   '''
   Basic HTTP Server
   '''
   def do_POST( self ):
      ''' Handle POST request '''
      pass

   def do_GET( self ):
      ''' Handle GET request '''
      pass

   def do_DELETE( self ):
      ''' Handle DELETE request '''
      pass

   def do_OPTIONS( self ):
      ''' Handle OPTIONS request '''
      pass
