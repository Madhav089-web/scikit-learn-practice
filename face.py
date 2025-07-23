import cv2
import os
import numpy as np


data_path = 'test/' 
people = os.listdir(data_path)
print("Found classes:", people)

faces = []
labels = []
label_map = {}

for label, person in enumerate(people):
    label_map[label] = person  
    person_folder = os.path.join(data_path, person)
    for image_name in os.listdir(person_folder):
        img_path = os.path.join(person_folder, image_name)
        print("Loading:", img_path)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            continue
        img = cv2.resize(img, (200, 200))
        faces.append(img)
        labels.append(label)

faces = np.array(faces)
labels = np.array(labels)


recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(faces, labels)

print("Model trained and saved.")


test_img_path = "cat.jpg"
test_img = cv2.imread(test_img_path)
gray = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)
gray_resized = cv2.resize(gray, (200, 200))

label, confidence = recognizer.predict(gray_resized)
if confidence < 70:
   cv2.putText(test_img, f"{label_map[label]} ({int(confidence)})", 
            (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
else:
    print("Unknown / Not confident")
    cv2.putText(test_img, "Unknown / Not confident", 
            (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)




cv2.imshow("Recognition Result", test_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
