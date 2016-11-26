from TagDistance import *
from MajorColorDetection import *
from picamera import PiCamera


camera = PiCamera()
camera.capture("images/cache.png")
print(majorColor('images/cache.jpg'))
print(markerDistance('images/cache.jpg'))



