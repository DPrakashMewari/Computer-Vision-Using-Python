import cv2

img = cv2.imread("image1.jpg")
# To save image in your format png,jpg,etc
img1 = cv2.imwrite("image1.png",img)
cv2.imshow('image1',img)
cv2.waitKey(0)
cv2.destroyAllWindows()