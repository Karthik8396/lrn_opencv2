import cv2
import numpy as np



#adding a image to another img
img1 = cv2.imread('panda.jpg')
#img2 = cv2.imread('panda_gray.jpg')

img2 = cv2.imread('python.jpg')


#add=img1+img2   #adding two images
#add=cv2.add(img1,img2) #adding the pixel value causes to go to white
#w=cv2.addWeighted(img1,0.6,img2,0.4,0)

rows,cols,channels=img2.shape  #getting the size(rols and cols) of img2
roi= img1[0:rows,0:cols]       #getting the region of interest from img1 same size as img2 to paste the img2 on img1
img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY )  #converting the image to gray scale

ret,mask=cv2.threshold(img2gray,235,255,cv2.THRESH_BINARY_INV) # converting the greyscale image to black and white image and inversing it based on threshold

mask_inv=cv2.bitwise_not(mask) # inverting the mask (b/w image)

img1_bg=cv2.bitwise_and(roi,roi,mask=mask_inv) # adding the inverted mask to img

img2_fg=cv2.bitwise_and(img2,img2,mask=mask) # adding the mask to img2 to get the color

dst=cv2.add(img1_bg,img2_fg)

img1[0:rows,0:cols] = dst
cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()