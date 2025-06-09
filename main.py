import cv2
import numpy as np

# Zadanie 1
def show_image(title, image):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image = cv2.imread("1.jpg")
# a)
kernel_sizes = [(3,3), (5,5), (9,9), (15,15)]
for k in kernel_sizes:
    blurred = cv2.blur(image, k)
    show_image(f"cv2.blur Kernel={k}", blurred)

for k in kernel_sizes:
    blurred = cv2.GaussianBlur(image, k, 0)
    show_image(f"cv2.GaussianBlur Kernel={k}", blurred)

median_kernels = [3, 5, 9, 15]
for k in median_kernels:
    blurred = cv2.medianBlur(image, k)
    show_image(f"cv2.medianBlur Kernel={k}", blurred)

params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]
for diameter, sigmaColor, sigmaSpace in params:
    blurred = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)
    show_image(f"cv2.bilateralFilter d={diameter} sc={sigmaColor} ss={sigmaSpace}", blurred)

# b)
"""
KOMENTARZE:

i)  - Rozmycie medianowe najlepiej usuwa szum typu 'salt and pepper'.
    - Rozmycie dwustronne dobrze redukuje szum, jednocześnie zachowując krawędzie.
ii)  - Rozmycie dwustronne najlepiej zachowuje szczegóły i krawędzie.
iii) - cv2.blur: proste, szybkie, ale rozmywa wszystko równomiernie, gubi krawędzie.
    - cv2.GaussianBlur: lepsze niż cv2.blur, lepsze wygładzanie.
    - cv2.medianBlur: bardzo dobre przy usuwaniu szumu solnego i pieprzowego, ale może szarpaC krawędzie.
    - cv2.bilateralFilter: zachowuje krawędzie
"""

# Zadanie 2
for method in ['blur', 'gaussian', 'median']:
    print(f"Testowanie metody: {method}")
    for k in [3, 5, 9, 15]:
        if method == 'blur':
            blurred = cv2.blur(image, (k, k))
        elif method == 'gaussian':
            blurred = cv2.GaussianBlur(image, (k, k), 0)
        elif method == 'median':
            blurred = cv2.medianBlur(image, k)
        show_image(f"{method} Kernel={k}", blurred)

"""
KOMENTARZE:

i) efekt rozmycia wzrasta wraz z rozmiarem kernela - im większy kernel, tym bardziej rozmyty obraz.
ii) optymalny rozmiar kernela to taki, który usuwa szum, ale nie rozmywa zbytnio detali, zwykle (3x3) do (5x5).
"""

# Zadanie 3
noisy_image = cv2.imread("2.jpg")
show_image("Original noisy image", noisy_image)

params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]
for diameter, sigmaColor, sigmaSpace in params:
    bilateral = cv2.bilateralFilter(noisy_image, diameter, sigmaColor, sigmaSpace)
    show_image(f"Bilateral d={diameter} sc={sigmaColor} ss={sigmaSpace}", bilateral)

for k in [3,5,9]:
    avg = cv2.blur(noisy_image, (k,k))
    gauss = cv2.GaussianBlur(noisy_image, (k,k), 0)
    median = cv2.medianBlur(noisy_image, k)
    show_image(f"Average Blur k={k}", avg)
    show_image(f"Gaussian Blur k={k}", gauss)
    show_image(f"Median Blur k={k}", median)

"""
KOMENTARZE:
i) rozmycie dwustronne skutecznie redukuje szum, zachowując ostre krawędzie
ii) jest lepsze w zachowaniu krawędzi niż proste rozmycia
iii) najlepsze rezultaty przy średnich wartościach sigmaColor i sigmaSpace (np. 41,21).
"""

# Zadanie 4
text_image = cv2.imread("3.jpg")

for k in [3, 5, 9]:
    blurred_avg = cv2.blur(text_image, (k,k))
    blurred_gauss = cv2.GaussianBlur(text_image, (k,k), 0)
    blurred_median = cv2.medianBlur(text_image, k)
    blurred_bilateral = cv2.bilateralFilter(text_image, 11, 41, 21)

    show_image(f"Text Average Blur k={k}", blurred_avg)
    show_image(f"Text Gaussian Blur k={k}", blurred_gauss)
    show_image(f"Text Median Blur k={k}", blurred_median)
show_image("Text Bilateral Blur", blurred_bilateral)

"""
KOMENTARZE:

i) najmocniej rozmywają tekst: cv2.blur i cv2.medianBlur przy dużych kernelach
ii) najlepiej zachowują czytelność: cv2.bilateralFilter oraz cv2.GaussianBlur przy małych kernelach
"""

# 5. Zadanie 5
# dodanie sztucznego szumu solnego i pieprzowego
def add_salt_and_pepper_noise(img, amount=0.02):
    noisy = img.copy()
    num_salt = np.ceil(amount * img.size * 0.5)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in img.shape[:2]]
    noisy[coords[0], coords[1]] = 255

    num_pepper = np.ceil(amount* img.size * 0.5)
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in img.shape[:2]]
    noisy[coords[0], coords[1]] = 0
    return noisy

noisy_img = add_salt_and_pepper_noise(image, 0.03)
show_image("Noisy Image (salt and pepper)", noisy_img)

for k in [3,5,9]:
    avg = cv2.blur(noisy_img, (k,k))
    gauss = cv2.GaussianBlur(noisy_img, (k,k), 0)
    median = cv2.medianBlur(noisy_img, k)
    bilateral = cv2.bilateralFilter(noisy_img, 11, 41, 21)

    show_image(f"Average Blur k={k}", avg)
    show_image(f"Gaussian Blur k={k}", gauss)
    show_image(f"Median Blur k={k}", median)
show_image("Bilateral Blur", bilateral)

"""
KOMENTARZE:
    najlepiej usuwa szum typu sol i pieprz: medianBlur
     bilateral też dobrze usuwa szum, jednocześnie zachowując krawędzie
     average i Gaussian rozmywają szum, ale tracą więcej detali
"""

# Zadanie 6

dof_image = cv2.imread("4.jpg")

mask = np.zeros(dof_image.shape[:2], dtype="uint8")
height = dof_image.shape[0]
mask[int(height/2):, :] = 255  # tło

blurred_background = cv2.GaussianBlur(dof_image, (25, 25), 0)

foreground = cv2.bitwise_and(dof_image, dof_image, mask=cv2.bitwise_not(mask))
background = cv2.bitwise_and(blurred_background, blurred_background, mask=mask)
dof_result = cv2.add(foreground, background)

show_image("Original image", dof_image)
show_image("Simulated depth of field", dof_result)



