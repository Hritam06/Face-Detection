import cv2

# Load the cascade which contains all the factors of Human Face for detection

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")




# To capture video from the Webcam

cap = cv2.VideoCapture(0)




# To use a video file as input please use this code  ----------------> cap = cv2.VideoCapture('Give the name of video file') in place of cap = cv2.VideoCapture(0) 




while True:
    # Read the frame
    _, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)

    # Display
    cv2.imshow('img', img)

    # Closes the webcam when we press the User press "c" Key........User can change the key as per choice by updating the key given below
    k = cv2.waitKey(1)
    if k==ord('c'):                                   
        break
                
# Release the VideoCapture object

cap.release()

#destroys all the running windows

cv2.destroyAllWindows()