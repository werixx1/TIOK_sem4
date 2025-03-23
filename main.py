# Zadanie 1
import argparse
import imutils
import cv2

image = cv2.imread("me.jpg")
cv2.imshow("Zadanie 1 (before)", image)
cv2.waitKey(0)
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Zadanie 1 (after)", rotated)
cv2.waitKey(0)

# Zadanie 2
M = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Zadanie 2", rotated)
cv2.waitKey(0)

# Zadanie 3
M = cv2.getRotationMatrix2D((0, 0), 30, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Zadanie 3", rotated)
cv2.waitKey(0)

# Zadanie 4
angle = int(input("Podaj kat obrotu (liczba calkowita)\n"))
M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Zadanie 4", rotated)
cv2.waitKey(0)

# Zadanie 5
rotated = imutils.rotate(image, 180)
cv2.imshow("Zadanie 5", rotated)
cv2.waitKey(0)

# Zadanie 6
rotated = imutils.rotate_bound(image, -33)
cv2.imshow("Zadanie 6", rotated)
cv2.waitKey(0)

# Zadanie 7
M = cv2.getRotationMatrix2D((cX, cY), 60, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Zadanie 7 (warpAffine)", rotated)
rotated = imutils.rotate(image, 60)
cv2.imshow("Zadanie 7 (imutils.rotate)", rotated)
cv2.waitKey(0)
# obie funkcje zwracaja te same wyniki (jedynie jest roznica w ich implementacji)

# Zadanie 8
rotated = imutils.rotate(image, 30)
rotated1 = imutils.rotate(rotated, 30)
rotated2 = imutils.rotate(rotated1, 30)
cv2.imwrite("round.jpg", rotated2)
cv2.imshow("Zadanie 8 (3x 30)", rotated2)
rotated = imutils.rotate(image, 90)
cv2.imshow("Zadanie 8 (1x 90)", rotated)
cv2.waitKey(0)

# Zadanie 9
rotated = imutils.rotate(image, 75)
cv2.imwrite("rotated_output.jpg", rotated)

#Zadanie 10
for x in range(0, 361, 15):
    rotated = imutils.rotate(image, x)
    cv2.imshow("Zadanie 10", rotated)
    cv2.waitKey(500)



