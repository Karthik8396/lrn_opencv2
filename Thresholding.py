import cv2
import numpy as np

img1 = cv2.imread('bookpage.jpg')
retval,threshold= cv2.threshold(img1,12,255,cv2.THRESH_BINARY)  #color threshold
grayscaled =cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY) #graysacled

retval2,threshold2= cv2.threshold(grayscaled,12,255,cv2.THRESH_BINARY) # applying threshold to grayscaled image

gaus =cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1) # guasian threshold

cv2.imshow('img',img1)
cv2.imshow('threshold',threshold2)
cv2.imshow('gauss',grayscaled)
cv2.waitKey(0)
cv2.destroyAllWindows()