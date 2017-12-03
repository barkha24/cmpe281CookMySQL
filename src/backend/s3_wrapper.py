#!/usr/bin/env python

import tempfile
aid = os.getenv( 'AWS_ACCESS_ID' )
apwd = os.getenv( 'AWS_SECRET_KEy' )

def save( filename, fcontent ):
   '''
   save file to the s3 server
   '''
   assert aid and apwd, 'AWS credentials not defined'
   temporary_file = tempfile.NamedTemporaryFile()
   fw=open(temporary_file.name,'w+')
   fw.write(fContent)
   fw.close()
   data=open(temporary_file.name,'r')
   s3 = boto3.resource('s3',aws_access_key_id=aid,aws_secret_access_key=apwd)
   s3.Bucket(bucket_name).put_object(Key=filename, Body=data)
   return filename
