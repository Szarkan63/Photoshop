from PIL import Image
def increase_contrast(img, c):
    result_img = img.copy()
    w, h = img.size
    for i in range(w):
        for j in range(h):
            pixel = img.getpixel((i, j))
            if len(pixel) == 4:
                r, g, b, _ = pixel
            else:
                r, g, b = pixel

            r = min(255, (127 / (127 - c)) * (r - c))
            g = min(255, (127 / (127 - c)) * (g - c))
            b = min(255, (127 / (127 - c)) * (b - c))

            result_img.putpixel((i, j), (int(r), int(g), int(b)))

    return result_img

def decrease_contrast(img, c):
    result_img = img.copy()
    w, h = img.size
    for i in range(w):
        for j in range(h):
            pixel = img.getpixel((i, j))
            if len(pixel) == 4:
                r, g, b, _ = pixel
            else:
                r, g, b = pixel

            r = min(255, ((127 + c) / 127) * (r - c))
            g = min(255, ((127 + c) / 127) * (g - c))
            b = min(255, ((127 + c) / 127) * (b - c))

            result_img.putpixel((i, j), (int(r), int(g), int(b)))

    return result_img
