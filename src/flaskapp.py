#!/usr/bin/env python

import ConfigParser
from boto3 import client
import tempfile
import urllib
from flask import Flask#, flash, redirect, render_template, \
from boto3.s3.transfer import S3Transfer
import boto3
from flask import Flask, flash, redirect, render_template, \
     request, url_for

from flask_cors import CORS
import sys
import os
import platform
import os.path, time
import cgi, io
import cgitb; cgitb.enable()
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask import Response
from flask import make_response
from flask import jsonify

#from boto.s3.key import Key
from boto3.session import Session
import boto3.session
from botocore.exceptions import ClientError
import botocore.session
from flask.ext.api import status

app = Flask(__name__)
CORS(app, resource={r"*": {"origins": "*"}})

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'json'])
app.secret_key = 'sdg is crazy'
config = ConfigParser.ConfigParser()

AWS_ACCESS_ID = os.environ.get( 'AWS_ACCESS_ID' )
AWS_SECRET_KEY = os.environ.get( 'AWS_SECRET_KEY' )
assert len( AWS_ACCESS_ID ) > 0, 'Please set AWS access key'
assert len( AWS_SECRET_KEY ) > 0, 'Please set AWS secret key'


from server import api
import json
from backend import s3_helper

bucket_name_yaml = 'cmpe281-recipe'
bucket_name_mp3 = 'cmpe281-mp3'


def toJson( err, response ):
   '''
   Return JSON response back to the user and include
   Access-Control-Allow-Origin
   '''
   resp = jsonify({ "error" : err, "response" : response })
   resp.headers.add('Access-Control-Allow-Origin', '*')
   print resp
   return resp

def parseInput():
   '''
   Return request.data if present, otherwise request.form
   '''
   if request.data:
      print request.data
      return json.loads( request.data )
   return request.form

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#------------------------------------- Delete File ---------------------------------
@app.route( api.POST_DELETE_FILE, methods=['POST'])
def delfile():
   data = parseInput()
   args = {}
   for k,v in data.items():
      args[k] = v
   print args
   err, response = api.postDeleteRecipe( args, request.headers.get( 'token' ) )
   if err:
      print 'Failed to delete recipe in the database or could not authenticate', err
      return toJson( err, '' )
   # Data is all cleared, now delete the bucket objects
   bucket_key_yaml, bucket_key_mp3 = response
   try:
      s3 = boto3.resource( 's3',
                          aws_access_key_id=AWS_ACCESS_ID,
                          aws_secret_access_key=AWS_SECRET_KEY)
      print 'Deleting %s from %s' % ( bucket_key_yaml, bucket_name_yaml )
      s3.Object( bucket_name_yaml, bucket_key_yaml ).delete() 
      print 'Deleting %s from %s' % ( bucket_key_mp3, bucket_name_mp3 )
      s3.Object( bucket_name_mp3, bucket_key_mp3 ).delete() 
   except Exception, e:
      return toJson( str(e), '' )
   return toJson( err, response )

#-----------------------------------File Upload ------------------------------
@app.route( api.POST_UPLOAD_FILE, methods=['GET','POST'])
def saveFile():
   import os, time
   file = request.files['file']

   if file.filename == '':
      flash('No selected file')
      return redirect(request.url)

   data = parseInput()
   args = {}
   for k,v in data.items():
      args[k] = v
   args[ 'fileName' ] = file.filename
   if file and allowed_file(file.filename):
      err, response = api.postUploadRecipe( args, request.headers.get( 'token' ) )
      if err:
         return toJson( err, response )

      filename, _ = response
      bucketkey = filename
      fContent = file.read()

      temporary_file = tempfile.NamedTemporaryFile()
      fw=open(temporary_file.name,'w+')
      fw.write(fContent)
      fw.close()
      data=open(temporary_file.name,'r')
      s3 = boto3.resource( 's3',
                           aws_access_key_id=AWS_ACCESS_ID,
                           aws_secret_access_key=AWS_SECRET_KEY )
      s3.Bucket(bucket_name_yaml).put_object(Key=bucketkey, Body=data)
      return toJson( err, response )
   return toJson( 'Invalid File extension', '' )

#----------------------- List Files -------------------------------
@app.route('/ListFiles',methods=['GET','POST'])
def ListFiles():
        html = ''
        s3 = boto3.resource('s3',aws_access_key_id=AWS_ACCESS_ID,
                                 aws_secret_access_key=AWS_SECRET_KEY )
        temp = []
        bucket=s3.Bucket(bucket_name_yaml)
        for obj in bucket.objects.all():
                temp.append(obj.key)
        html = '''<html>
                       <title>Attributes</title>
                       %s
               </html>''' %(temp)
        return html

#------------------File Download ---------------------------------
def downloadfile( bucketkey ):
   s3 = boto3.resource('s3',aws_access_key_id=AWS_ACCESS_ID,aws_secret_access_key=AWS_SECRET_KEY)
   fContent=s3.Object(bucket_name_yaml, bucketkey).get()['Body'].read()
   #response = make_response(fContent)
   #response.headers["Content-Disposition"] = "attachment; filename="+filename+";"
   return fContent

#------------------------ HSHIN ---------------------------------

@app.route( api.POST_AUTHENTICATE, methods=['POST'])
def authenticate():
   err, response = api.authenticate( parseInput() )
   if err:
      return toJson( err, response ), status.HTTP_401_UNAUTHORIZED
   return toJson( err, response )

@app.route( api.POST_SIGN_UP, methods=['POST'])
def postSignUp():
   err, response = api.postSignUp( parseInput() )
   return toJson( err, response )

@app.route( api.GET_USER_INFO, methods=['GET'])
def getUserInfo():
   err, response = api.getUserInfo( request.args, request.headers.get( 'token' ) )
   return toJson( err, response )

@app.route( api.GET_RECIPE, methods=['GET'])
def getRecipe():
   err, response = api.getRecipe( request.args, request.headers.get( 'token' ) )
   bucketKey = response[ 'bucketjson' ]
   content = downloadfile( bucketKey )
   response[ 'content' ] = json.loads( content )
   return toJson( err, response )

@app.route( api.GET_RECIPES, methods=['GET'])
def getRecipes():
   err, response = api.getRecipes( request.args, request.headers.get( 'token' ) )
   return toJson( err, response )

if __name__ == '__main__':
  app.run( host='0.0.0.0', port=8084, debug=True )
