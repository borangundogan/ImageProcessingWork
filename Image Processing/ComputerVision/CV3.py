import cv2 as cv
import numpy as np

# img = cv.imread("Photos/cat1.jpg")
# cv.imshow("Cat", img)


#0. create blank frame
blank = np.zeros((500,500, 3), dtype="uint8")
#cv.imshow("Blank", blank)

blank1 = np.zeros((500,500, 3), dtype="uint8")
cv.imshow("Blank", blank)

#1.paint the image a certain color

blank[:] = (255,0,0)
cv.imshow("Blue", blank)

blank[200:300,300:400] = (0,255,0)
cv.imshow("Green", blank)

#2.draw a rectangle
rec = cv.rectangle(blank, (0,0) , (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=cv.FILLED )#THICKNESS = -1
cv.imshow("rectangle", rec)

#3.draw a circle
circ = cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
cv.imshow("circle", circ)

#4.draw a line
line = cv.line(blank, (0,0),(blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
cv.imshow("line", line)

#5. put some text
text = cv.putText(blank1, "FPS:", (225,225), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,0,255), 2)
cv.imshow("text", text)


cv.waitKey(0)