import cv2
import glob
import os.path as path
photosdir='/home/sanyam/Downloads/photos'
checkedphotos = '/home/sanyam/Downloads/chekedones'




def mark_face(cascade,filepath):
	image = cv2.imread(filepath,cv2.IMREAD_COLOR)
	faces = cascade.detectMultiScale(image , 1.3, 5)

	for (x, y, w, h) in faces:
		cv2.rectangle(image, (x, y),(x+w,y+h), (0, 0, 255), 2)

	return image
default_cascade = cv2.CascadeClassifier('/home/sanyam/Downloads/haarcascade_frontalface_default.xml')
filepaths = glob.glob(path.join(photosdir, '*.jpg'))
for filepath in filepaths:
	marked_image = mark_face(default_cascade,filepath)
	resized_marked_image = cv2.resize(marked_image, (400, 400))
	cv2.imwrite(path.join(checkedphotos, path.basename(filepath)), resized_marked_image)
