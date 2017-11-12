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

   def tearDown( self ):
      self.user.delete( self.con )
      self.con.close()

if __name__ == '__main__':
   unittest.main()
