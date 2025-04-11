# Zadanie 1
import cv2
import numpy as np

image = cv2.imread('yea.jpg')
mask = np.zeros(image.shape[:2], dtype="uint8")
print(image.shape)
cv2.rectangle(mask, (120,100), (700,550), 255, -1)
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Zadanie 1", masked)
cv2.waitKey(0)

# Zadanie 2
mask2 = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask2, (120,240), (700,300), 255, -1)
masked2 = cv2.bitwise_not(image, image, mask=mask2)
cv2.imshow("Zadanie 2", masked2)
cv2.waitKey(0)

# Zadanie 3
img = cv2.imread('zad3.jpg')
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_blue = np.array([100, 100, 100])
upper_blue = np.array([140, 255, 255])
mask3 = cv2.inRange(hsv_img, lower_blue, upper_blue)
masked3 = cv2.bitwise_and(img, img, mask=mask3)
combined = np.hstack((img, masked3))
cv2.imshow("Zadanie 3", combined)
cv2.waitKey(0)
