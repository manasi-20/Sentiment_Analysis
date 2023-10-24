import os
import numpy as np
import cv2 as cv

p=['Sundar Pichai','Priyanka Chopra','Amitabh Bachchan']
dir=r'D:\My Data\projects\major\Sentiment_Analysis\practice'


#classifier
haar_cascade=cv.CascadeClassifier('haar_face.xml')

#training set
features=[]    #faces
labels=[]      #names-> denoted by index values

def create_train():
    for person in p:
        path=os.path.join(dir,person)
        label=p.index(person)

        for img in os.listdir(path):
            img_path=os.path.join(path,img)

            img_array=cv.imread(img_path)
            gray=cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)

            # scalefactor ^ no. of pixels ^
            # minneighbours ^ detection low
            faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                faces_roi=gray[y:y+h,x:x+w]
                features.append(faces_roi)
                labels.append(label)
create_train()
print("**** Trained ****")

#converting lists into numpy arrays
features=np.array(features,dtype='object')
labels=np.array(labels)

#instantiate face recognizer
face_recognizer=cv.face.LBPHFaceRecognizer_create()

#train the recognizer on features and labels list
face_recognizer.train(features,labels)

#to use this trained model anywhere anytime we have to save it as yml file
face_recognizer.save('face_trained.yml')

np.save('features.npy',features)
np.save('labels.npy',labels)