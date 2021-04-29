import cv2
import numpy as np

pic = cv2.imread('image1.png')
# Assigning cols and rows
cols = pic.shape[1]
rows = pic.shape[0]
# Define How much it should move
M = np.float32([[1,0,-150],[0,1,-70]])
# it is affine matrix multiplication
shifted = cv2.warpAffine(pic,M,(cols,rows))
# 
cv2.imshow("Shifted",shifted)
#
cv2.waitKey(0)
# destroy all windows
cv2.destroyAllWindows()