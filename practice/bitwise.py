import cv2 as cv
import numpy as np

# Pixel -> ON ->if 1
# Pixel -> OFF->IF 0

blank = np.zeros((400,400),dtype='uint8')

rect=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circ=cv.circle(blank.copy(),(200,200),200,355,-1)

cv.imshow('Rect',rect)
cv.imshow('Circ',circ)
cv.waitKey(0)