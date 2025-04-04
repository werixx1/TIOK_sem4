import numpy as np
import cv2

# Zadanie 1
image = cv2.imread("rel.jpg")
roi = image[0:100, 0:100]
cv2.imshow("Zadanie 1", roi)
cv2.waitKey(0)

# Zadanie 2
(h, w) = image.shape[:2]
polowa_h = h // 2
roi = image[polowa_h:h, 0:w]
cv2.imshow("Zadanie 2", roi)
cv2.waitKey(0)

# Zadanie 3
polowa_w = w // 2
roi = image[0:h, polowa_w:w]
cv2.imshow("Zadanie 3", roi)
cv2.waitKey(0)

# Zadanie 4
startX = int(input("Podaj startX: "))
endX = int(input("Podaj endX: "))
startY = int(input("Podaj startY: "))
endY = int(input("Podaj endY: "))
roi = image[startX:endX, startY:endY]
cv2.imshow("Zadanie 4", roi)

# Zadanie 5
polowa = h // 2
roi = image[polowa-170:polowa+50, polowa-100:polowa+100]
cv2.imshow("Zadanie 5", roi)
cv2.waitKey(0)

# Zadanie 6
roi = image[0:100, 0:100]
image[50:150, 50:150] = roi
cv2.imshow("Zadanie 6", image)
cv2.waitKey(0)

# Zadanie 7
jedna_trzecia = h // 3
for i in range(3):
    for j in range(3):
        cropped = image[i * jedna_trzecia:(i + 1) * jedna_trzecia, j * jedna_trzecia:(j + 1) * jedna_trzecia]
        cv2.imshow(f"Czesc {i},{j}", cropped)
        cv2.waitKey(0)

# Zadanie 8 - bledne ?
start = 0
step = 10
s = w // 3
while True:
    end = min(start + s, w)
    roi = image[:, start:end]
    start += step
    cv2.imshow("Zadanie 8", roi)
    cv2.waitKey(0)
    if start + s > w:
        break

# Zadanie 9
cv2.imwrite("cropped_image.jpg", image[0:300, 0:300])
