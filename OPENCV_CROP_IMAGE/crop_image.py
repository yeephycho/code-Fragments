import cv2
img = cv2.imread("test.jpg")
# crop_img = img[y:y+h, x:x+w]
crop_img = img[50:(50 + 100), 60:(60 + 100)]
cv2.imwrite("./crop_test.jpg", crop_img)
