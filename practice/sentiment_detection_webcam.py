import cv2 as cv
import numpy as np

p=['angry','sad','happy']
haar_cascade=cv.CascadeClassifier('haar_face.xml')

# features=np.load('fetaures.npy')
# labels=np.load('labels.npy')

face_recognizer=cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('emotion_trained.yml')


img=cv.VideoCapture(0)
ret, frame=img.read()
gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

face_rect=haar_cascade.detectMultiScale(gray,1.1,13)

for (x,y,w,h) in face_rect:
    face_roi=gray[y:y+h,x:x+w]

    label,confidence=face_recognizer.predict(face_roi)
    print(f'Label={p[label]} with a confidence of {confidence}')

    cv.putText(frame,str(p[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)
    cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('Detected face',frame)
cv.waitKey(0)