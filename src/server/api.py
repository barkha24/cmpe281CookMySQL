#!/usr/bin/env python

from backend import rds_wrapper
import datetime

GET_RECIPE = '/getRecipe'
GET_RECIPES = '/getRecipes'
GET_USER_INFO = '/userInfo'

def api( endpoint, params ):
   '''
   Api handling module for the servers
   '''
   con = rds_wrapper.connect_mysql()
   print endpoint
   try:
      if endpoint == GET_USER_INFO:
         user = rds_wrapper.User( con, params[ 'username' ], strict=True )
         print user
         return  '', { 'id' : user.id,
                       'username' : user.username,
                       'dateCreated' : '{}'.format( user.dateCreated ) }
      elif endpoint == GET_RECIPE:
         recipe = rds_wrapper.Recipe( con, int( params[ 'ownerId' ] ),
                                      id=int( params[ 'id' ] ) )
         print recipe
         return '', { 'id' : recipe.id,
                      'bucket-yaml' : recipe.bucket,
                      'createdOn' : "{}".format( recipe.createdOn ),
                      'updatedOn' : "{}".format( recipe.updatedOn ),
                      'bucket-audio' : recipe.bucketAudio }
      raise KeyError( 'Endpoint Not found' )
   except TypeError, e:
      return str( "Ensure that the ID field is in numeric format and Non-ID fields are in string format, " + str(e) ), {}
   except KeyError, e:
      return str( e ), {}
   except ValueError, e:
      return str( "Ensure that the ID field is in numeric format and Non-ID fields are in string format, " + str( e) ), {}

#/getRecipe?format=json&recipeId=<recipeId> - get recipe instruction in JSON format/getRecipe?format=json&recipeId=<recipeId>
#/getRecipe?format=mp3 - get recipe instruction in mp3 format
#/userInfo?userId=<userId> - get user information
#/getRecipes?user=<userId> - get list of recipes in JSON format
