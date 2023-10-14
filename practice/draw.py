import cv2 as cv
import numpy as np

#                (height,width,color)
blank = np.zeros((500,500,3), dtype='uint8')
'''
cv.imshow('blank',blank)
cv.waitKey(0)

# paint img
blank[:]=0,255,0
cv.imshow('green',blank)
cv.waitKey(0)
'''
# put text
cv.putText(blank,'Sentiment Analysis',(95,255),cv.FONT_HERSHEY_SIMPLEX,1.0,(0,255,0),2)
cv.imshow('Text',blank)
cv.waitKey(1000)