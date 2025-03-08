# Zadanie 1
import cv2
image = cv2.imread("kot.jpeg")
if image is None:
 print("Błąd: nie mozna wczytac obrazu!")
else:
 cv2.imshow("Wyswietlony obraz", image)
 cv2.waitKey(0)
 cv2.destroyAllWindows()

# Zadanie 2
(h, w, c) = image.shape[:3]
print(f'Liczba kanalow: {c}')

# Zadanie 3
image_gray = cv2.imread("kot.jpeg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Obraz w skali szarosci", image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
# liczba kanalow dla zdjecia w odcieniach szarosci jest rowna 1, bo nie maja kolorow

# Zadanie 4
cv2.imwrite('kot_gray.jpeg', image_gray)

# Zadanie 5
cv2.imshow("Obraz 1", image)
cv2.imshow("Obraz 2", image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Zadanie 6
cv2.namedWindow("Autosize window", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("Autosize window", 800, 600)
cv2.imshow('Autosize window', image)
cv2.waitKey(0)
cv2.destroyAllWindows()