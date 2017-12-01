#!/usr/bin/env python

from backend import rds_wrapper
import datetime
import tokens

GET_RECIPE = '/getRecipe'
GET_RECIPES = '/getRecipes'
GET_USER_INFO = '/userInfo'
POST_AUTHENTICATE = '/authenticate'
POST_SIGN_UP = '/signup'
POST_UPLOAD_RECIPE = '/uploadRecipe'

#
# API End point
#
# /getRecipe?format=json&recipeId=<recipeId> - get recipe instruction in JSON format/getRecipe?format=json&recipeId=<recipeId>
# /getRecipe?format=mp3 - get recipe instruction in mp3 format
# /userInfo?userId=<userId> - get user information
# /getRecipes?user=<userId> - get list of recipes in JSON format

con = rds_wrapper.connect_mysql()

def t( string ):
   print string

def authenticate( params ):
   t( 'Authenticating with params {}'.format( params ) )
   print params
   print 'a'
   print params[ 'username' ]
   print 'a'
   user = rds_wrapper.User( con, params[ 'username' ], strict=True )
   try:
      token = tokens.Token( user.username, params[ 'password' ] )
      return '', { 'token' : token.token_,
                   'username' : params[ 'username' ],
                   'userId' : token.userId(),
                   'until' : token.until() }
   except AssertionError:
      return 'Invalid authentication', ''
   except Exception, e:
      print e
      return str( e ), ''

def postSignUp( params ):
   t( 'Sign up with params {}'.format( params ) )
   try:
      user = rds_wrapper.User( con, params[ 'username' ], strict=True )
      return 'Username already exists', []
   except KeyError:
      user = rds_wrapper.User( con, params[ 'username' ],
                                    tokens.hashPassword( params[ 'password' ], params[ 'username' ] ),
                                    params[ 'firstname' ],
                                    params[ 'lastname' ],
                                    params[ 'mobile' ]
                              )
      return '', "Succesful! Your account has been created.";

def postDeleteRecipe( params, tokenString ):
   try:
      recipe = rds_wrapper.Recipe( self.con, params[ 'ownerId' ],
                                   params[ 'recipeTitle' ] )
      recipe.delete( self.con )
   except KeyError:
      return 'Recipe not found', ''

def postUploadRecipe( params, tokenString ):
   try:
      rds_wrapper.Recipe( self.con, params[ 'ownerId' ],
                          params[ 'recipeTitle' ], strict=True )
      return 'Recipe already exists', []
   except KeyError:
      recipe = rds_wrapper.Recipe( self.con, params[ 'ownerId' ],
                                   params[ 'recipeTitle' ] )
      return '', "Succesful! Recipe has been uploaded.";


def getUserInfo( params, tokenString ):
   user = rds_wrapper.User( con, params[ 'username' ], strict=True )
   try:
      token = tokens.Token( user.username, token=tokenString )
      assert token.isValid()
   except AssertionError:
      return 'Invalid authentication', []
   return  '', { 'id' : user.id,
                 'username' : user.username,
                 'firstname' : user.firstname,
                 'lastname' : user.lastname,
                 'mobile' : user.mobile,
                 'dateCreated' : '{}'.format( user.dateCreated ) }


def getRecipe( params, tokenString ):
   recipe = rds_wrapper.Recipe( con, int( params[ 'ownerId' ] ),
                                id=int( params[ 'id' ] ) )
   user = rds_wrapper.User( con, id=int( params[ 'ownerId' ]), strict=True )
   try:
      token = tokens.Token( user.username, token=tokenString )
      assert token.isValid()
   except AssertionError:
      return 'Invalid authentication', []
   return '', { 'id' : recipe.id,
                'bucket-yaml' : recipe.bucket,
                'createdOn' : "{}".format( recipe.createdOn ),
                'updatedOn' : "{}".format( recipe.updatedOn ),
                'bucket-audio' : recipe.bucketAudio }


def getRecipes( params, tokenString ):
   user = rds_wrapper.User( con, id=int( params[ 'ownerId' ] ), strict=True )
   try:
      token = tokens.Token( user.username, token=tokenString )
      assert token.isValid()
   except AssertionError:
      return 'Invalid authentication', []

   recipes = rds_wrapper.getRecipesForUser( con, user )
   results = []
   for recipe in recipes:
      results.append( { 'id' : recipe.id,
        'bucket-yaml' : recipe.bucket,
        'createdOn' : "{}".format( recipe.createdOn ),
        'updatedOn' : "{}".format( recipe.updatedOn ),
        'bucket-audio' : recipe.bucketAudio } )
   return '', results

def api( endpoint, params, headers={} ):
   '''
   Api handling module for the servers
   '''
   tokenString = headers.get( 'token', '' )
   print endpoint
   try:
      if endpoint == POST_AUTHENTICATE:
         return authenticate( params )

      elif endpoint == POST_UPLOAD_RECIPE:
         return postUploadRecipe( params, tokenString )

      elif endpoint == POST_SIGN_UP:
         return postSignUp( params, tokenString )

      elif endpoint == GET_USER_INFO:
         return getUserInfo( params, tokenString )

      elif endpoint == GET_RECIPE:
         return getRecipe( params, tokenString )

      elif endpoint == GET_RECIPES:
         return getRecipes( params, tokenString )

      raise KeyError( 'Endpoint Not found' )
   except TypeError, e:
      return str( "Ensure that the ID field is in numeric format and Non-ID fields are in string format, " + str(e) ), {}
   except KeyError, e:
      return str( e ), {}
   except ValueError, e:
      return str( "Ensure that the ID field is in numeric format and Non-ID fields are in string format, " + str( e) ), {}
