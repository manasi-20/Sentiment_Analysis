import cv2 as cv
import numpy as np

img = cv.imread('cat.jpg')
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
canny = cv.Canny(blur,125,125)

# threshold img i.e converting into binary form
ret, thresh = cv.threshold(canny,125,255,cv.THRESH_BINARY) # binarizes the img
#cv.imshow('Threshold',thresh)

blank = np.zeros(img.shape,dtype='uint8')

# findcontours detects color changes in imgs
contours, hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours found') 

# draw contours on blank img
#           blank img,con_img,no.of con,color,thickness
cv.drawContours(blank,contours,-1,(0,0,255),2)
cv.imshow("Contours drawn",blank)
cv.waitKey(10000)