import os
import numpy as np
from PIL import Image
import cv2
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "images")

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml')
recogniser = cv2.face.LBPHFaceRecognizer_create()

current_id = 0
label_ids = {}
y_labels = []
x_train = []

for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root, file)
            label = os.path.basename(os.path.dirname(path)).replace(" ", "-").lower()
            print(label, path)
            if not label in label_ids:
                label_ids[label] = current_id
                current_id += 1
            id_ = label_ids[label]
            print(label_ids)
            # y_labels.append(label)
            # x_train.append(path)
            pil_image = Image.open(path).convert("L") # turns into grayscale
            # size = (550, 550)
            # final_image = pil_image.resize(size, Image.ANTIALIAS)
            image_array = np.array(pil_image, "uint8") # turns into numpy array ; #if resizing change pil_image to final_image
            print(image_array)
            faces = face_cascade.detectMultiScale(image_array, 1.1, 4)

            for (x,y,w,h) in faces:
                roi = image_array[y:y+h, x:x+w]
                x_train.append(roi)
                y_labels.append(id_)


# print(y_labels)
# print(x_train)

with open("labels.pickle", "wb") as f:
    pickle.dump(label_ids, f)

recogniser.train(x_train, np.array(y_labels))
recogniser.save("trainner.yml")