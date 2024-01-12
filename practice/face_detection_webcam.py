import cv2

cap = cv2.VideoCapture(0)

ret, frame = cap.read()

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Load the Haar cascade classifier for face detection
face_cascade = cv2.CascadeClassifier('haar_face.xml')

# Detect faces in the frame
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# Draw a bounding box around each detected face
for (x, y, w, h) in faces:
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the frame
cv2.imshow('frame', frame)
cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()