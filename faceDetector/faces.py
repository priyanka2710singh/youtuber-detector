import numpy as np
import cv2
import pickle

# trained models directory
MODEL_DIR = "..\\resources\\models\\"

# saved pickle directory
PICKLE_DIR = "..\\resources\\pickles\\"

# haar cascades classifier
face_cascade = cv2.CascadeClassifier('../resources/cascades/data/haarcascade_frontalface_alt2.xml')

# face recognizer
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# trained data
face_recognizer.read(MODEL_DIR + "face_recognizer.yml")

# opening the labels pickle
labels = dict()
with open(PICKLE_DIR + "labels.pickle", "rb") as file:
    labels = pickle.load(file)
labels = {v: k for k, v in labels.items()}

# getting the video source
cap = cv2.VideoCapture("../resources/v.mp4")

# labels for the youtube videos
# todo

while cap.isOpened():
    ret, frame = cap.read()

    frame = cv2.resize(frame, (0, 0), fx=0.7, fy=0.7)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    """
        this will give us the face
        x will be the x coordinate, y will be the y coordinate, 
        w will be the width of the face and h will be the height of the face
        so if we take a slice of y to y+h and x to x+h, we can get the face that is detected 
        in the frame.
    """
    for (x, y, w, h) in faces:
        multiple_people = False
        # print(len(faces))

        if len(faces) > 1:
            pass
            multiple_people = True # handle multiple faces here

        roi_gray = gray[y:y+h, x:x+w]
        roi_clr = frame[y:y+h, x:x+w]

        # resize the roi_gray
        roi_gray = cv2.resize(roi_gray, (550, 550))

        # recognizing the faces
        id_, confidence = face_recognizer.predict(roi_gray)
        people = list()
        if confidence >= 45:
            name = labels[id_]
            people.append(name)
            if not multiple_people:

            # todo: get the youtube video here and replace the face with the youtube video
                me = cv2.imread("../resources/me.jpg")
                me = cv2.resize(me, (h, w))
                frame[y:y+h, x:x+w] = me

                cv2.putText(frame, name, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)
            else:
                print("multiple people detected")
                print("whose video do you wanna play?")
                for n in people:
                    print(n)
        #         todo: open a prompt to ask for whose video u wanna play


        #     specifying the color to draw a rectangle around the face
        # TODO: instead of drawing a rectangle on the face, replace the face with the youtube video
        color = (255, 0, 0)  # (blue, green, red) 0-255
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x-50, y-50), (end_cord_x+50, end_cord_y+50), color=color, thickness=stroke)

    cv2.imshow("frame", frame)

    if cv2.waitKey(30) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()