import cv2 as cv

img = cv.imread("Photos/cat1.jpg")
cv.imshow("Cat", img)


# converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("CatGray", gray)

# blur
blur = cv.GaussianBlur(img,(3,3), cv.BORDER_DEFAULT)
cv.imshow("Catblur", blur)

# Edge Cascade
canny = cv.Canny(img, 125,175)
cv.imshow("CatCanny", canny)

#dilating the image
dilated = cv.dilate(canny, (5,5), iterations=3)
cv.imshow("CatDilated", dilated)

#eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow("CatEroded", eroded)

#resize
resize  = cv.resize(img, (500,700), interpolation=cv.INTER_AREA)
cv.imshow("CatResize", resize)

#Cropping
cropped = img[:]
cv.imshow("CatCropped", cropped)


cv.waitKey(0)
