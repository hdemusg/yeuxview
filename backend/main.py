from flask import Flask, render_template, request
from PIL import Image
from io import BytesIO
import requests
import os
from google.cloud import storage
from pipeline import *

app = Flask(__name__)

TEST_FOLDER = '../static'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = TEST_FOLDER
app.config['BUCKET_URL'] = "yeuxview.appspot.com"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'

@app.route('/')
def root():
    images = {
        'right_image': open('0_right.jpg', 'rb'),
        'left_image': open('0_left.jpg', 'rb'),
    }
    # For the sake of example, use static information to inflate the template.
    # This will be replaced with real information in later steps.
    #my_img = {'image': open("fmicon.jpg", 'rb')}
    r = requests.post('http://127.0.0.1:8081/pipeline', files=images)
    filename=os.path.join(app.config['UPLOAD_FOLDER'], r.text)
    return render_template('index.html', image=filename)

@app.route('/pipeline-test', methods=['GET', 'POST'])
def accept_input_test():
    
    print('file: ', request.files["image"].filename)
    file = request.files["image"]
    img = Image.open(file.stream)
    img.save('output.jpg')
    return 'output.jpg'

@app.route('/pipeline', methods=['GET', 'POST'])
def accept_input():
    '''
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(object_name)
    blob.upload_from_string(image_data)
    '''
    file_r = request.files["right_image"]
    file_l = request.files["left_image"]
    print(file_l, file_r)
    filename_r = file_r.filename
    filename_l = file_l.filename
    storage_client = storage.Client()
    bucket = storage_client.bucket(app.config['BUCKET_URL'])
    blob_l = bucket.blob(filename_l)
    blob_r = bucket.blob(filename_r)
    blob_l.upload_from_file(file_obj=file_l,  rewind=True)
    blob_r.upload_from_file(file_obj=file_r,  rewind=True)
    image_l = fetch(filename_l, bucket, filename_l)
    image_r = fetch(filename_r, bucket, filename_r)
    data = classify(image_l, image_r)
    return data

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8081, debug=True)