import numpy as np
import cv2

# Zadanie 1
image = cv2.imread('hej.jpg')
M = np.ones(image.shape, dtype="uint8") * 50
zad1_cv = cv2.add(image, M)
zad1_numpy = image + 50
combined = np.hstack((zad1_numpy, zad1_cv))
cv2.imshow("Zadanie 1", combined)
cv2.waitKey(0)

# Zadanie 2
zad2_numpy = image +150
M = np.ones(image.shape, dtype="uint8") * 150
zad2_cv = cv2.add(image, M)
combined = np.hstack((zad2_numpy, zad2_cv))
cv2.imshow("Zadanie 2", combined)
cv2.waitKey(0)

# Zadanie 3
zad3_numpy = image - 80
M = np.ones(image.shape, dtype="uint8") * 80
zad3_cv = cv2.subtract(image, M)
combined = np.hstack((zad3_numpy, zad3_cv))
cv2.imshow("Zadanie 3", combined)
cv2.waitKey(0)

# Zadanie 4
b = image[:, :, 0]
g = image[:, :, 1]
r = image[:, :, 2]
r+=30
g-=20
b+=10
image_filter = cv2.merge([b, g, r])
cv2.imshow("Zadanie 4", image_filter)
cv2.waitKey(0)

# Zadanie 5
im1 = cv2.imread('1.png')
im2 = cv2.imread('2.png')
im2 = cv2.resize(im2, (im1.shape[1], im1.shape[0]))
roznica = cv2.absdiff(im1, im2)
print(roznica)
# wynik pokazuje roznice w kolorach poszczegolnych pixeli na obrazkach
