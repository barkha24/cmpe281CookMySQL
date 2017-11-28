#!/usr/bin/env python
from hashlib import sha256
import datetime

from backend import rds_wrapper

hour = datetime.datetime.now().strftime("%Y-%m-%d %H")
SALT = 'RECIPE'

def hashPassword( password, username ):
   return sha256( password + username + SALT ).hexdigest()

class Token( object ):
   '''
   Token is generated if token string is not set (usually to give
   back to the caller). If token string is set, it can be used
   to authenticate a user.
   '''
   def __init__( self, username, password='', token='', valid=1 ):
      self.username = username
      con = rds_wrapper.connect_mysql()
      self.valid = valid
      self.created = datetime.datetime.now()
      if token:
         self.token_ = token
      else:
         user = rds_wrapper.User( con, self.username, strict=True )
         password = hashPassword( password, username )
         assert user.verifyPassword( password ), 'Incorrect password'
         self.token_ =  sha256( user.password + hour ).hexdigest()

   def userId( self ):
      con = rds_wrapper.connect_mysql()
      user = rds_wrapper.User( con, self.username, strict=True )
      return user.id

   def token( self ):
      return self.token_

   def until( self ):
      hour = self.created + datetime.timedelta( hours = self.valid )
      return '{}'.format( hour )

   def isValid( self ):
      con = rds_wrapper.connect_mysql()
      user = rds_wrapper.User( con, self.username, strict=True )
      valid = False
      for i in range( self.valid ):
         hour = (datetime.datetime.now() - datetime.timedelta( hours = i )).strftime("%Y-%m-%d %H")
         testSha = sha256( user.password + hour ).hexdigest()
         if ( self.token_ == testSha  ):
            return True
      if not valid:
         return False
