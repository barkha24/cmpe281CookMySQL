import boto3
import ast
# from flask import Flask, render_template, request, make_response
from flask import Flask, flash, redirect, render_template, \
     request, url_for
s3 = boto3.resource('s3',
     aws_access_key_id='AKIAJ4KTDVOLX5N4HH4Q',
                       aws_secret_access_key='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')
#ast.literal_eval()
# client = boto3.client(
#     's3',
#     # Hard coded strings as credentials, not recommended.
#     aws_access_key_id='',
#     aws_secret_access_key=''
# )
bucket = s3.Bucket('one000')


app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    details_dict={'admin': 'secret', 'vidhi': 'admin', 'world': 'hello', 'hello':'world', 'adminis':'noproblem'}
    error = None
    if request.method == 'POST':
        for key, value in details_dict.items():
            if request.form['username'] != key or \
                    request.form['password'] != value:
                error = 'Invalid credentials'
            else:
                flash('You were successfully logged in')
                return redirect(url_for('upload_file'))
    return render_template('login.html', error=error)

#Uploading a file in Amazon S3
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == "POST":
        file = request.files['file']
        file_name = file.filename
        # data = open('UTA_Athletics_logo.png', 'rb')
        s3.Bucket('one000').put_object(Key='new/'+file_name, Body=file)
        return "Filename  " + file_name + "  is uploaded"
    return render_template('index_new.html')

#Listing a file in Amazon S3
@app.route('/list_files', methods=['GET', 'POST'])
def return_file():
    return_document = []
    if request.method == "POST":
        for buc in bucket.objects.all():
            #for key in buc.objects.all():
                print(buc.key)
                return_document.append(buc.key)
        print(return_document)
    return render_template('index_new.html', return_document=return_document)

#Deleting a file in Amazon S3
@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == "POST":
        file_name = request.form['filename']
        for buc in bucket.objects.all():
            print(buc)
            if file_name == buc.key:
                # print("Hiii----------")
                buc.delete()
        return "Filename=" + file_name + " has been deleted!.."
    return render_template('index_new.html')
#Download file
@app.route('/download', methods=['GET', 'POST'])
def download_file():
        file_name = request.form['filename']
        srcBucket = s3.get_bucket('one000')
        dstBucket = s3.get_bucket('one000')
        dstBucket.copy_key(file_name,srcBucket.name,file_name)
        return render_template('index_new.html')


if __name__ == '__main__':
   app.run(port=8000)
