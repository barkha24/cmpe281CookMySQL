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

   def tearDown( self ):
      self.user.delete( self.con )
      self.con.close()

if __name__ == '__main__':
   unittest.main()
