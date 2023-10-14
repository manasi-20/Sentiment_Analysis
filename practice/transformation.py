import cv2 as cv
import numpy as np

img = cv.imread('cat.jpg')

# Transformation
def translate(img,x,y): # x,y no, of pixels we want to shift in x and y axis
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])       #shape=[height,width,channels]
    return cv.warpAffine(img,transMat,dimensions)

''' 
-x -> left
-y -> up
+x -> right
+y -> down     
'''
translated=translate(img,-100,100)
cv.imshow('Translated',translated)
cv.waitKey(10)

# Rotation
def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]

    if(rotPoint is None):
        rotPoint=(width//2,height//2)    # center rotation
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0) # rotpt,angle,scale
    dimensions=(width,height)
    return cv.warpAffine(img,rotMat,dimensions)

# +ve angle -> clockwise
# -ve angle -> anticlockwise
rotated=rotate(img,-45)
cv.imshow('Rotated',rotated)
cv.waitKey(10)
# can rotate rotated img
rotated_rotated = rotate(rotated,-45)
cv.imshow('Double Rotated',rotated_rotated)
cv.waitKey(10)

# Flipping
flip=cv.flip(img,0)   
'''
flip code = 0 -> flip vertically
            1 -> flip horizontally
           -1 -> flip both H & V
'''
cv.imshow('Flip',flip)
cv.waitKey(10)

# cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped',cropped)
cv.waitKey(10000)