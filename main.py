# Zadanie 1
import cv2
import numpy as np

green = (0, 255, 0)
blue = (255,0,0)
red = (0, 0, 255)

canvas1 = np.zeros((300, 300, 3), dtype="uint8")
cv2.line(canvas1, (150, 150), (299, 299), blue, 2)
cv2.imshow("Zadanie 1", canvas1)
cv2.waitKey(0)

# Zadanie 2
canvas2 = np.zeros((400, 400, 3), dtype="uint8")
# a
cv2.rectangle(canvas2, (0, 0), (100, 50), green)
# b
cv2.rectangle(canvas2, (300, 350), (399, 399), red, 3)
cv2.imshow("Zadanie 2", canvas2)
cv2.waitKey(0)

# Zadanie 3
canvas3 = np.zeros((300,300,3), dtype="uint8")
(centerX, centerY) = (canvas3.shape[1] // 2, canvas3.shape[0] // 2)
cv2.circle(canvas3, (50, 50), 40, blue)
cv2.circle(canvas3, (centerX, centerY), 60, red)
cv2.imshow("Zadanie 3", canvas3)
cv2.waitKey(0)

# Zadanie 4
canvas4 = np.zeros((400,400,3), dtype="uint8")
cv2.rectangle(canvas4, (150,150), (250,250), blue)
cv2.circle(canvas4,(200, 200), 30, blue)
cv2.imshow("Zadanie 4", canvas4)
cv2.waitKey(0)

# Zadanie 5
canvas5 = np.zeros((400,400,3), dtype="uint8")
(centerX5, centerY5) = (canvas5.shape[1] // 2, canvas5.shape[0] // 2)
for size in range(20, 200, 20):
    top_left = (centerX5 - size // 2, centerY5 - size // 2)
    bottom_right = (centerX5 + size // 2, centerY5 + size // 2)
    cv2.rectangle(canvas5, top_left, bottom_right, blue, 1)
cv2.imshow("Zadanie 5", canvas5)
cv2.waitKey(0)

# Zadanie 6
profilowe = cv2.imread("profilowe.jpg")
(h, w) = profilowe.shape[:2]
(cX, cY) = (w // 2, h // 2)
cv2.circle(profilowe, (cX-80, cY), 50, red, -1)
cv2.circle(profilowe, (cX+80, cY), 50, red, -1)
cv2.rectangle(profilowe, (cX-100, cY+190), (cX+100, cY+110), green, -1)
cv2.circle(profilowe, (cX, cY),  300, blue, 2)
cv2.imshow("Zadanie 6", profilowe)
cv2.waitKey(0)
cv2.imwrite('profilowe_zmienione.jpg', profilowe)