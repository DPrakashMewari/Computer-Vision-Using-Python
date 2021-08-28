import cv2
from cv2 import *
import imutils
from imutils import *

cap = cv2.VideoCapture(0)
# Intialize weidth and height
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# Saving video
vid = cv2.VideoWriter('mymov.mp4',cv2.VideoWriter_fourcc(*'XVID'),20,(width,height))


while True:
    ret,frame = cap.read()
    # Saving frame
    vid.write(frame)
    # Covert frame into GrayScale
    #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
vid.release()
cv2.destroyAllWindows()