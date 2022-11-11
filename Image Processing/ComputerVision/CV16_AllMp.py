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

#false means it is not static image !
faceMesh = mp.solutions.face_mesh.FaceMesh( 
                                        static_image_mode=False,
                                        max_num_faces=1,
                                        refine_landmarks=True,
                                        min_detection_confidence=0.5,
                                        min_tracking_confidence=0.5
                                        )

drawMesh = mp.solutions.drawing_utils

font = cv.FONT_HERSHEY_COMPLEX
fontSize = 0.5
fontColor = (0,255,255)
fontThick = (1)

while cap.isOpened():
    _ , frame = cap.read()
    frame = cv.flip(frame,1)
    frame = cv.resize(frame, (width,height))
    frameRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    
    results = faceMesh.process(frameRGB)
    #print(results.multi_face_landmarks)
    
    if results.multi_face_landmarks != None:
        for face in results.multi_face_landmarks:
            drawMesh.draw_landmarks(
                frame, 
                face, 
                mp.solutions.face_mesh.FACEMESH_CONTOURS
                )
    
    cv.imshow("frame",frame)
    cv.moveWindow("frame", 0, 0)
    
    if cv.waitKey(1) & 0xff==ord("q"):
        break

cap.release()

