import cv2 as cv

img =cv.imread('cat.jpg')

#converting to grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
cv.waitKey(1)

# blur
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT) #2nd param-> intensity of img to be blur
cv.imshow("Blur",blur)
cv.waitKey(1)

# edge cascade 
canny = cv.Canny(img,125,175)    # gives back mig with white edges
cv.imshow('canny',canny)
cv.waitKey(1)

# dilating the img
dilated=cv.dilate(canny,(7,7),iterations=1)
cv.imshow('dilated',dilated)
cv.waitKey(1)

# resize
resized = cv.resize(img,(500,500))
cv.imshow('resized',resized)
cv.waitKey(1)

# cropping
cropped = img[100:200,400:400]
cv.imshow('cropped',cropped)
cv.waitKey(10000)