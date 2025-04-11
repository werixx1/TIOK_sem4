# Zadanie 1
import cv2
import numpy as np

image = cv2.imread("zdj1.jpg")
(B, G, R) = cv2.split(image)
cv2.imshow("Zadanie 1 R", R)
cv2.imshow("Zadanie 2 G", G)
cv2.imshow("Zadanie 3 B", B)
cv2.waitKey(0)
cv2.imwrite("zad1_b.jpg", B)
cv2.imwrite("zad1_g.jpg", G)
cv2.imwrite("zad1_r.jpg", R)

# Zadanie 2
img2 = cv2.imread("zdj2.jpg")
(B2, G2, R2) = cv2.split(img2)
all = np.hstack((B2, G2, R2))
cv2.imshow("Zadanie 2 B, G, R", all)
cv2.waitKey(0)

# Zadanie 3
reordered_image = cv2.merge([R, B, G])
cv2.imshow("Zadanie 3 zmiana kolejnosci", reordered_image)
cv2.waitKey(0)
G[:] = 0
image_no_green = cv2.merge([B, G, R])
cv2.imshow("Zadanie 3 zielony jako 0", image_no_green)
cv2.waitKey(0)

# Zadanie 4
image3 = cv2.imread("zdj1.jpg")
(B3, G3, R3) = cv2.split(image)
R3 = cv2.add(R3, 50)
image_more_red = cv2.merge([B3, G3, R3])
cv2.imshow("Zadanie 4", image_more_red)
cv2.waitKey(0)

# Zadanie 5
im5 = cv2.imread("zdj5.jpg")
hsv = cv2.cvtColor(im5, cv2.COLOR_BGR2HSV)
lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])
mask5 = cv2.inRange(hsv, lower_red, upper_red)
hsv[:,:,1] = cv2.add(hsv[:,:,1], 50) # +50 do kanalu nasycenia
hsv_masked = cv2.bitwise_and(hsv, hsv, mask=mask5)
im5_with_more_red = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
both_cars = np.hstack((im5, im5_with_more_red))
cv2.imshow("Zadanie 5", both_cars)
cv2.waitKey(0)

# Zadanie 6
logo = cv2.imread("logo.png")
hsv = cv2.cvtColor(im5, cv2.COLOR_BGR2HSV)
(B6, G6, R6) = cv2.split(logo)
swapped = cv2.merge([R6, G6, B6])
(B7, G7, R7) = cv2.split(logo)
R7[:] = 0
no_red = cv2.merge([B7, G7, R7])
zad6 = np.hstack((swapped, no_red))
cv2.imshow("Zadanie 6 - zamienione kolory i bez czerwonego", zad6)
cv2.waitKey(0)
