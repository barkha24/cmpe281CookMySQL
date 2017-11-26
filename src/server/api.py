#!/usr/bin/env python

from backend import rds_wrapper
import datetime
import tokens

GET_RECIPE = '/getRecipe'
GET_RECIPES = '/getRecipes'
GET_USER_INFO = '/userInfo'
GET_AUTHENTICATE = '/authenticate'

#
# API End point
#
# /getRecipe?format=json&recipeId=<recipeId> - get recipe instruction in JSON format/getRecipe?format=json&recipeId=<recipeId>
# /getRecipe?format=mp3 - get recipe instruction in mp3 format
# /userInfo?userId=<userId> - get user information
# /getRecipes?user=<userId> - get list of recipes in JSON format

def api( endpoint, params, headers={} ):
   '''
   Api handling module for the servers
   '''
   con = rds_wrapper.connect_mysql()
   tokenString = headers.get( 'token', '' )
   print endpoint
   try:
      if endpoint == GET_AUTHENTICATE:
         user = rds_wrapper.User( con, params[ 'username' ], strict=True )
         try:
            token = tokens.Token( user.username, params[ 'password' ] )
            return '', { 'token' : token.token,
                         'username' : params[ 'username' ],
                         'userId' : token.userId(),
                         'until' : token.until() }
         except AssertionError:
            return 'Invalid authentication', ''


      elif endpoint == GET_USER_INFO:
         user = rds_wrapper.User( con, params[ 'username' ], strict=True )
         try:
            token = tokens.Token( user.username, token=tokenString )
            assert token.isValid()
         except AssertionError:
            return 'Invalid authentication', []
         return  '', { 'id' : user.id,
                       'username' : user.username,
                       'dateCreated' : '{}'.format( user.dateCreated ) }

      elif endpoint == GET_RECIPE:
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

      elif endpoint == GET_RECIPES:
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

      raise KeyError( 'Endpoint Not found' )
   except TypeError, e:
      return str( "Ensure that the ID field is in numeric format and Non-ID fields are in string format, " + str(e) ), {}
   except KeyError, e:
      return str( e ), {}
   except ValueError, e:
      return str( "Ensure that the ID field is in numeric format and Non-ID fields are in string format, " + str( e) ), {}
