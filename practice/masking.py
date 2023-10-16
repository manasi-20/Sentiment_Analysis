import cv2 as cv
import numpy as np

img=cv.imread('cat.jpg')
blank=np.zeros(img.shape[:2],dtype='uint8')
circ=cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),200,255,-1)
rect=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
bit_and=cv.bitwise_and(circ,rect)
masked_img=cv.bitwise_and(img,img,mask=bit_and)
cv.imshow('Mask img',masked_img)
cv.waitKey(0)