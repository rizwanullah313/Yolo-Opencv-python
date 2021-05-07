import os
import cv2
import requests
from app import app
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed below')
        return render_template('upload.html', filename=filename)
    else:
        flash('Allowed image types are -> png, jpg, jpeg, gif')
        return redirect(request.url)

# img = cv2.imread("Resources/car1.jpg")
#-------------------------------------------------
# import http.client
import  requests

# conn = http.client.HTTPSConnection("api.collectapi.com")

# headers = {
  #  'content-type': "application/json",
   # 'authorization': "apikey your_token"
    #}

#conn.request("GET", "/vehicleai/vehicleDetection?photourl=url", headers=headers)

#res = conn.getresponse()
#data = res.read()

#print(data)
#---------------------------------------------------

#data = {
 #   "success": True,
  #  "result": [
     #   {
      #      "model": "Ford",
       #     "vehicletype": "car",
        #    "color": "Blue"
        #}
    #]
#}
#print(data)


@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

if __name__ == "__main__":
    app.run()