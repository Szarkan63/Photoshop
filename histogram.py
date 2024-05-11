import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def generate_rgb_histogram(image_path):
    if isinstance(image_path, str):
        img = Image.open(image_path).convert('RGB')
    else:
        img = image_path.convert('RGB')
    img_cv = np.array(img)
    img_cv = img_cv[:, :, ::-1].copy()  ##Bierzemy wszystkie kolumny i zmieniamy RGB na BGR
    r, g, b = cv2.split(img_cv)  #Rozdzielamy obraz na trzy kanaly
    r_eq = cv2.equalizeHist(r)  #Poprawianie kontrastu
    g_eq = cv2.equalizeHist(g)
    b_eq = cv2.equalizeHist(b)
    img_eq = cv2.merge([r_eq, g_eq, b_eq])  #laczymy znowy
    r_values = cv2.calcHist([r_eq], [0], None, [256], [0, 256])
    g_values = cv2.calcHist([g_eq], [0], None, [256], [0, 256])
    b_values = cv2.calcHist([b_eq], [0], None, [256], [0, 256])
    plt.bar(np.arange(256), r_values.ravel(), color='red', alpha=0.7, label='Red')
    plt.bar(np.arange(256), g_values.ravel(), color='green', alpha=0.7, label='Green')
    plt.bar(np.arange(256), b_values.ravel(), color='blue', alpha=0.7, label='Blue')
    plt.legend(loc='upper right')
    plt.show()

