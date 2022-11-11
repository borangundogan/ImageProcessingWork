from cgitb import handler
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

maxNumberOfHands = 2
confidentTrackinNumber = 0.5
confidentDetecetionNumber = 0.5
modelComplexity = 1
#false mean is frame not static!! (we use camera)

hands = mp.solutions.hands.Hands(False, maxNumberOfHands, modelComplexity,
                                confidentDetecetionNumber, confidentTrackinNumber )

mpDraw = mp.solutions.drawing_utils

while cap.isOpened():
    _ , frame = cap.read()
    frame = cv.flip(frame,1)
    #frame = cv.resize(frame, (width,height))

    frameRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    results = hands.process(frameRGB)

    if results.multi_hand_landmarks != None:
        for handLandMarks in results.multi_hand_landmarks:
            myHand = []
            #mpDraw.draw_landmarks(frame,handLandMarks, mp.solutions.hands.HAND_CONNECTIONS)
            for landMark in handLandMarks.landmark:
                #print((landMark.x , landMark.y))
                myHand.append((int(landMark.x*width) , int(landMark.y*height)))
            print("")
            print(myHand)
            
            cv.circle(frame,myHand[20], 15, (255,0,0),-1)
            
            
            
    cv.imshow("frame",frame)
    cv.moveWindow("frame", 0, 0)
    
    if cv.waitKey(1) & 0xff==ord("q"):
        break

cap.release()