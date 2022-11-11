from turtle import width
import cv2 as cv

#reading frame
# img = cv.imread("Photos/cat2.jpeg")

# #show frame
# cv.imshow("Dog", img)


# #create delay
# cv.waitKey(0)

#video capture

height = 1280
width = 720
fps = 120

cap = cv.VideoCapture(0, cv.CAP_DSHOW)

cap.set(cv.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, height)
cap.set(cv.CAP_PROP_FPS, fps)
cap.set(cv.CAP_PROP_FOURCC, cv.VideoWriter_fourcc(*"MJPG"))

while cap.isOpened():
    _, frame = cap.read()
    cv.imshow("Video", frame)
    cv.moveWindow("Video", 0,0)
    if cv.waitKey(20)  &  0xff==ord("q"):
        break

cap.release()
cv.destroyAllWindows()