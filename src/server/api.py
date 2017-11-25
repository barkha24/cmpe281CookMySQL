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
   except KeyError, e:
      return str( e ), {}

#/getRecipe?format=json&recipeId=<recipeId> - get recipe instruction in JSON format/getRecipe?format=json&recipeId=<recipeId>
#/getRecipe?format=mp3 - get recipe instruction in mp3 format
#/userInfo?userId=<userId> - get user information
#/getRecipes?user=<userId> - get list of recipes in JSON format
