import numpy as np
from io import BytesIO
from PIL import Image
import cv2
import base64

def convert_bytes_to_img(img_bytes):
	pil_image = Image.open(BytesIO(img_bytes))
	img_np = np.asarray(pil_image)                                                                                                                                                      
	img_np = cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
	return img_np

def readBase64(imgstring): 
	imgdata = base64.b64decode(imgstring) #Decode into byte array
	# imgdata = base64.decodestring(imgstring) 
	img_np = convert_bytes_to_img(imgdata)
	return img_np

def get_img_b64(img):
	_, im_arr = cv2.imencode('.jpg', img)
	im_bytes = im_arr.tobytes()
	im_b64 = base64.b64encode(im_bytes).decode("utf-8")
	return im_b64