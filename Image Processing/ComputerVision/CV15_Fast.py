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

findFaces = mp.solutions.face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5)
drawFaces = mp.solutions.drawing_utils


while cap.isOpened():
    _ , frame = cap.read()
    frame = cv.flip(frame,1)
    frame = cv.resize(frame, (width,height), interpolation= cv.INTER_AREA)
    frameRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    
    results = findFaces.process(frameRGB)
    #print(results.detections)
    
    if results.detections != None:
        for face in results.detections:
            #drawFaces.draw_detection(frame,face)
            bBox = face.location_data.relative_bounding_box
            topLeft = (int(bBox.xmin*width),int(bBox.ymin*height))
            bottomRight = (int((bBox.xmin+bBox.width)*width),int((bBox.ymin+bBox.height)*height))
            cv.rectangle(frame, topLeft, bottomRight, (0,0,255), 3)
    cv.imshow("frame",frame)
    cv.moveWindow("frame", 0, 0)
    
    if cv.waitKey(1) & 0xff==ord("q"):
        break

cap.release()

