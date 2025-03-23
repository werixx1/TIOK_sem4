# Zadanie 1
import numpy as np
import cv2
import imutils

image = cv2.imread("m.jpg")
cv2.imshow("Zadanie 1 before", image)
cv2.waitKey(0)

M1 = np.float32([[1, 0, 30],
               [0, 1, 40]])
shifted1 = cv2.warpAffine(image, M1, (image.shape[1], image.shape[0]))
cv2.imshow("Zadanie 1 after", shifted1)
cv2.waitKey(0)

# Zadanie 2
M2 = np.float32([[1, 0, -20],
               [0, 1, -50]])
shifted2 = cv2.warpAffine(image, M2, (image.shape[1], image.shape[0]))
cv2.imshow("Zadanie 2", shifted2)
cv2.waitKey(0)

# Zadanie 3
(h, w) = image.shape[:2]
M3 = np.float32([[1, 0, w/2 +10],
               [0, 1, h/2 +10]])
shifted3 = cv2.warpAffine(image, M3, (image.shape[1], image.shape[0]))
cv2.imshow("Zadanie 3", shifted3)
cv2.waitKey(0)

# Zadanie 4
shifted4 = imutils.translate(image, 100, 50)
cv2.imshow("Zadanie 4", shifted4)
cv2.waitKey(0)

# Zadanie 5
x = int(input("Podaj wartosc wartosc x: (dodatnia/ujemna)\n"))
y = int(input("Podaj wartosc wartosc y: (dodatnia/ujemna)\n"))

if abs(x) < h and abs(y) < w:
   shifted5 = imutils.translate(image, x, y)
   cv2.imshow("Zadanie 5", shifted5)
   cv2.waitKey(0)
else:
   print("Po przesunieciu obraz wychodzi poza zakres")


