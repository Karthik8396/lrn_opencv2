#sentdex opencv youtube

import cv2
import numpy
import matplotlib.pyplot as plt

img = cv2.imread('panda.jpg',cv2.IMREAD_GRAYSCALE)

#plt.imshow(img, cmap='gray', interpolation='bicubic')
#plt.plot([50,100],[80,100],'b',linewidth=5)
#plt.show()
cv2.imwrite('panda_gray.jpg',img)
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()





