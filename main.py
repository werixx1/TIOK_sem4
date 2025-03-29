# Zadanie 1
import cv2
import numpy as np

image = cv2.imread("gnarp.png")
flipped1 = cv2.flip(image, 0)
cv2.imshow("Zadanie 1", flipped1)
cv2.waitKey(0)

# Zadanie 2
flipped2 = cv2.flip(image, 1)
cv2.imshow("Zadanie 2-original", image)
cv2.imshow("Zadanie 2-flipped", flipped2)
cv2.waitKey(0)

# Zadanie 3
flipped3 = cv2.flip(image, -1)
cv2.imshow("Zadanie 3", flipped3)
cv2.waitKey(0)

# Zadanie 4
# bylo zrobione w poprzednich zadaniach ale oki..
combined = np.hstack((image, flipped1, flipped2, flipped3))
cv2.imshow("Zadanie 4", combined)
cv2.waitKey(0)

# Zadanie 5
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
startX, endX = cX - 100, cX + 100
startY, endY = cY - 100, cY + 100
flipped4 = cv2.flip(image[startY:endY, startX:endX], -1)
image[startY:endY, startX:endX] = flipped4
cv2.imshow("Zadanie 5", image)
cv2.waitKey(0)

# Zadanie 6
image[startY:endY, startX:endX] = cv2.flip(image[startY:endY, startX:endX], -1)
odbicie = int(input("Siemka jakie chcesz odbicie: (1-pionowe, 0-poziome, -1-oba)\n"))

if odbicie in [0, 1, -1]:
    flipped = cv2.flip(image, odbicie)
    cv2.imshow("Zadanie 6", flipped)
    cv2.waitKey(0)
else:
    print("Nie ma takiej opcji")
