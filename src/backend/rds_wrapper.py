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


def getRecipesForUser( con, user ):
   '''
   Return a list of recipe objects for the user
   '''
   cur = con.cursor()
   select = "SELECT * from Recipe where ownerId=%d"
   cur.execute( select % user.id )
   return [ RecipeForUser( *entry ) for entry in cur ]

class User( object ):
   '''
   User represents the user object uploading, modifying and accessing the
   recipe information.
   '''
   def __init__( self, con, username='', password='nopassword', id=0, strict=False ):
      cur = con.cursor()
      select = "SELECT * from User where username=\"%s\" or id=%d"
      insert = "INSERT into User ( username ) values (\"%s\")"
      while True:
         cur.execute( select % ( username, id ) )
         results = [ entry for entry in cur ]
         if results:
            self.id, self.username, self.dateCreated, self.password = results[0]
            break
         elif not strict:
            cur.execute( insert % ( username, password ) )
            con.commit()
         else:
            raise KeyError( 'User Not Found' )
      self.active = True

   def __repr__( self ):
      assert self.active, 'Object is no longer accessible'
      output = ''
      output += 'User ID: {}\n'.format( self.id )
      output += 'Username: {}\n'.format( self.username )
      output += 'Date Created: {}'.format( self.dateCreated )
      return output

   def verifyPassword( self, password ):
      ''' must be hashed string '''
      return password == self.password

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
   def __init__( self, con, ownerId, title='', id=0, strict=False ):
      assert ownerId, 'Owner for the Recipe object must be set'
      cur = con.cursor()
      while True:
         select = "SELECT * from Recipe where ownerId=%d and (id=%d or title=\"%s\")"
         cur.execute( select % ( ownerId, id, title ) )
         results = [ entry for entry in cur ]
         if results:
            self.id = results[0][0]
            self.title = results[0][1]
            self.ownerId = results[0][2]
            self.createdOn = results[0][3]
            self.updatedOn = results[0][4]
            self.bucket = results[0][5]
            self.bucketAudio = results[0][6]
            break
         elif not strict:
            insert = "INSERT into Recipe (ownerId,title) values ( %d, \"%s\")"
            cur.execute( insert % (ownerId, title) )
         else:
            raise KeyError( 'Recipe Not Found' )
      self.active = True

   def __repr__( self ):
      assert self.active, 'Object is no longer accessible'
      output = ''
      output += 'User ID: {}'.format( self.id )
      output += 'Title: {}'.format( self.title )
      output += 'Created On: {}'.format( self.createdOn )
      return output

   def titleIs( self, con, title ):
      assert self.active, 'Object is no longer accessible'
      self.title = title

   def yamlBucketKeyIs( self, con, key ):
      assert self.active, 'Object is no longer accessible'
      self.bucket = key

   def audioBucketKeyIs( self, con, key ):
      assert self.active, 'Object is no longer accessible'
      self.audio = key

   def save( self, con ):
      assert self.active, 'Object is no longer accessible'
      cur = con.cursor()
      update = 'UPDATE Recipe set title = \"%s\" where id=%d'
      cur.execute( update % ( self.title, self.id ) )
      con.commit()

   def delete( self, con, username='', id=0 ):
      assert self.active, 'Object is no longer accessible'
      cur = con.cursor()
      delete = "DELETE from Recipe where id=%d"  
      cur.execute( delete % self.id )
      self.active = False

class RecipeForUser( Recipe ):
   '''
   Another way of initializing, from previous query
   '''
   def __init__( self, id, title, ownerId, createdOn, updatedOn, bucket, bucketAudio ):
      self.id = id
      self.title = title
      self.ownerId = ownerId
      self.createdOn = createdOn
      self.updatedOn = updatedOn
      self.bucket = bucket
      self.bucketAudio = bucketAudio
      self.active = True
