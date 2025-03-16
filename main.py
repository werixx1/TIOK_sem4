# Zadanie 1
import cv2
image = cv2.imread('chillerka.jpg')
(h, w) = image.shape[:2]
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))
print("-"*50)

# Zadanie 2
cv2.imshow("(Zadanie 2) Before", image)
cv2.waitKey(0)
image[300, 500] = (0, 0, 255)
(b, g, r) = image[300, 500]
cv2.imshow("(Zadanie 2) After", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Zadanie 3
(cX, cY) = (w // 2, h // 2)
(b1, g1, r1) = image[cY, cX]
print("Center: ({}, {})".format(cX, cY))
print("Pixel at center - Red: {}, Green: {}, Blue: {}".format(r1, g1, b1))

# Zadanie 4
x = int(input("Podaj wsp x: "))
y = int(input("Podaj wsp y: "))

if 0 <= x < h and 0 <= y < w:
    image[x, y] = (0, 0, 0)
    (b, g, r) = image[x, y]
    cv2.imshow("Zadanie 4", image)
    cv2.waitKey(0)
else:
    print("Wspolrzedne wychodza poza wymiar zdjecia")

# Zadanie 5
tl = image[0:cY, 0:cX]
tr = image[0:cY, cX:w]
br = image[cY:h, cX:w]
bl = image[cY:h, 0:cX]
image[0:cY, 0:cX] = (255, 0, 0)
cv2.imshow("Zadanie 5", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Zadanie 6
startX, endX = cX - 50, cX + 50
startY, endY = cY - 50, cY + 50
image[startY:endY, startX:endX] = (0, 0, 255)

cv2.imshow("Zadanie 6", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Zadanie 7
(cX_, cY_) = (w // 3, h // 3)
polowa_x = cX_ // 2
polowa_y = cY_ // 2
# fragment ze srodka
startX_, endX_ = cX - polowa_x, cX + polowa_x
startY_, endY_ = cY - polowa_y, cY + polowa_y

cv2.imshow("Zadanie 7", image[startY_:endY_, startX_:endX_])
cv2.waitKey(0)
cv2.destroyAllWindows()

# Zadanie 8
cv2.imshow("(Zadanie 8) Before: ", image)
cv2.waitKey(0)
for i in range (w):
    image[100, i] = (0, 255, 0)

cv2.imshow("(Zadanie 8) After: ", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Zadanie 9
cv2.imshow("(Zadanie 9) Before: ", image)
cv2.waitKey(0)
image[50:100, 50:100] = (255, 255, 255)
cv2.imshow("(Zadanie 9) After: ", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Zadanie 10
(b1, g1, r1) = image[50, 50]
(b2, g2, r2) = image[200, 200]

print("Pixel at (50, 50) - Red: {}, Green: {}, Blue: {}".format(r1, g1, b1))
print("Pixel at (200, 200) - {}, {}, {}".format(r2, g2, b2))
print("Roznica: {} {} {}".format(b1-b2, g1-g2, r1-r2))
print("-"*50)

# Zadanie 11
(b0, g0, r0) = image[0, 0] # zalozony poczatkowy najjasniejszy piksel

for i in range(w):
    for j in range(h):
        (bn, gn, rn) = image[j, i]
        if (bn, gn, rn) > (b0, g0, r0):
            (b0, g0, r0) = image[i, j]

print("Najjasniejszy piksel znajduje sie H: {} W: {} i ma wartosci "
                  "R: {}, G: {}, B: {}".format(i, j, b0, g0, r0))

cv2.imwrite('piesek_po_zmianach.jpg', image)