from TagDistance import *
from MajorColorDetection import *
from ServoControl import *
from picamera import PiCamera


while 1:
    camera = PiCamera()
    camera.capture("images/cache.png")
    color = majorColor('images/cache.png')
    print(color)
    # print(markerDistance('images/cache.png'))
    armMovement(color)



