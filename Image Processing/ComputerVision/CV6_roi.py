import numpy as np
import cv2 as cv

width = 640
height = 360
fps = 75

cap = cv.VideoCapture(0, cv.CAP_DSHOW)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, height)
cap.set(cv.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv.CAP_PROP_FPS, fps)
cap.set(cv.CAP_PROP_FOURCC, cv.VideoWriter_fourcc(*"MJPG"))

while cap.isOpened():
    _ , frame = cap.read()
    #frame[HEIGHT , WIDTH]
    
    frameROI = frame[150:210, 250:390]
    frameROIGray = cv.cvtColor(frameROI, cv.COLOR_BGR2GRAY)
    frameROIBGR = cv.cvtColor(frameROIGray, cv.COLOR_GRAY2BGR)
    
    # ıf we try to frame[:] = frameROI ıt doesnt work because size doesnt match each other
    # However, we transform first gray pıcture to BGR and then try it works!
    
    frame[0:60, 0:140] = frameROIBGR

    cv.imshow("frame4",frameROIBGR)
    cv.moveWindow("frame4", 660, 180)

    cv.imshow("frame3",frameROIGray)
    cv.moveWindow("frame3", 660, 90)
    
    cv.imshow("frame2",frameROI)
    cv.moveWindow("frame2", 660, 0)
    
    cv.imshow("frame",frame)
    cv.moveWindow("frame", 0, 0)
    
    if cv.waitKey(1) & 0xff==ord("q"):
        break

cap.release()
