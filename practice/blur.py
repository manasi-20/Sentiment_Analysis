import cv2 as cv

img = cv.imread('cat.jpg')

# Averaging blur (avg of surrounding pixels)
avg = cv.blur(img,(7,7))
cv.imshow('avg',avg)

# Gaussian blur (each pixel in window is given a weight)
gaus = cv.GaussianBlur(img,(7,7),0)
cv.imshow('GaussianBlur',gaus)

# Median blur (meadian of surrounding pixels)
median = cv.medianBlur(img,7)   # automatically assumes other 7
cv.imshow('medianBlur',median)

# Bilateral blur (most effective)
bilateral=cv.bilateralFilter(img,5,15,15)
cv.imshow('Bilateral',bilateral)

cv.waitKey(0)