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

    kernel=np.ones((5,5),np.uint8)
    erosion=cv2.erode(mask,kernel,iterations=1)
    dilate = cv2.dilate(mask, kernel, iterations=1)
    opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel) #adds false positive matching to mask
    close=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel) #adds false negative matching to mask
    cv2.imshow('Frame', frame)
    cv2.imshow('open',opening)
    cv2.imshow('close',close)
    cv2.imshow('res', res)
    cv2.imshow('dilation',dilate)
    cv2.imshow('erosion',erosion)



    k=cv2.waitKey(5) & 0xFF
    if k==27:
        break

cv2.destroyAllWindows()
cap.release()