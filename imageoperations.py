import numpy as np
import cv2

img=cv2.imread('panda.jpg',cv2.IMREAD_COLOR)

img[640,320]=[255,255,255] # getting color values from img
px =img[640,320]  # stoes the color value (BGR)

img[100:200,100:200]=[255,255,255] # setting a range of img pixels to white color

face = img[250:350,250:350]   # getting a sub-picture from image
img[0:100,0:100] = face       # copying the sub-picture to image


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()