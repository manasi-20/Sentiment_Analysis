import cv2 as cv

img=cv.imread('cat.jpg')
gray=cv.cvtColor(img,cv.COLOR_RGB2GRAY)
# simple threshold
# threshold_val=150    thresh=binary_img
# by default maxValue=255 -> value assigned to pixels greater than 150
threshold_val,thresh=cv.threshold(img,150,255,cv.THRESH_BINARY_INV)
cv.imshow('threshold image',thresh)

#Adaptive threshold -> don't have to give manual threshold value 
#                      instead comp optimizes the value by itself
adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('Adaptive thresh',adaptive_thresh)

cv.waitKey(0)