import cv2
import numpy as np

# Defining Image structure
img = np.zeros((500,500,3),dtype='uint8')
# Defining Font type
font = cv2.FONT_ITALIC
# Put text has some parameter which we can see when we call it
cv2.putText(img,"Prakash",(100,100),font,3,(255,255,255),4,cv2.LINE_8)
# To show
cv2.imshow("dark",img)
# Till that we press any key
cv2.waitKey(0)
cv2.destroyAllWindows()

