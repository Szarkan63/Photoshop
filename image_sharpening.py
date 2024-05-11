from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
def wyostrzanie_robertsa_poziomy(image):
    # Konwersja obrazu na typ danych int16, który obsługuje liczby ujemne
    image = image.astype(np.int16)
    height, width = image.shape
    new_image = np.zeros((height, width), dtype=np.int16)

    # Definicja maski filtru Robertsa dla kierunku poziomego
    roberts_x = np.array([[0, 0, 0], [0, 0, -1], [0, 1, 0]])

    # Przejście przez każdy piksel obrazu
    for i in range(height-2):
        for j in range(width-2):
            # Obliczenie wyniku
            Gx = np.sum(roberts_x * image[i:i+3, j:j+3]) ##Przedzial
            new_image[i, j] = min(255, max(0, int(abs(Gx))))
    return new_image

def wyostrzanie_robertsa_pionowy(image):
    # Konwersja obrazu na typ danych int16, który obsługuje liczby ujemne
    image = image.astype(np.int16)
    height, width = image.shape
    new_image = np.zeros((height, width), dtype=np.int16)

    # Definicja maski filtru Robertsa dla kierunku pionowego
    roberts_y = np.array([[0, 0, 0], [0, -1, 0], [0, 0, 1]])

    # Przejście przez każdy piksel obrazu
    for i in range(height-2):
        for j in range(width-2):
            # Obliczenie wyniku
            Gy = np.sum(roberts_y * image[i:i+3, j:j+3])
            new_image[i, j] = min(255, max(0, int(abs(Gy))))

    return new_image



def filtr_prewitta_poziomy(image):
    # Konwersja obrazu na typ danych int16, który obsługuje liczby ujemne
    image = image.astype(np.int16)
    height, width = image.shape
    new_image = np.zeros((height, width), dtype=np.int16)

    # Definicja maski filtru Prewitta w poziomie
    prewitt_x = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])

    # Przejście przez każdy piksel obrazu
    for i in range(1, height-1):
        for j in range(1, width-1):
            # Obliczenie gradientu Gx
            Gx = np.sum(prewitt_x * image[i-1:i+2, j-1:j+2])

            # Obliczenie wyniku
            new_image[i, j] = min(255, max(0, int(abs(Gx))))

    return new_image
def filtr_prewitta_pionowy(image):
    # Konwersja obrazu na typ danych int16, który obsługuje liczby ujemne
    image = image.astype(np.int16)
    height, width = image.shape
    new_image = np.zeros((height, width), dtype=np.int16)

    # Definicja maski filtru Prewitta w pionie
    prewitt_y = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])

    # Przejście przez każdy piksel obrazu
    for i in range(1, height-1):
        for j in range(1, width-1):
            # Obliczenie gradientu Gy
            Gy = np.sum(prewitt_y * image[i-1:i+2, j-1:j+2])

            # Obliczenie wyniku
            new_image[i, j] = min(255, max(0, int(abs(Gy))))

    return new_image
def filtr_sobela_poziomy(image):
    # Konwersja obrazu na typ danych int16, który obsługuje liczby ujemne
    image = image.astype(np.int16)
    height, width = image.shape
    new_image = np.zeros((height, width), dtype=np.int16)

    # Definicja maski filtru Sobela w poziomie
    sobel_x = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])

    # Przejście przez każdy piksel obrazu
    for i in range(1, height-1):
        for j in range(1, width-1):
            # Obliczenie gradientu Gx
            Gx = np.sum(sobel_x * image[i-1:i+2, j-1:j+2])

            # Obliczenie wyniku
            new_image[i, j] = min(255, max(0, int(abs(Gx))))

    return new_image
def filtr_sobela_pionowy(image):
    # Konwersja obrazu na typ danych int16, który obsługuje liczby ujemne
    image = image.astype(np.int16)
    height, width = image.shape
    new_image = np.zeros((height, width), dtype=np.int16)

    # Definicja maski filtru Sobela w pionie
    sobel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

    # Przejście przez każdy piksel obrazu
    for i in range(1, height-1):
        for j in range(1, width-1):
            # Obliczenie gradientu Gy
            Gy = np.sum(sobel_y * image[i-1:i+2, j-1:j+2])

            # Obliczenie wynikud
            new_image[i, j] = min(255, max(0, int(abs(Gy))))

    return new_image
def filtr_laplacea(image):
    # Konwersja obrazu na typ danych int16, który obsługuje liczby ujemne
    image = image.astype(np.int16)
    height, width = image.shape
    new_image = np.zeros((height, width), dtype=np.int16)

    # Definicja masek filtru Laplace'a
    laplace_mask1 = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
    laplace_mask2 = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    laplace_mask3 = np.array([[-2, 1, -2],[1 , 4, 1],[-2,  1, -2]])

    # Przejście przez każdy piksel obrazu
    for i in range(1, height-1):
        for j in range(1, width-1):
            # Obliczenie wyniku dla każdej maski
            new_image1 = np.sum(laplace_mask1 * image[i-1:i+2, j-1:j+2])
            new_image2 = np.sum(laplace_mask2 * image[i-1:i+2, j-1:j+2])
            new_image3 = np.sum(laplace_mask3 * image[i-1:i+2, j-1:j+2])

            # Obliczenie wyniku
            new_image[i, j] = min(255, max(0, int((new_image1**2 + new_image2**2 + new_image3**2)**0.5)))

    return new_image

