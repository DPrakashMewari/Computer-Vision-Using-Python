import cv2
cap = cv2.VideoCapture('mymov.mp4')

if cap.isOpened() == False:
    print("Error File not found")
while cap.isOpened():
    ret,frame = cap.read()
    if ret == True:
        cv2.imshow('frame',frame)
        if cv2.waitKey(10) & 0xff == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
