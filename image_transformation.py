from PIL import Image

def transform_image(img, brightness, darkness):
    result_img = img.copy()
    w, h = img.size
    for i in range(w):
        for j in range(h):
            pixel = img.getpixel((i, j))
            if len(pixel) == 4:
                r, g, b, _ = pixel
            else:
                r, g, b = pixel

            r = min(255, r + brightness)
            g = min(255, g + brightness)
            b = min(255, b + brightness)

            r = max(0, r - darkness)
            g = max(0, g - darkness)
            b = max(0, b - darkness)

            result_img.putpixel((i, j), (r, g, b))

    return result_img
def power_transform(img, c, n):
    result_img = img.copy()
    w, h = img.size
    for i in range(w):
        for j in range(h):
            pixel = img.getpixel((i, j))
            if len(pixel) == 4:
                r, g, b, _ = pixel
            else:
                r, g, b = pixel

            r = min(255, c.get() * (r / 255.0) ** n.get())
            g = min(255, c.get() * (g / 255.0) ** n.get())
            b = min(255, c.get() * (b / 255.0) ** n.get())

            result_img.putpixel((i, j), (int(r), int(g), int(b)))
    return result_img



def make_negative(img):
    result_img = img.copy()
    w, h = img.size
    for i in range(w):
        for j in range(h):
            pixel = img.getpixel((i, j))
            if len(pixel) == 4:
                r, g, b, _ = pixel
            else:
                r, g, b = pixel

            r = 255 - r
            g = 255 - g
            b = 255 - b

            result_img.putpixel((i, j), (r, g, b))

    return result_img


