import cv2 as cv

#mouse click function
evt = 0
def mouseClick(event , xPos, yPos, flags, params):
    global evt
    global pnt
    
    if event == cv.EVENT_LBUTTONDOWN:
        print("Mouse event was: ", event)
        print("at Position", xPos, yPos)
        pnt = (xPos, yPos)
        evt = event 
    if event == cv.EVENT_LBUTTONUP:
        print("Mouse event was: ", event)
        print("at Position", xPos, yPos)
        evt = event
    if event == cv.EVENT_RBUTTONUP:
        print("Right button  was: ", event)
        pnt = (xPos, yPos)
        evt = event 
#default parameter
width = 1280
height = 720
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

    if evt == 1 or evt == 4:
        cv.circle(frame, (pnt), 25, (255,0,0), 2)
    
    cv.imshow("frame",frame)
    cv.moveWindow("frame", 0, 0)
    
    if cv.waitKey(1) and 0xff==ord("q"):
        break

cap.release()
cv.destroyAllWindows()