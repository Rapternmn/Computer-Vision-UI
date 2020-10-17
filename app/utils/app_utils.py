import os
import sys
import torch
import numpy as np
from io import BytesIO
import pandas as pd
from flask import jsonify

myntra_db = 'data/feature_myntra.csv'
arr_cls = ["class","category_top","conf_top","sleeve","category_bottom","conf_bottom","category_full_body","conf_full_body","color_1",
			"conf_color_1","color_2","conf_color_2","pattern_1","conf_pattern_1","pattern_2","conf_pattern_2","gender"]

weights_features = [1000,500,1,100,500,1,500,1,300,1,10,1,100,1,1,1,1000]
weights_features = np.asarray(weights_features)

df = pd.read_csv(myntra_db,sep = "\t")
features = df.iloc[:,:-2].values
features = features*weights_features

def search_on_matrix(m, v):
	r = np.sqrt(np.sum(np.square(np.subtract(m, v)), axis=1))
	num_top_k = 8
	val_k, idx_k = torch.topk(torch.from_numpy(r),num_top_k,largest = False)
	val_k = np.asarray(val_k)
	idx_k = np.asarray(idx_k)
	return idx_k, val_k  

def get_url(f_vect):
	f_vect *= weights_features
	idx, dist = search_on_matrix(f_vect,features)
	url = df.iloc[idx,-2].values
	product_url = df.iloc[idx,-1].values
	return url, product_url

def consolidated_output(data):
	color = data["color"]
	pattern = data["pattern"] 
	category = data["category"] 

	# final_str = '{} {} {}'.format(color,pattern,category)
	final_str = '{} {} {}'.format(pattern, color, category)

	if category in ["Saree", "Kurta"]:
		final_str = '{} {}'.format(color,category)

	if data['sleeve'] > -1 :
		# final_str = '{} {} {} {}'.format(color,pattern,data['sleeve_type'],category)
		final_str = '{} {} {} {}'.format(pattern, color, data['sleeve_type'], category)

	return final_str

def get_data_init():
	data = {}
	data["class"] = -1
	data["category_top"] = -1
	data["conf_top"] = -1
	data["sleeve"] = -1
	data["category_bottom"] = -1
	data["conf_bottom"] = -1
	data["category_full_body"] = -1
	data["conf_full_body"] = -1
	data["color_1"] = -1
	data["conf_color_1"] = -1
	data["color_2"] = -1
	data["conf_color_2"] = -1
	data["pattern_1"] = -1
	data["conf_pattern_1"] = -1
	data["pattern_2"] = -1
	data["conf_pattern_2"] = -1
	data["gender"] = 0.5 ## In between 0 / 1

	return data

def data_feature(data):
	f_vect = []
	f_vect.append(data["class"])
	f_vect.append(data["category_top"])
	f_vect.append(data["conf_top"])
	f_vect.append(data["sleeve"])
	f_vect.append(data["category_bottom"])
	f_vect.append(data["conf_bottom"])
	f_vect.append(data["category_full_body"])
	f_vect.append(data["conf_full_body"])
	f_vect.append(data["color_1"])
	f_vect.append(data["conf_color_1"])
	f_vect.append(data["color_2"])
	f_vect.append(data["conf_color_2"])
	f_vect.append(data["pattern_1"])
	f_vect.append(data["conf_pattern_1"])
	f_vect.append(data["pattern_2"])
	f_vect.append(data["conf_pattern_2"])
	f_vect.append(data["gender"])

	return f_vect


def get_final_output(data, f_vect):
	final_output = {}

	if not data:
		final_output['type'] = "Detection Failed. Try another Image"
		final_output['similar'] = None
		final_output['similar_product'] = None
		return jsonify(final_output)

	image_urls, product_urls = get_url(f_vect)
	final_output['type'] = consolidated_output(data)
	final_output['similar'] = "{}".format(image_urls)
	final_output['similar_product'] = "{}".format(product_urls)

	return jsonify(final_output)
