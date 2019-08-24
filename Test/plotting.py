import cv2
import numpy as np

img = cv2.imread('panda.jpg',cv2.IMREAD_COLOR)
cv2.line(img,(0,0),(150,150),(255,0,0),15)  #drawing line
cv2.rectangle(img,(250,250),(750,500),(0,0,255),10) #drawing rectangle
cv2.circle(img,(640,320),20,(0,0,255),-1) #drawing circle thickness -1 fills up the circle

pts= np.array([[50,100],[250,100],[960,500],[50,500],[750,250]],np.int32) # points of polygon
cv2.polylines(img,[pts],True,(255,255,0),3) #drawing a polygon

font = cv2.FONT_HERSHEY_SIMPLEX  # font
cv2.putText(img,'TEST',(750,600),font,3,(0,255,255),6,cv2.LINE_AA) #writing text

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
