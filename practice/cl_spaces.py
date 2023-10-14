import cv2 as cv
import matplotlib.pyplot as plt

# opencv displays a BGR img while matplotlib displays it as RGB img 
# and so we have iversion in colors in both the imgs
img = cv.imread('cat.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

plt.imshow(img)
plt.show()

hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)        # lab is washed down version of hsv

rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)
cv.waitKey(1000)

plt.imshow(rgb)
plt.show()