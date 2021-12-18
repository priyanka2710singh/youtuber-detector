import os
import cv2
from PIL import Image
import numpy as np
import pickle

# will give us the parent directory of this py file.
BASE_DIR = os.path.dirname((os.path.abspath(__file__)))

# saved pickle directory
PICKLE_DIR = "..\\resources\\pickles\\"

# image resources directory
IMG_DIR = "..\\resources\\faces\\"

# trained models directory
MODEL_DIR = "..\\resources\\models\\"

# data for training and labeling
x_train = []
y_labels = []
label_ids = dict()
curr_id = 0

# face classifier
face_cascade = cv2.CascadeClassifier('../resources/cascades/data/haarcascade_frontalface_alt2.xml')
# face recognizer
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

"""
    basically, we go through every image in the image dir, and for every image, we get its path and
    its parent dir, which is the name of the person that we are gonna identify.
    and we first check if there's an entry in the label_ids dict for that person, 
    and add that person based on the previous check
    then we take the id and also open the image and detect faces in it.
    we take the region of interest in the image and add it along with the id to the training dataset.
    
"""

# walking through the whole image dir
for root, dirs, files in os.walk(IMG_DIR):

    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root, file)
            label = os.path.basename(root)

            if not label in label_ids:
                label_ids[label] = curr_id
                curr_id += 1
            id_ = label_ids[label]

            # print(label_ids)

#             open the image, and convert it into numpy array
            pil_img = Image.open(path).convert("L")
            img_arr = np.array(pil_img, "uint8")

            # print(img_arr)

            faces = face_cascade.detectMultiScale(img_arr, scaleFactor=1.5, minNeighbors=5)
            for (x, y, w, h) in faces:
                roi = img_arr[y:y+h, x:x+w]
                roi = cv2.resize(roi, (550, 550))
                x_train.append(roi)
                y_labels.append(id_)

# saving the labels in pickle
with open(PICKLE_DIR + "labels.pickle", "wb") as file:
    pickle.dump(label_ids, file)

# training the recognizer
face_recognizer.train(x_train, np.array(y_labels))

# saving the trained recognizer
face_recognizer.save(MODEL_DIR + "face_recognizer.yml")



