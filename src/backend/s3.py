#!/usr/bin/env python

from hashlib import sha256

def bucketKeyGenerator( name ):
   return sha256( name ).hexdigest()
