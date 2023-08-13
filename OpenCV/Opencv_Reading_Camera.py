import cv2 
import sys



s = 0 

if len(sys.argv) > 1:
	s = sys.argv[1]
wind = "Window"
source = cv2.VideoCapture(s)
while cv2.waitKey(1) != 27:
	hs,frame = source.read()
	if not hs:
		break 
	ch = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	cv2.imshow(wind,ch)
source.release()
cv2.destroyWindow(wind) 