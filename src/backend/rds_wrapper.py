#!/usr/bin/env python

import os

MYSQL_HOST = 'cmpe281p2db.cmqx6tpknayx.us-east-2.rds.amazonaws.com'
MYSQL_USER = 'root'
MYSQL_DB = 'cook'
MYSQL_PASS = os.getenv( 'MYSQL_PASS' )

class User( object ):
   '''
   User represents the user object uploading, modifying and accessing the
   recipe information.
   '''
   def __init__( self, username='', id=0, con ):
      cur = con.cursor()
      select = "SELECT * from User where username=\"%s\" or id=%d"
      insert = "INSERT into USER ( username ) values \"%s\"" 
      while True:
         cur.execute( select % ( username, id ) )
         results = [ entry for entry in cur ]
         if results:
            self.id, self.username, self.createdOn = results[0]
            break
         else:
            cur.execute( insert % username )
      self.active = True

   def print( self ):
      assert self.active, 'Object is no longer accessible'
      print 'User ID:', self.id
      print 'Username:', self.username
      print 'Date Created:', self.dateCreated

   def delete( self, username='', id=0, con ):
      assert self.active, 'Object is no longer accessible'
      cur = con.cursor()
      delete = "DELETE from USER where id=%d"
      cur.execute( delete % self.id )
      self.active = False

class Recipe( object ):
   '''
   Recipe class represents a single recipe the user can upload, modify or delete
   '''
   def __init__( self, ownerId, id=0, title='' ):
      assert ownerId, 'Owner for the Recipe object must be set'
      cur = con.cursor()
      while True:
         select = "SELECT * from Recipe where id=%d or title=%s"
         cur.execute( select % ( id, title ) )
         results = [ entry for entry in cur ]
         if results:
            self.id = results[0][0]
            self.title = results[0][1]
            self.ownerId = results[0][2]
            self.createdOn = results[0][3]
            self.updatedOn = results[0][4]
            self.bucket = results[0][5]
            break
         else:
            insert = "INSERT into Recipes (ownerId,title) values %s"
            cur.execute( insert % (ownerId, title) )
      self.active = True

   def print( self ):
      assert self.active, 'Object is no longer accessible'
      print 'User ID:', self.id
      print 'Title:', self.title
      print 'Created On:', self.createdOn

   def delete( self, username='', id=0, con ):
      assert self.active, 'Object is no longer accessible'
      cur = con.cursor()
      delete = "DELETE from Recipe where id=%d"  
      cur.execute( delete % self.id )
      self.active = False
