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
import requests
import sys
import os
import platform
import os.path, time
import cgi, io
import cgitb; cgitb.enable()
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask import Response
from flask import make_response
#from boto.s3.key import Key
from boto3.session import Session
import boto3.session
from botocore.exceptions import ClientError
import botocore.session
app = Flask(__name__)
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app.secret_key = 'sdg is crazy'
config = ConfigParser.ConfigParser()

AWS_ACCESS_ID = os.environ.get( 'AWS_ACCESS_ID' )
AWS_SECRET_KEY = os.environ.get( 'AWS_SECRET_KEY' )
assert len( AWS_ACCESS_ID ) > 0, 'Please set AWS access key'
assert len( AWS_SECRET_KEY ) > 0, 'Please set AWS secret key'

from backend import s3_helper

bucket_name_yaml = 'cmpe281-recipe'
bucket_name_mp3 = 'cmpe281-mp3'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#------------------------------------- Delete File ---------------------------------
@app.route('/DeleteFile',methods=['GET','POST'])
def DeleteFile():
        return render_template('file-delete.htm')

@app.route('/delfile',methods=['POST'])
def delfile():
        filename=request.form['fileName']
        request.args[ 'recipeTitle' ] =  filename
        err, response = api.postDeleteRecipe( request.args, request.headers.get( 'token' ) )
        if err:
           return toJson( err, response )
        # Data is all cleared, now delete the bucket objects
        try:
           for bucket_name in ( bucket_name_yaml, bucket_name_mp3 ):
              bucketkey = s3_helper.key( filename )
              s3 = boto3.resource( 's3',
                                   aws_access_key_id=AWS_ACCESS_ID,
                                   aws_secret_access_key=AWS_SECRET_KEY)
              s3.Object( bucket_name, bucketkey ).delete() 
        except Exception, e:
           return ( str(e), '' )
        return toJson( err, response )


#-----------------------------------File Upload ------------------------------
@app.route('/file-upload', methods=['GET', 'POST'])
def fileUpload():
        return render_template('file-upload.htm')

@app.route('/save-file', methods=['GET','POST'])
def saveFile():
        #print 'save'
        import os, time
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        request.args[ 'recipeTitle' ] = file.filename
        err, response = api.postDeleteRecipe( request.args, request.headers.get( 'token' ) )
        if err:
           return toJson( err, response )

        if file and allowed_file(file.filename):
                filename =  file.filename
                bucketkey = s3_helper.key( filename )
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
@app.route('/fileDownload',methods=['GET','POST'])
def fileDownload():
        return render_template('file-download.htm')

@app.route('/downloadfile',methods=['POST'])
def downloadfile():
        filename=request.form['fileName']
        s3 = boto3.resource('s3',aws_access_key_id=AWS_ACCESS_ID,aws_secret_access_key=AWS_SECRET_KEY)
        bucketkey = s3_helper.key( filename )
        fContent=s3.Object(bucket_name, bucketkey).get()['Body'].read()
        response = make_response(fContent)
        response.headers["Content-Disposition"] = "attachment; filename="+filename+";"
        return response


#------------------------ HSHIN ---------------------------------

from server import api
import json

def toJson( err, response ):
   return json.dumps({ "error" : err, "response" : response })

def parseInput():
   if request.data:
      print request.data
      return json.loads( request.data )
   return request.form

@app.route( api.POST_AUTHENTICATE, methods=['POST'])
def authenticate():
   err, response = api.authenticate( parseInput() )
   return toJson( err, response )

@app.route( api.POST_UPLOAD_RECIPE, methods=['POST'])
def uploadRecipe():
   err, response = api.postUploadRecipe( parseInput(), request.headers.get( 'token' ) )
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
   return toJson( err, response )

@app.route( api.GET_RECIPES, methods=['GET'])
def getRecipes():
   err, response = api.getRecipe( request.args, request.headers.get( 'token' ) )
   return toJson( err, response )

if __name__ == '__main__':
  app.run( host='0.0.0.0', port=8084, debug=True )
