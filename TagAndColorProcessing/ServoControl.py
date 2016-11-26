import RPi.GPIO as GPIO
import time

rotateBody = 2
claw = 4
upDown = 14
forwardBackward = 3

def armMovement(color):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(rotateBody, GPIO.OUT)
    GPIO.setup(claw, GPIO.OUT)
    # GPIO.setup(upDown,GPIO.OUT)
    GPIO.setup(forwardBackward, GPIO.OUT)

    rotateBodyp = GPIO.PWM(rotateBody, 50)
    clawp = GPIO.PWM(claw, 50)
    # upDownp = GPIO.PWM(upDown,50)
    forwardBackwardp = GPIO.PWM(forwardBackward, 50)

    rotateBodyp.start(1)
    forwardBackwardp.start(1)
    clawp.start(5)
    try:
        if (color == "Red"):
            clawp.ChangeDutyCycle(1)
            time.sleep(3)
            rotateBodyp.ChangeDutyCycle(7)
            time.sleep(3)
            forwardBackwardp.ChangeDutyCycle(12)
            time.sleep(3)
            clawp.ChangeDutyCycle(12)
            time.sleep(2)
            forwardBackwardp.ChangeDutyCycle(3)
            time.sleep(2)
            rotateBodyp.ChangeDutyCycle(12)
            time.sleep(3)
        if (color="Green"):
            clawp.ChangeDutyCycle(1)
            time.sleep(3)
            rotateBodyp.ChangeDutyCycle(7)
            time.sleep(3)
            forwardBackwardp.ChangeDutyCycle(12)
            time.sleep(3)
            clawp.ChangeDutyCycle(12)
            time.sleep(2)
            forwardBackwardp.ChangeDutyCycle(3)
            time.sleep(2)
            rotateBodyp.ChangeDutyCycle(1)
            time.sleep(3)

    except KeyboardInterrupt:
        clawp.stop()
        GPIO.cleanup()
