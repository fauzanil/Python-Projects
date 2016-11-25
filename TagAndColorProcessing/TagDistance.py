#  many thanks to http://www.pyimagesearch.com/
import numpy as np
import cv2

def find_marker(image):
	# convert greyscale, detect edges
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (5, 5), 0)
	edged = cv2.Canny(gray, 35, 125)

	#cari kontur
	# (_,cnts,_) for newer opencv
	#  marker 3.0 cm x 2.5cm
	(cnts,_) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	c = max(cnts, key = cv2.contourArea)

	# hitung boundling box
	return cv2.minAreaRect(c)

def distance_to_camera(knownWidth, focalLength, perWidth):
	# hitung, kembalikan distance
	return (knownWidth * focalLength) / perWidth



def markerDistance(imagesPath):
    cms = []  # markers distance, the first one is the calibration marker
    # inisialisasi jarak yg diketahui
    # jarak yang digunakan 10 cm
    KNOWN_DISTANCE = 10.0
    # inisialisasi lebar yg diketahui
    # lebar yang digunakan 3 cm
    KNOWN_WIDTH = 3.0
    image = cv2.imread(imagesPath[0])
    marker = find_marker(image)
    focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH

    # loop over the images
    for imagePath in imagesPath:
        # load the image, find the marker in the image, then compute the
        # distance to the marker from the camera
        image = cv2.imread(imagePath)
        marker = find_marker(image)
        cms.append(distance_to_camera(KNOWN_WIDTH, focalLength, marker[1][0]))

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




testpath = ["images/10cm.png", "images/15cm.png", "images/unknown.png"]

print(markerDistance(testpath))