import cv2 as cv

#reading frame
img = cv.imread("Photos/dog.jpg")

#for everything such as photo, live videos, videos..
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width, height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
    
resized_image = rescaleFrame(img)

#video capture
cap = cv.VideoCapture("Videos/2.mp4")

while cap.isOpened():
    _, frame = cap.read()
    cv.imshow("Video", frame)
    
    if cv.waitKey(20) and 0xFF==ord("q"):
        break
    
cap.release()
cap.destroyAllWindows()

#for videos and live shows..
def changeRes(width, height):
    cap.set(3, width)
    cap.set(4,height)

#show frame
cv.imshow("Dog", resized_image)
    
#create delay
cv.waitKey(0)


