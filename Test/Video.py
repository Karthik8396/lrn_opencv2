import cv2
import numpy

cap=cv2.VideoCapture(0) #first webcam
fourcc =cv2.VideoWriter_fourcc(*'XVID') # for saving the video and fourcc is codec
out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))  # adding codec and size of video
cv2.VideoWriter()
while True :
    ret,frame = cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):   #waitkey return 32 bit value(32 ones) 0xFF is 11111111(8 bit value),logical and makes it true and if executes
        break                               #ord is for getting key value
cap.release()
out.release()
cv2.destroyAllWindows()