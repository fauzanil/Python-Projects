

import cv2
import numpy

def majorColor(image):
    maxColor = -1
    majorColor = ""
    img = cv2.imread(image)
    average = numpy.average(img, anbvcxzxis=0)
    averageColor = numpy.average(average, axis=0)

    for i in range(0,3):
        if averageColor[i] > maxColor:
            maxColor = averageColor[i]
            majorColor = i

    def channelToColor(channel):
        switcher = {
            0 : "Blue",
            1 : "Green",
            2 : "Red",
        }
        return switcher.get(channel,"nothing")

    return channelToColor(majorColor)


print(majorColor('images/testimage.jpg'))


