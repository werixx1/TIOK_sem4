# Zadanie 1
import cv2
import imutils

image = cv2.imread("alien.jpg")
(h, w) = image.shape[:2]
resized = imutils.resize(image, width=w//2)
cv2.imshow("Zadanie 1", resized)
cv2.waitKey(0)

# Zadanie 2
resized = cv2.resize(image, (2*w, 2*h), interpolation=cv2.INTER_LINEAR)
cv2.imshow("Zadanie 2", resized)
cv2.waitKey(0)

# Zadanie 3
r_w = 200.0 / image.shape[1]
r_h = 300.0 / image.shape[0]
r = min(r_w, r_h)
dim = (int(image.shape[1] * r), int(image.shape[0] * r))
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Zadanie 3", resized)
cv2.waitKey(0)

# Zadanie 4
INTER_N = cv2.resize(image, (3*h, 3*w), interpolation=cv2.INTER_NEAREST)
INTER_L = cv2.resize(image, (3*h, 3*w), interpolation=cv2.INTER_LINEAR)
INTER_C = cv2.resize(image, (3*h, 3*w), interpolation=cv2.INTER_CUBIC)
INTER_L4 = cv2.resize(image, (3*h, 3*w), interpolation=cv2.INTER_LANCZOS4)
# cv2.imshow("Zadanie 4-INTER_NEAREST", INTER_N)
# cv2.imshow("Zadanie 4-INTER_LINEAR", INTER_L)
# cv2.imshow("Zadanie 4-INTER_CUBIC", INTER_C)
# cv2.imshow("Zadanie 4-INTER_LANCZOS4", INTER_L4)
# cv2.waitKey(0)


# Zadanie 5
resized = imutils.resize(image, width=500)
cv2.imshow("Zadanie 5", resized)
cv2.waitKey(0)

# Zadanie 6
resized = imutils.resize(image, height=400)
cv2.imshow("Zadanie 6", resized)
cv2.waitKey(0)

# Zadanie 7
resized = cv2.resize(image, (int(w/5), int(h/5)), interpolation=cv2.INTER_AREA)
cv2.imshow("Zadanie 7", resized)
cv2.waitKey(0)

# Zadanie 8
INTER_C = cv2.resize(image, (4*h, 4*w), interpolation=cv2.INTER_CUBIC)
INTER_L4 = cv2.resize(image, (4*h, 4*w), interpolation=cv2.INTER_LANCZOS4)
cv2.imshow("Zadanie 8-INTER_C", INTER_C)
cv2.imshow("Zadanie 8-INTER_L4", INTER_L4)
cv2.waitKey(0)

# Zadanie 9
for i in range(100,301,20):
    resized = imutils.resize(image, width=i)
    cv2.imshow("Zadanie 9", resized)
    cv2.waitKey(500)

# Zadanie 10
resized10 = imutils.resize(image, width=800)
cv2.imwrite("resized_output.jpg", resized10)


