#!/usr/bin/env python

from urlparse import urlparse, parse_qs
import api
import BaseHTTPServer
import os
import json

AWS_ACCESS_ID = os.environ.get( 'AWS_ACCESS_ID' )
AWS_SECRET_KEY = os.environ.get( 'AWS_SECRET_KEY' )

assert AWS_ACCESS_ID and AWS_SECRET_KEY, 'Please set AWS keys'

def warningErr( err ):
   if err:
      print '\033[91m' + err + '\033[0m'

def marshall( info, err ):
   warningErr( err )
   return json.dumps({ 'error' : err, 'info' : info })

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
      self.wfile.write( 'Test POST' )

   def do_GET( self ):
      ''' Handle GET request '''
      self.send_response( 200 )
      self.send_header( 'Content-type', 'text/html' )
      self._headers()
      query = urlparse( self.path ).query
      path =  urlparse( self.path ).path
      params = { k:v[0] for k,v in parse_qs( query ).items() }
      self.end_headers()
      err, response = api.api( path, params )
      print response
      self.wfile.write( marshall( response, err ) )

   def do_DELETE( self ):
      ''' Handle DELETE request '''
      self.send_response( 200 )
      self.send_header( 'Content-type', 'text/html' )
      self._headers()
      self.end_headers()
      self.wfile.write( 'Test DELETE' )

   def do_OPTIONS( self ):
      ''' Handle OPTIONS request '''
      self.send_response( 200 )
      self.send_header( 'Content-type', 'text/html' )
      self._headers()
      self.end_headers()
      self.wfile.write( 'Test OPTIONS' )

