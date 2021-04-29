import cv2
import numpy as np

img = np.zeros((500,500,3),dtype="uint8")
cv2.rectangle(img,(23,23),(493,495),(132,123,98),3,lineType=0,shift=0)
font = cv2.FONT_ITALIC
cv2.putText(img,"Prakash",(100,100),font,3,(255,255,255),4,cv2.LINE_8)
color = (255,0,255)
cv2.circle(img,(228,229),50,color)
cv2.line(img,(223,227),(479,360),(0,0,255))
cv2.imshow('Pic',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


