#!/usr/bin/env python

import unittest
import rds_wrapper

class RdsTest( unittest.TestCase ):
   '''
   RdsTest is a test for adding and removing entries from
   database. We will add tests as we add more features
   '''
   def setUp( self ):
      self.con = rds_wrapper.connect_mysql()
      self.user = rds_wrapper.User( self.con, 'hello' )

   def testPrint( self ):
      print self.user

   def testUser( self ):
      account = rds_wrapper.User( self.con, 'bobby' )
      account.delete( self.con )
      try:
         print account
         raise RuntimeError( 'Deleted object did not raise exception' )
      except AssertionError:
         pass
      # Test rename
      account_orig = rds_wrapper.User( self.con, 'charles' )
      account_orig.usernameIs( 'Charlie' )
      account_orig.save( self.con )
      account_verify = rds_wrapper.User( self.con, 'Charlie' )
      assert account_orig.id == account_verify.id
      account_orig.delete( self.con )

   def testRecipe( self ):
      try:
         owner = rds_wrapper.User( self.con, 'theCook' )
         recipe = rds_wrapper.Recipe( self.con, owner.id, 'cheesecake' )
         assert recipe.title == 'cheesecake'
         recipe.titleIs( self.con, 'chocolate cheesecake' )
         assert recipe.title == 'chocolate cheesecake'
         recipe.save( self.con )
         newrecipe = rds_wrapper.Recipe( self.con, owner.id, 'chocolate cheesecake' )
         assert newrecipe.id == recipe.id
         newrecipe.delete( self.con )
         try:
            print newrecipe
            raise RuntimeError( 'Deleted object did not raise exception' )
         except AssertionError:
            pass
      finally:
         owner.delete( self.con )

   def testRecipes( self ):
      try:
         recipes = []
         owner = rds_wrapper.User( self.con, 'theChef' )
         for i in range( 10 ):
            recipeTitle = 'recipe%d' % i
            recipes.append( rds_wrapper.Recipe( self.con, owner.id, recipeTitle ) )
         # Now get recipes
         newRecipes = rds_wrapper.getRecipesForUser( self.con, owner )
         oldIds = [ recipe.id for recipe in recipes ]
         oldIds.sort()
         newIds = [ recipe.id for recipe in newRecipes ]
         newIds.sort()
         for i in range( 10 ):
            assert newIds[i] == oldIds[i]
         for recipe in newRecipes:
            recipe.delete( self.con )
      finally:
         owner.delete( self.con )

   def tearDown( self ):
      self.user.delete( self.con )
      self.con.close()

if __name__ == '__main__':
   unittest.main()
