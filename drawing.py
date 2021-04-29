import numpy as np
import cv2
# Defining pic using numpy
pic = np.zeros((500,500,3),dtype='uint8')
# Rectangle it is function that can make any type of shape
cv2.rectangle(pic,(23,23),(493,495),(132,123,98),3,lineType=0,shift=0)
# It is to show the image
cv2.imshow('dark',pic)
# Our image will wait till the we press 0
cv2.waitKey(0)
# for destroy the frame that just created
cv2.destroyAllWindows()