import cv2 as cv

img = cv.imread('cat.jpg')
cv.imshow('cat',img)
cv.waitKey(1000)
def rescale(frame,scale=0.2):    # scale=0.75 by default i.e, scales it to 0.75
    # can be used for img, video, live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
resized_img=rescale(img)
cv.imshow('cat',resized_img)
cv.waitKey(10000)
'''
# Resizing video
def rescaleVideo(width,height):
    # live video
    capture.set(3,width)
    capture.set(4,height)

capture = cv.VideoCapture('dog.mp4')      # instance of capture
while True:                               # loop for continous reading video
    isTrue,frame=capture.read()           # read frame
    frame_resized=rescale(frame,scale=0.2)
    cv.imshow('video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):   # wait till key is pressed break if 'd' is pressed
        break
capture.release()
cv.destroyAllWindows()
'''