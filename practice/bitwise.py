import cv2 as cv
import numpy as np

# Pixel -> ON ->if 1
# Pixel -> OFF->IF 0

blank = np.zeros((400,400),dtype='uint8')

rect=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circ=cv.circle(blank.copy(),(200,200),200,355,-1)

cv.imshow('Rect',rect)
cv.imshow('Circ',circ)

# Bitwise AND -common part
#          OR -common + non-common part
#         NOT -interchanges color
#         XOR -non common part
bit_and=cv.bitwise_and(rect,circ)
bit_or=cv.bitwise_or(rect,circ)
bit_not=cv.bitwise_not(rect)
bit_xor=cv.bitwise_xor(rect,circ)

cv.imshow('AND',bit_and)
cv.imshow('OR',bit_or)
cv.imshow('NOT',bit_not)
cv.imshow('XOR',bit_xor)

cv.waitKey(0)