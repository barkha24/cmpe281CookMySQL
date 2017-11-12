#!/usr/bin/env python

import os
import MySQLdb

MYSQL_HOST = 'cmpe281p2db.cmqx6tpknayx.us-east-2.rds.amazonaws.com'
MYSQL_USER = 'root'
MYSQL_DB = 'cook'
MYSQL_PASS = os.getenv( 'MYSQL_PASS', None )


def connect_mysql():
   assert MYSQL_PASS, 'MYSQL_PASS env variable not set'
   return MySQLdb.connect( host=MYSQL_HOST,
                          user=MYSQL_USER,
                          passwd=MYSQL_PASS,
                          db=MYSQL_DB )

class User( object ):
   '''
   User represents the user object uploading, modifying and accessing the
   recipe information.
   '''
   def __init__( self, con, username='', id=0 ):
      cur = con.cursor()
      select = "SELECT * from User where username=\"%s\" or id=%d"
      insert = "INSERT into User ( username ) values (\"%s\")"
      while True:
         cur.execute( select % ( username, id ) )
         results = [ entry for entry in cur ]
         if results:
            self.id, self.username, self.dateCreated = results[0]
            break
         else:
            cur.execute( insert % username )
      self.active = True

   def __repr__( self ):
      assert self.active, 'Object is no longer accessible'
      output = ''
      output += 'User ID: {}\n'.format( self.id )
      output += 'Username: {}\n'.format( self.username )
      output += 'Date Created: {}'.format( self.dateCreated )
      return output

   def usernameIs( self, username ):
      assert self.active, 'Object is no longer accessible'
      self.username = username

   def save( self, con ):
      assert self.active, 'Object is no longer accessible'
      cur = con.cursor()
      update = 'UPDATE User set username = \"%s\" where id=%d'
      cur.execute( update % ( self.username, self.id ) )
      con.commit()

   def delete( self, con, username='', id=0 ):
      assert self.active, 'Object is no longer accessible'
      cur = con.cursor()
      delete = "DELETE from User where id=%d"
      cur.execute( delete % self.id )
      self.active = False
      con.commit()

class Recipe( object ):
   '''
   Recipe class represents a single recipe the user can upload, modify or delete
   '''
   def __init__( self, con, ownerId, id=0, title='' ):
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

   def __repr__( self ):
      assert self.active, 'Object is no longer accessible'
      output = ''
      output += 'User ID: {}'.format( self.id )
      output += 'Title: {}'.format( self.title )
      output += 'Created On: {}'.format( self.createdOn )
      return output

   def delete( self, con, username='', id=0 ):
      assert self.active, 'Object is no longer accessible'
      cur = con.cursor()
      delete = "DELETE from Recipe where id=%d"  
      cur.execute( delete % self.id )
      self.active = False
