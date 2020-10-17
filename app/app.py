from PIL import Image
import numpy as np
from flask import Flask, render_template, request, redirect, jsonify
from flask_cors import CORS
import cv2
import time
import base64
import requests
import os
import sys

from utils.img_utils import *
from utils.Detector import Detector

import logging
from threading import Lock
from datetime import date

lock = Lock()

# initialize our Flask application and the Keras model
app = Flask(__name__)
app.config['CORS_HEADERS'] = "Content-Type"
app.config['CORS_RESOURCES'] = {r"/predict_img_url_kaggle": {"origins": "*"}}
cors = CORS(app)

## Initialize Object Detector ##
od = Detector()

def process_data(img_orig, dict_bbox=None):
	dict_bbox = od.detect(img_orig)
	return jsonify(dict_bbox)

@app.route("/predict_img_url_kaggle",  methods=["POST"])
def predict_img_url_kaggle():
	if request.method == "POST":
		with lock:
			start = time.time()
			req = request.get_json()
			url = req["url"]

			try:
				img_base64 = base64.b64encode(requests.get(url).content)
				img = readBase64(img_base64)
			except :
				final_output = get_final_output(None, None)
				return final_output

			final_output = process_data(img)

			return final_output

@app.after_request
def after_request(response):
	response.headers.add('Access-Control-Allow-Origin', '*')
	response.headers.add('Access-Control-Allow-Headers',
							'Content-Type,Authorization')
	response.headers.add('Access-Control-Allow-Methods',
							'GET,PUT,POST,DELETE,OPTIONS')
	return response


if __name__ == "__main__":

	print(("* Loading model and Flask starting server..."
		   "please wait until server has fully started"))

	app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
