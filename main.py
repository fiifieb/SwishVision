import cv2
import cvzone
import math
import cvzone
from cvzone.ColorModule import ColorFinder
import numpy as np

# Initialization

cam = cv2.VideoCapture('Test ball/Videos/vid (3).mp4')
x_pos_list = []
y_pos_list = []
x_path = [i for i in range(1300)]
# y_path = []

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

    # Trace ball path
    if contours:
        x_pos_list.append(contours[0]['center'][0])   
        y_pos_list.append(contours[0]['center'][1])  
    # Calculations y = Ax^2 + Bx + C
    if x_pos_list:
        for i, (x,y) in enumerate(zip(x_pos_list,y_pos_list)):
            cv2.circle(imgContours,(x,y),5,(0,255,0),cv2.FILLED)
            if i>0:
                cv2.line(imgContours,(x,y),(x_pos_list[i-1],y_pos_list[i-1]),(0,255,0),2)
        
        # Calculations y = Ax^2 + Bx + C
        a,b,c = np.polyfit(x_pos_list,y_pos_list,2)

        for x in x_path:
            y = int((a*x*x) + (b*x) + c)
            cv2.circle(imgContours,(x,y),1,(0,0,255),cv2.FILLED)










    # Display 
    imgContours = cv2.resize(imgContours, (0,0),None,0.7,0.7)
    cv2.imshow('Image', imgContours)
    cv2.waitKey(40)