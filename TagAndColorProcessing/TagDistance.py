#Filename :TagDistance.py
#----------------------Tag Distance Finder--------------------
#-----------------------Fauzanil Zaki,2016--------------------
#----------------------github.com/fauzanil--------------------
# Modified from : http://www.pyimagesearch.com/2015/01/19/find-distance-camera-objectmarker-using-python-opencv/
# Version 1.1
# OpenCV 2.4

import numpy as np
import cv2

def find_marker(image):
	# convert greyscale, detect edges
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (5, 5), 0)
	edged = cv2.Canny(gray, 35, 125)

	#Find contour
	# (_,cnts,_) for newer opencv
	#  marker 3.0 cm x 2.5cm
	(cnts,_) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	c = max(cnts, key = cv2.contourArea)

	# Count the boundling box
	return cv2.minAreaRect(c)

def distance_to_camera(knownWidth, focalLength, perWidth):
	#Calculate, return the distance to camera
	return (knownWidth * focalLength) / perWidth



def markerDistance(imagePath):
    cms = []  # markers distance, the firsiniti
    # initiaalize known distance
    # Used known distance is 10 cm
    KNOWN_DISTANCE = 10.0
    # initialize known width
    # width used = 3.0 cm
    KNOWN_WIDTH = 3.0
    #image for calibration can be found at images/calibration.png
    image = cv2.imread("images/calibration.png")
    marker = find_marker(image)
    focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH
    #Load the image
    image = cv2.imread(imagePath)
    #Find the marker
    marker = find_marker(image)
    #Find the distance
    cms = distance_to_camera(KNOWN_WIDTH, focalLength, marker[1][0])

        # draw a bounding box around the image and display it
        # Uncomment the lines below to draw on box on the detected tag
        # box = np.int0(cv2.cv.BoxPoints(marker))
        # cv2.drawContours(image, [box], -1, (0, 255, 0), 2)
        # cv2.putText(image, "%.2fcm" % (cms),
        # (image.shape[1] - 300, image.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
        # 2.0, (0, 255, 0), 3)
        # cv2.imshow("image", image)
        # cv2.waitKey(0)
    return cms




#testpath = "images/14cm.png"

