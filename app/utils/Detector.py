import os
###################
import sys
import numpy as np
from utils.models import *  # set ONNX_EXPORT in models.py
from utils.datasets import *

CLASS_NAMES = "configs/classes.names"
CONFIG_FILE = "configs/yolov3-tiny.cfg"
WEIGHTS_FILE = "weights/yolov3-tiny.weights"

class Detector():
	def __init__(self):
		self.names_classes = CLASS_NAMES
		self.config = CONFIG_FILE
		self.weights = WEIGHTS_FILE
		self.img_size = (416, 256)
		
		self.load_detector()

	def load_detector(self):
		# Initialize model
		self.detector_model = Darknet(self.config, self.img_size)
		# Load weights    
		load_darknet_weights(self.detector_model, self.weights)
		# Get names
		self.detector_classes = load_classes(self.names_classes)

		if torch.cuda.is_available():
			self.detector_model.to(0).eval()
		else:
			self.detector_model.eval()

	def detect(self,img_orig):    

		img = get_yolo_img(img_orig,self.img_size)
		
		if img.ndimension() == 3:
			img = img.unsqueeze(0)

		pred = self.detector_model(img)[0]
		# Apply NMS
		pred = non_max_suppression(pred, 0.3, 0.6)

		dict_bbox = {}
		# for name in self.detector_classes:
		# 	dict_bbox[name] = []

		# Process detections
		for i, det in enumerate(pred):  # detections per image
			if det is not None and len(det):
				# Rescale boxes from img_size to im0 size
				det[:, :4] = scale_coords(img.shape[2:], det[:, :4], img_orig.shape).round()

				for det_loc in det:
					conf = det_loc[4]
					cls_loc = det_loc[5]
					dict_bbox[self.detector_classes[int(cls_loc)]] = list(map(int,det_loc[:4]))

		return dict_bbox
