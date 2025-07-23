import cv2
# import  face.recognizer
test_img = cv2.imread("test.jpg")
gray = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)




face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = face_cascade.detectMultiScale(gray, 1.1, 5)
label_map = {
    0: "aham",
    1: "shaheer"
}

for (x, y, w, h) in faces:
    face_roi = gray[y:y+h, x:x+w]
    face_roi = cv2.resize(face_roi, (200, 200))  # Must match training size
    label, confidence = recognizer.predict(face_roi)

    print(f"Label: {label}, Confidence: {confidence}")
    print("Recognized as:", label_map[label])

    cv2.rectangle(test_img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.putText(test_img, f"{label_map[label]} ({int(confidence)})", (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)