import mediapipe
import cv2
import cvzone
import serial
from cvzone.HandTrackingModule import HandDetector

ser=serial.Serial('COM5', 9600)
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
total_fingers=0
prev_fingers = -1

detector = HandDetector(detectionCon=0.7)

while True:
    success, img = cap.read()
    hands, img = detector.findRightHand(img)
    # print(hands)
    if len(hands)== 1:
        list_fingers = detector.fingersUp(hands[0])
        total_fingers=sum(list_fingers)

    if total_fingers != prev_fingers:
        ser.write(str(total_fingers).encode())
        prev_fingers = total_fingers

    cv2.putText(img, str(total_fingers), (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 5, (100, 50, 200), thickness=5)

    # #x-axis coordination
    # img = cv2.line(img, (128, 0), (128,img.shape[1]), (255,0,0), 2)
    # img = cv2.line(img, (256, 0), (256, img.shape[1]), (0, 255, 0), 2)
    # img = cv2.line(img, (384, 0), (384, img.shape[1]), (0, 0, 255), 2)
    #
    # #y-axis coordination
    # img = cv2.line(img, (0, 128), (img.shape[1], 128), (255, 0, 0), 2)
    # img = cv2.line(img, (0, 256), (img.shape[1], 256), (0, 255, 0), 2)
    # img = cv2.line(img, (0, 384), (img.shape[1], 384), (0, 0, 255), 2)
    cv2.imshow("controller", img)
    key = cv2.waitKey(1)
    if key==27:
        break