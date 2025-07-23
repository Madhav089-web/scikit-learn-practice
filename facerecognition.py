import cv2
image = cv2.imread('test.jpg')
image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=3)

# gray_img=cv2.resize(gray_img,(880,1430))
# print(gray_img.shape)

# faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)
for (x, y, w, h) in faces:
    print((x, y, w, h))
    image=cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
# image=cv2.resize(image,(880,1430))
cv2.imshow('Detected Faces', image)
cv2.waitKey(0)
cv2.destroyAllWindows()