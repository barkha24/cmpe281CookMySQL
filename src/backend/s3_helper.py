#!/usr/bin/env python

from hashlib import sha256

def key( name ):
   return name
   #return sha256( name ).hexdigest()
