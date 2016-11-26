import RPi.GPIO as GPIO
import time

rotateBody = 2
claw = 4
upDown = 14
forwardBackward = 3


GPIO.setmode(GPIO.BCM)
GPIO.setup(rotateBody,GPIO.OUT)
#GPIO.setup(claw,GPIO.OUT)
#GPIO.setup(upDown,GPIO.OUT)
#GPIO.setup(forwardBackward,GPIO.OUT)

rotateBodyp = GPIO.PWM(rotateBody,50)
#clawp = GPIO.PWM(claw,50)
#upDownp = GPIO.PWM(upDown,50)
# forwardBackwardp = GPIO.PWM(forwardBackward,50)


rotateBodyp.start(5)