import cv2 as cv

img=cv.imread('jersey.jpg')
'''
face detection uses edges for detection and colors doesn't matter
We need pretrained models(trained using data) to detect face
opencv cv provides us readymade classifiers for fd 
and one of it is haar_cascade_frontalface_default->haar_face.xml
'''
gray=cv.cvtColor(img,cv.COLOR_RGB2GRAY)
# CascadeClassifier class will read haar_face.xml and store it in haar_cascade
haar_cascade=cv.CascadeClassifier('haar_face.xml')
# minNeighbors=no. of pixels u want to call a face
faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=22)
print(f'No. of faces found in img is {len(faces_rect)}')
for(x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv.imshow('Detected face',img)
#print(faces_rect)

cv.waitKey(0)