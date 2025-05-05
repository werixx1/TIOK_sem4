# Zadanie 1
import cv2
import matplotlib.pyplot as plt
import numpy as np

img_b = cv2.imread('binary1.jpg')
kernel_r = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
kernel_e = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))

eroded_r = cv2.erode(img_b,kernel_r, iterations=5) # daje 5 iteracji aby wynik byl bardziej zauwazalny
eroded_e = cv2.erode(img_b,kernel_e, iterations=5)
cv2.imshow('Zadanie 1 - eroded_r',eroded_r)
cv2.imshow('Zadanie 1 - eroded_e',eroded_e)
cv2.waitKey(0)
# w wyniku erozji figury na zdjeciu sie zmiejszyly (przy morph_ellipse sa mniej "starte" krawedzie)

# Zadanie 2
# b
img_b2 = cv2.imread('binary2.jpg', 0)
for size in [3, 5, 9]:
    kernel_r2 = cv2.getStructuringElement(cv2.MORPH_RECT, (size, size))
    dilated = cv2.dilate(img_b2, kernel_r2, iterations=1)
    cv2.imshow("Zadanie 2 - dilated", dilated)
    cv2.waitKey(0)
# c - poprawic wykres
iterations = [1, 2, 3, 4, 5]
temp = []

for iteration in iterations:
    cv2.dilate(img_b2, kernel_r, iterations=iteration)
    thickness = cv2.countNonZero(dilated)
    temp.append(thickness)

plt.plot(iterations, temp, marker='o')
plt.style.use('dark_background')
plt.title('Zmiana grubosci a iteracje')
plt.xlabel('Liczba iteracji')
plt.ylabel('Liczba bialych pikseli')
plt.grid(True)
plt.show()

# Zadanie 3
img_noise = cv2.imread('noise.jpg', 0)

opening_1 = cv2.morphologyEx(img_noise, cv2.MORPH_OPEN, kernel_r) # 5x5
kernel_r3 = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
opening_2 = cv2.morphologyEx(img_noise, cv2.MORPH_OPEN, kernel_r3) # 3x3
cv2.imshow("Zadanie 3 - przed", img_noise)
cv2.imshow("Zadanie 3 - po (5x5)", opening_1)
cv2.imshow("Zadanie 3 - po (3x3)", opening_2)
cv2.waitKey(0)

# Zadanie 4
img_words = cv2.imread("words.jpg", 0)
closing_r = cv2.morphologyEx(img_words, cv2.MORPH_CLOSE, kernel_r)
closing_e = cv2.morphologyEx(img_words, cv2.MORPH_CLOSE, kernel_e)
cv2.imshow("Zadanie 4 - prost", closing_r)
cv2.imshow("Zadanie 4 - elip", closing_e)
cv2.waitKey(0)

# Zadanie 5
cat = cv2.imread('cat.jpg', 0)
e = cv2.erode(cat, kernel_r, iterations=5)
d = cv2.dilate(e,kernel_r, iterations=5)
o = cv2.morphologyEx(d, cv2.MORPH_OPEN, kernel_r)
c = cv2.morphologyEx(o, cv2.MORPH_CLOSE, kernel_r)
g = cv2.morphologyEx(c, cv2.MORPH_GRADIENT, kernel_r)

e2 = cv2.erode(cat, kernel_e, iterations=5)
d2 = cv2.dilate(e2,kernel_e, iterations=5)
o2 = cv2.morphologyEx(d2, cv2.MORPH_OPEN, kernel_e)
c2 = cv2.morphologyEx(o2, cv2.MORPH_CLOSE, kernel_e)
g2 = cv2.morphologyEx(c2, cv2.MORPH_GRADIENT, kernel_e)

comb = np.hstack((cat, g, g2)) # original rectangle elipse
cv2.imshow("Zadanie 5", comb)
cv2.waitKey(0)

# Zadanie 6
tablica = cv2.imread("tablica.png", 0)
tablica_e = cv2.erode(tablica, kernel_r, iterations=1) # pogrubienie liter
comb2 = np.hstack((tablica, tablica_e))
cv2.imshow("Zadanie 6", comb2)
cv2.waitKey(0)