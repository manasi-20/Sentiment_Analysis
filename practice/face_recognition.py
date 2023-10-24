import cv2 as cv
import numpy as np

p=['Sundar Pichai','Priyanka Chopra','Amitabh Bachchan']
haar_cascade=cv.CascadeClassifier('haar_face.xml')

# features=np.load('fetaures.npy')
# labels=np.load('labels.npy')

face_recognizer=cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')


img=cv.imread(r'D:\My Data\projects\major\Sentiment_Analysis\practice\validation\sundar.jpg')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

face_rect=haar_cascade.detectMultiScale(gray,1.1,4)

for (x,y,w,h) in face_rect:
    face_roi=gray[y:y+h,x:x+w]

    label,confidence=face_recognizer.predict(face_roi)
    print(f'Label={p[label]} with a confidence of {confidence}')

    cv.putText(img,str(p[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('Detected face',img)
cv.waitKey(0)