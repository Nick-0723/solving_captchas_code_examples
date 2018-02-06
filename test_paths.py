from imutils import paths
import cv2
import numpy as np

for imagePath in paths.list_images("testing_paths"):
	print imagePath
	image = cv2.imread(imagePath)
	cv2.imshow("imagePath", image)
	cv2.waitKey()
