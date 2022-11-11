from tkinter import W
import numpy as np
import cv2 as cv

def onTrack1(val):
    global hueLow
    hueLow = val
    print("Hue Low", hueLow)

def onTrack2(val):
    global hueHigh
    hueHigh = val
    print("Hue High", hueHigh)
    
def onTrack3(val):
    global satLow
    satLow = val
    print("Sat Low", satLow)
    
def onTrack4(val):
    global satHigh
    satHigh = val
    print("Sat High", satHigh)

def onTrack5(val):
    global valLow
    valLow = val
    print("val Low", valLow)
    
def onTrack6(val):
    global valHigh
    valHigh = val
    print("Val High", valHigh)


width = 640
height = 360
fps = 60

cap = cv.VideoCapture(0, cv.CAP_DSHOW)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, height)
cap.set(cv.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv.CAP_PROP_FPS, fps)
cap.set(cv.CAP_PROP_FOURCC, cv.VideoWriter_fourcc(*"MJPG"))

cv.namedWindow("myTracker")
cv.moveWindow("myTracker", width + 10,0)

hueLow = 10
hueHigh = 20
satLow = 10
satHigh = 250
valLow = 10
valHigh = 250

cv.createTrackbar("Hue Low" , "myTracker", 10, 179 ,onTrack1)
cv.createTrackbar("Hue High" , "myTracker", 20, 179 ,onTrack2)
cv.createTrackbar("Sat Low" , "myTracker", 10, 255 ,onTrack3)
cv.createTrackbar("Sat High" , "myTracker", 250, 255 ,onTrack4)
cv.createTrackbar("Val Low" , "myTracker", 10, 255 ,onTrack5)
cv.createTrackbar("Val High" , "myTracker", 250, 255 ,onTrack6)

while cap.isOpened():
    _ , frame = cap.read()
    frameHSV  = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lowerBound = np.array([hueLow,satLow,valLow])
    upperBound = np.array([hueHigh,satHigh,valHigh])

    myMask = cv.inRange(frameHSV, lowerBound, upperBound)
    myMask = cv.bitwise_not(myMask)
    
    #cv.imshow("My mask",myMask)
    #cv.moveWindow("My mask", 0 , height + 10)
    
    myMaskSmall = cv.resize(myMask, (int(width/2), int(height/2)))

    myObject = cv.bitwise_and(frame,frame,mask=myMask)
    myObjectSmall = cv.resize(myObject, (int(width/2), int(height/2)))
    
    cv.imshow("My object small",myObjectSmall)
    cv.moveWindow("My object small", int(width/2) + 10, int(height) + 10 )
    
    cv.imshow("My mask small",myMaskSmall)
    cv.moveWindow("My mask small", 0, height + 10)
    
    cv.imshow("frame",frame)
    cv.moveWindow("frame", 0, 0)
    
    if cv.waitKey(1) & 0xff==ord("q"):
        break

cap.release()
