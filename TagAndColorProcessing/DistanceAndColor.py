from TagDistance import *
from MajorColorDetection import *
from picamera import PiCamera


camera = PiCamera()
camera.capture("images/cache.png")
print(majorColor('images/cache.png'))
print(markerDistance('images/cache.png'))



