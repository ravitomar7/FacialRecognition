import glob, os
import cv2
import numpy as np
os.chdir("/home/sanyam/Downloads/sanyamPhotos")
def getting_img():
	for file in glob.glob("*.jpg"):
		print(file)
		img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
		resized_image=cv2.resize(img, (100,100))
		cv2.imwrite(file,resized_image)
getting_img()
	
	
	
