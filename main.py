import cv2
import cvzone
import math
import cvzone
from cvzone.ColorModule import ColorFinder
import numpy

# Initialization

cam = cv2.VideoCapture('Test ball/Videos/vid (1).mp4')

while True:
    # Find image
    success, img = cam.read()
    # whole_img = cv2.imread("Test ball/Ball.png")
    img = img[0:900,:]

    # Find ball color 
    colorFinder = ColorFinder(False)
    hsv={'hmin' : 8 , 'smin' : 96 , 'vmin' : 115, 'hmax' : 15 , 'smax' : 255 ,'vmax' : 255}
    color, mask = colorFinder.update(img,hsv)

    # Find ball location
    imgContours, contours = cvzone.findContours(img,mask,minArea=500)




    # Display 
    img = cv2.resize(color, (0,0),None,0.7,0.7)
    cv2.imshow('Image', imgContours)
    cv2.waitKey(40)