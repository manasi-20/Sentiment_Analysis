import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('nature.jpg')

# Grayscale histogram
gray=cv.cvtColor(img,cv.COLOR_RGB2GRAY)
gray_hist=cv.calcHist([gray],[0],None,[256],[0,256])
plt.figure()
plt.title('Gray Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])

# RGB histogram
'''
blank=np.zeros(img.shape[:2],dtype='uint8')
circle=cv.circle(blank.copy(),[img.shape[1]//2,img.shape[0]//2],200,255,-1)
mask=cv.bitwise_and(img,img,mask=circle)'''
plt.figure()
plt.title('RGB Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors=('b','g','r')
for i,col in enumerate(colors):
    hist=cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()