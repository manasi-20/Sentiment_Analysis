import cv2 as cv
# Reading imgs
img = cv.imread('cat.jpg')
cv.imshow('cat',img) #shows img
cv.waitKey(0) #waits for key to be pressed

# Reading video
capture = cv.VideoCapture('dog.mp4')      # instance of capture
while True:                               # loop for continous reading video
    isTrue,frame=capture.read()           # read frame
    cv.imshow('video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):   # wait till key is pressed break if 'd' is pressed
        break
capture.release()
cv.destroyAllWindows()