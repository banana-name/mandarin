import cv2

# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
cascade_smile = cv2.CascadeClassifier('haarcascade_smile.xml')
cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # for (x, y, w, h) in faces:
    #     cv2.rectangle(frame, (x, y), (x + w, y+h), (12, 123, 0), 2)
    # eyes = eye_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5)
    # for (ex, ey, ew, eh) in eyes:
    #     cv2.rectangle(frame, (ex, ey), (ex + ew, ey+ eh), (255, 0, 0), 5)
    #
    smile = cascade_smile.detectMultiScale(frame, 1.7, 20)
    for (x_smile, y_smile, w_smile, h_smile) in smile:
        cv2.rectangle(frame, (x_smile, y_smile), (x_smile + w_smile, y_smile + h_smile), (255, 0, 130), 2)


    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyWindow()