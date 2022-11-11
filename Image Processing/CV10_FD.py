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

faceCascade = cv.CascadeClassifier("haar/haarcascade_frontalface_default.xml")


while cap.isOpened():
    _ , frame = cap.read()
    frame = cv.flip(frame,1)
    
    frameGray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(frameGray,1.3, 5)
    
    for face in faces:
        x,y,w,h = face
        cv.rectangle(frame, (x,y), (x+w, y+h),(255,0,0),2)
        cv.putText(frame,"Unsigned Person", (x-5,y-5),cv.FONT_HERSHEY_COMPLEX,1,(255,0,0),1)
        # print("x= ",x)
        # print("y= ",y)
        # print("w= ",w)
        # print("h= ",h)
    
    cv.imshow("frame",frame)
    cv.moveWindow("frame", 0, 0)
    
    if cv.waitKey(1) & 0xff==ord("q"):
        break

cap.release()