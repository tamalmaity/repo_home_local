import cv2

face_cascade = cv2.CascadeClassifier ('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier ('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (fx,fy,fw,fh) in faces:
        cv2.rectangle(img, (fx,fy), (fx+fw, fy+fh), (255,0,0), 2)

        face_roi_gray = gray[fy:int((fy+fh)*0.5), fx:fx+fw]     #Since eyes will be inside face and at top half of face
                                                                # (hopefully :P )
        face_roi_img = img[fy:int((fy+fh)*0.5), fx:fx+fw]

        eyes = eye_cascade.detectMultiScale(face_roi_gray)

        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(face_roi_img, (ex, ex+ew), (ey, ey+eh), (0,0,255), 2)

    cv2.imshow('img', img)
    k = cv2.waitKey(30) and 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
