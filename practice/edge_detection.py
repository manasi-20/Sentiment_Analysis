import cv2 as cv
import numpy as np

img=cv.imread('cat.jpg')
gray=cv.cvtColor(img,cv.COLOR_RGB2GRAY)

# Laplacian
# src, data
lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow('Laplacian',lap)

#Sobel
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel=cv.bitwise_or(sobelx,sobely)

cv.imshow('Sobelx',sobelx)
cv.imshow('Sobely',sobely)
cv.imshow('Combined sobel',combined_sobel)

#canny
canny=cv.Canny(img,150,175)
cv.imshow('canny',canny)

cv.waitKey(0)