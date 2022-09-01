import cv2
import numpy as np
import pickle
import datetime
import os
# import main


face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml')
recogniser = cv2.face.LBPHFaceRecognizer_create()
recogniser.read("trainner.yml")

labels = {"person_name: 1"}
with open("labels.pickle", "rb") as f:
    og_labels = pickle.load(f)
    labels = {v:k for k,v in og_labels.items()}

cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        # print(x,y,w,h)
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]

        id_, conf = recogniser.predict(roi_gray)
        if conf >= 55 and conf <= 95:
            print(id_)
            # print(labels[id_])
            time_arrive = datetime.datetime.now().strftime("%H:%M:%S")
            print(time_arrive)
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            print(name)
            color = (255, 255, 255)
            stroke = 2
            cv2.putText(img, name, (x,y), font, 1, color, stroke, cv2.LINE_AA)
 

    cv2.imshow('img', img)

    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
    # count = 0
    m = cv2.waitKey(30) & 0xff
    # print(m)
    if m==13:
        print("Enter")
        os.system('table.py')
        # img_item = "takenimages/{}{}.png".format(name, count)
        # cv2.imwrite(img_item, roi_gray)
        # count += 1

cap.release()


# cv2.destroyAllWindows()