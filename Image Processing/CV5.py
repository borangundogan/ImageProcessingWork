import cv2 as cv
import numpy as np

img = cv.imread("Photos/cat1.jpg")
cv.imshow("Cat", img)

#Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat,dimensions)

# -x --> Left
# -y --> Up

#  x --> Right
#  y --> Down

translated = translate(img, -100, -100)
cv.imshow("CatTranslated", translated)


#Rotation
def rotate(img, angle, rotPoint):
    (height, width) = img.shape[:2]
    
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, scale=1.0)
    dimensions = (width,height)
    
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45, (100,100))
cv.imshow("CatRotated", rotated)

#Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("CatResized", resized)

#Flipping
# 1 --> vertical axis
# 0 --> horizontal axis
# -1 --> both axis

flip = cv.flip(img , 0 )
cv.imshow("Catflip", flip)



cv.waitKey(0)