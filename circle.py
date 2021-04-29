import numpy as np
import cv2

image = np.zeros((500,500,3),dtype='uint8')
color = (255,0,255)
cv2.circle(image,(228,229),50,color)
cv2.imshow('dark',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

