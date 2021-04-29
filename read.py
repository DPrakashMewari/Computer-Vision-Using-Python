import cv2

# Reading a image
img = cv2.imread('image1.jpg')
# To see a image and label it
cv2.imshow('image1',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
