# Drawing on Video
import cv2
from cv2 import *

cap = cv2.VideoCapture(0)
# Setting Width And Height
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Top left Corner
x = width // 4
y = height // 4

# Width and height of rectangle
w = width//4
h = height//4


while True:
    ret,frame = cap.read()
    cv2.rectangle(frame,(x,y),(x+w,y+h),color=(244,0,0),thickness=4)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
