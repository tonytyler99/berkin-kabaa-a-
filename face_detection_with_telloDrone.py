import cv2
import sys
from djitellopy import Tello


SET_POINT_X = 960/2
SET_POINT_Y = 720/2

#Değişkenler atadık

drone = Tello()  # drone tanımlandı
drone.connect() #drone bağlandı
drone.get_battery()


drone.streamon()  # start camera streaming
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
frame_read = drone.get_frame_read()


while True:
    # loop through frames
    # ret, frame = video_capture.read()  # used to collect frame from alternative video streams

    frame = drone.get_frame_read().frame  # capturing frame from drone
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Gri çevirdik

    faces = faceCascade.detectMultiScale(  # face detection
        gray,
        scaleFactor=1.1,  #Görüntü boyutunu küçültcek parametre
        minNeighbors=5,   #Karenin min kaç komşusu olucak
        minSize=(30, 30), #Minimum olası nesne boyutu,bundan küçükler gözardı edilir.

        flags=cv2.CASCADE_SCALE_IMAGE
    )
    i = 0
#Döngüyü oluşturmak için i=0
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)  # Diktörtgen tanımlama
        cv2.circle(frame, (int(x + w / 2), int(y + h / 2)), 12, (255, 0, 0), 1)  #Circle oluşturma

        cv2.circle(frame, (int(SET_POINT_X), int(SET_POINT_Y)), 12, (255, 255, 0), 8)
        i = i + 1
        distanceX = x + w / 2 - SET_POINT_X
        distanceY = y + h / 2 - SET_POINT_Y

        up_down_velocity = 0
        right_left_velocity = 0


        cv2.imshow('Video', frame)  # mostra il frame sul display del pc

        if cv2.waitKey(1) & 0xFF == ord('q'):  # quit from script
            break
cv2.destroyAllWindows()
quit()