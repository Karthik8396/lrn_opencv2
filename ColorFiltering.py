import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    _,frame=cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)   #hsv hue saturation value

    lower_red=np.array([0,50,50])
    upper_red=np.array([255,255,255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)  # colors only that color

    cv2.imshow('Frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    k=cv2.waitKey(5) & 0xFF
    if k==27:
        break
    #   dark_red=np.uint8([[[12,22,121]]])
    #   dark_red=cv2.cvtColor(dark_red,cv2.COLOR_BGR2HSV)

    # cv2.imshow('mask', mask)
    # cv2.imshow('res', res)
cv2.destroyAllWindows()
cap.release()