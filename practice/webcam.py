import cv2 as cv
import numpy as np

# for default camera index=0
cap=cv.VideoCapture(0)   

cv.namedWindow("Image")

ret, frame=cap.read()

if ret:
    cv.imshow("Image",frame)
    cv.waitKey(0)
else:
    print("No frames available")

cap.release()

cv.destroyAllWindows()