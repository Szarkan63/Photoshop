import numpy as np
from PIL import Image
def apply_box_filter(image):
    # Pobierz wymiary obrazu
    width, height = image.size

    # Przekształć obraz PIL w tablicę numpy
    image = np.array(image)

    # Utwórz kopię obrazu do przechowywania wyników
    filtered_image = image.copy()

    # Przejdź przez każdy piksel obrazu
    for y in range(1, height-1): ###unikamy krawedzi by uniknac problemow z indekosowaniem poza zakresem
        for x in range(1, width-1):
            # Dla każdego piksela, oblicz średnią z jego otoczenia 3x3
            for color in range(3):  # Dla każdego kanału koloru (R, G, B)
                sum_color = 0
                for j in range(-1, 2):
                    for i in range(-1, 2):
                        sum_color += image[y+j, x+i, color]
                filtered_image[y, x, color] = sum_color // 9

    # Przekształć tablicę numpy z powrotem na obraz PIL
    filtered_image = Image.fromarray(filtered_image)
    return filtered_image

