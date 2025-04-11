# Zadanie 1
import cv2
import numpy as np
canvas = np.zeros((300, 300), dtype="uint8")
points = np.array([[150, 30], [30, 270], [270, 270]])
triangle = points.reshape((-1, 1, 2)) # dla drawContours aby kontury byly w dobrym formacie
cv2.drawContours(canvas, [triangle], 0, 255, -1)
circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 130, 255, -1)

bitwiseAnd = cv2.bitwise_and(canvas, circle)
bitwiseOr = cv2.bitwise_or(canvas, circle)
bitwiseXor = cv2.bitwise_xor(canvas, circle)
bitwiseNot = cv2.bitwise_not(canvas)
combined = np.hstack((bitwiseAnd, bitwiseOr, bitwiseXor, bitwiseNot))
cv2.imshow("Zadanie 1", combined)
cv2.waitKey(0)

# Zadanie 2
im1 = cv2.imread("2_1.jpeg")
im2 = cv2.imread("2_2.jpeg")
differences = cv2.bitwise_xor(im1, im2)
cv2.imshow("Zadanie 2", differences)
cv2.waitKey(0)