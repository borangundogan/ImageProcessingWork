from tkinter.messagebox import NO
from turtle import circle, pos
from unittest import result
import numpy as np
import cv2 as cv
import mediapipe as mp

width = 640
height = 360
fps = 60

cap = cv.VideoCapture(0, cv.CAP_DSHOW)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, height)
cap.set(cv.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv.CAP_PROP_FPS, fps)
cap.set(cv.CAP_PROP_FOURCC, cv.VideoWriter_fourcc(*"MJPG"))

pose = mp.solutions.pose.Pose(False, False, 1 ,True, 0.5, 0.5)
mpDraw = mp.solutions.drawing_utils

circleRad = 10
circleColor = (0,0,255)
circleThickness = 3

eyeColor = (255,0,0)
eyeRadius = 6
eyeThickness = -1


while cap.isOpened():
    _ , frame = cap.read()
    frame = cv.flip(frame,1)
    frame = cv.resize(frame, (width,height),interpolation= cv.INTER_AREA)
    frameRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = pose.process(frameRGB)
    landMarks = []
    if results.pose_landmarks != None:
        #mpDraw.draw_landmarks(frame, results.pose_landmarks, mp.solutions.pose.POSE_CONNECTIONS)    
        #print(results.pose_landmarks)
        for land in results.pose_landmarks.landmark:
            #print((land.x, land.y))
            landMarks.append((int(land.x*width),int(land.y*height)))
        #print(landMarks[0])
        
        cv.circle(frame, landMarks[0],circleRad,circleColor,circleThickness)
        cv.circle(frame,landMarks[2],eyeRadius,eyeColor,eyeThickness)
        cv.circle(frame,landMarks[5],eyeRadius,eyeColor,eyeThickness)
        
    cv.imshow("frame",frame)
    cv.moveWindow("frame", 0, 0)
    
    if cv.waitKey(1) & 0xff==ord("q"):
        break

cap.release()

