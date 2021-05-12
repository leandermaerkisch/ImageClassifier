import os
from fastai import *
from fastai.vision import *

import numpy as np
import pickle

from flask import Flask, render_template, url_for, request, redirect, jsonify
from werkzeug.utils import secure_filename
import time



app = Flask(__name__)
UPLOAD_FOLDER = "/Users/leandermarkisch/Documents/FlaskProject/static/images"
MODEL = None
DEVICE = "cpu"
FILE = None
#with open('export.pkl', 'rb') as f:
#    MODEL = pickle.load(f)

def predict(image_path, model):
    mean = (0.485, 0.456, 0.406)
    std = (0.229, 0.224, 0.225)
    test_images = [image_path]
    test_targets = [0]


@app.route('/', methods=['GET', 'POST'])
def index():
    '''
    For rendering results on HTML GUI
    '''
    output = "Pneunomia" #round(prediction[0], 2)
    if request.method == "POST":
        image_file = request.files["image"]
        if image_file:
            filename = secure_filename(image_file.filename)
            FILE  = filename
            image_location = os.path.join(
                UPLOAD_FOLDER,
                filename
            )
            image_file.save(image_location)
            return render_template('index.html', uploaded_img="static/images/"+filename)
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    output = "Pneunomia"
    pred = "80"
    pred_img = "mri_annotated.png"
    time.sleep(5)
    return render_template('index.html', prediction_text='You have {} with {}% probability'.format(output, pred), uploaded_img="static/images/mri_raw.jpg", annotated_img="static/images/"+pred_img)



if __name__ == "__main__":
    #MODEL.to(DEVICE)
    app.run(port=12000, debug=True)