from pickletools import uint8
import cv2 as cv
import numpy as np
#mouse click function
evt = 0
xVal = 0
yVal = 0
def mouseClick(event , xPos, yPos, flags, params):
    global evt
    global xVal
    global yVal
    
    if event == cv.EVENT_LBUTTONDOWN:
        print(event)
        xVal = xPos
        yVal = yVal
        evt = event 
    if event == cv.EVENT_LBUTTONUP:
        print(event)
        evt = event

#default parameter
width = 640
height = 360
fps = 120

cap = cv.VideoCapture(0, cv.CAP_DSHOW)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, height)
cap.set(cv.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv.CAP_PROP_FPS, fps)
cap.set(cv.CAP_PROP_FOURCC, cv.VideoWriter_fourcc(*"MJPG"))

#mouse click operation
cv.namedWindow("frame")
cv.setMouseCallback("frame", mouseClick)

while cap.isOpened(): 
    _ , frame = cap.read()
    if evt == 1:
        x = np.zeros([250,250, 3], dtype=np.uint8)
        clr = frame[yVal][xVal]
        print(clr)
        x[:,:] = clr
        cv.putText(x, str(clr),(0,50),cv.FONT_HERSHEY_COMPLEX,1,(255,255,255),1)
        cv.imshow("Color picker", x)
        cv.moveWindow("Color picker", width, 0)
        evt = 0

    cv.imshow("frame",frame)
    cv.moveWindow("frame", 0, 0)
    
    if cv.waitKey(1) and 0xff==ord("q"):
        break

cap.release()
cv.destroyAllWindows()