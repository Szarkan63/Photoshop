from PIL import Image
import math
def blend_images_additive(img1, img2):
    img1 = img1.convert("RGBA")
    img2 = img2.convert("RGBA").resize(img1.size)

    result_img = Image.new('RGBA', img1.size)

    for x in range(img1.width):
        for y in range(img1.height):
            r1, g1, b1, a1 = img1.getpixel((x, y))
            r2, g2, b2, a2 = img2.getpixel((x, y))

            r = min(r1 + r2, 255)
            g = min(g1 + g2, 255)
            b = min(b1 + b2, 255)

            result_img.putpixel((x, y), (r, g, b, 255))

    return result_img

def blend_images_subtractive(img1, img2):
    img1 = img1.convert("RGBA")
    img2 = img2.convert("RGBA").resize(img1.size)

    result_img = Image.new('RGBA', img1.size)

    for x in range(img1.width):
        for y in range(img1.height):
            r1, g1, b1, a1 = img1.getpixel((x, y))
            r2, g2, b2, a2 = img2.getpixel((x, y))

            r = max(r1 + r2 - 255, 0)
            g = max(g1 + g2 - 255, 0)
            b = max(b1 + b2 - 255, 0)

            result_img.putpixel((x, y), (r, g, b, 255))

    return result_img

def blend_images_difference(img1, img2):
    img1 = img1.convert("RGBA")
    img2 = img2.convert("RGBA").resize(img1.size)

    result_img = Image.new('RGBA', img1.size)

    for x in range(img1.width):
        for y in range(img1.height):
            r1, g1, b1, a1 = img1.getpixel((x, y))
            r2, g2, b2, a2 = img2.getpixel((x, y))

            r = abs(r1 - r2)
            g = abs(g1 - g2)
            b = abs(b1 - b2)

            result_img.putpixel((x, y), (r, g, b, 255))

    return result_img

def blend_images_multiply(img1, img2):
    img1 = img1.convert("RGBA")
    img2 = img2.convert("RGBA").resize(img1.size)

    result_img = Image.new('RGBA', img1.size)

    for x in range(img1.width):
        for y in range(img1.height):
            r1, g1, b1, a1 = img1.getpixel((x, y))
            r2, g2, b2, a2 = img2.getpixel((x, y))

            r = int(r1 * r2 / 255)
            g = int(g1 * g2 / 255)
            b = int(b1 * b2 / 255)

            result_img.putpixel((x, y), (r, g, b, 255))

    return result_img

def blend_images_screen(img1, img2):
    img1 = img1.convert("RGBA")
    img2 = img2.convert("RGBA").resize(img1.size)

    result_img = Image.new('RGBA', img1.size)

    for x in range(img1.width):
        for y in range(img1.height):
            r1, g1, b1, a1 = img1.getpixel((x, y))
            r2, g2, b2, a2 = img2.getpixel((x, y))

            r = 255 - ((255 - r1) * (255 - r2) // 255)
            g = 255 - ((255 - g1) * (255 - g2) // 255)
            b = 255 - ((255 - b1) * (255 - b2) // 255)

            result_img.putpixel((x, y), (r, g, b, 255))

    return result_img

def blend_images_negation(img1, img2):
    img1 = img1.convert("RGBA")
    img2 = img2.convert("RGBA").resize(img1.size)

    result_img = Image.new('RGBA', img1.size)

    for x in range(img1.width):
        for y in range(img1.height):
            r1, g1, b1, a1 = img1.getpixel((x, y))
            r2, g2, b2, a2 = img2.getpixel((x, y))

            r = 255 - abs(255 - r1 - r2)
            g = 255 - abs(255 - g1 - g2)
            b = 255 - abs(255 - b1 - b2)

            result_img.putpixel((x, y), (r, g, b, 255))

    return result_img

def blend_images_darken(img1, img2):
    img1 = img1.convert("RGBA")
    img2 = img2.convert("RGBA").resize(img1.size)

    result_img = Image.new('RGBA', img1.size)

    for x in range(img1.width):
        for y in range(img1.height):
            r1, g1, b1, a1 = img1.getpixel((x, y))
            r2, g2, b2, a2 = img2.getpixel((x, y))

            r = min(r1, r2)
            g = min(g1, g2)
            b = min(b1, b2)

            result_img.putpixel((x, y), (r, g, b, 255))

    return result_img

def blend_images_lighten(img1, img2):
    img1 = img1.convert("RGBA")
    img2 = img2.convert("RGBA").resize(img1.size)

    result_img = Image.new('RGBA', img1.size)

    for x in range(img1.width):
        for y in range(img1.height):
            r1, g1, b1, a1 = img1.getpixel((x, y))
            r2, g2, b2, a2 = img2.getpixel((x, y))

            r = max(r1, r2)
            g = max(g1, g2)
            b = max(b1, b2)

            result_img.putpixel((x, y), (r, g, b, 255))

    return result_img

def blend_images_exclusion(img1, img2):
    img1 = img1.convert("RGBA")
    img2 = img2.convert("RGBA").resize(img1.size)

    result_img = Image.new('RGBA', img1.size)

    for x in range(img1.width):
        for y in range(img1.height):
            r1, g1, b1, a1 = img1.getpixel((x, y))
            r2, g2, b2, a2 = img2.getpixel((x, y))

            r = r1 + r2 - 2 * r1 * r2 // 255
            g = g1 + g2 - 2 * g1 * g2 // 255
            b = b1 + b2 - 2 * b1 * b2 // 255

            result_img.putpixel((x, y), (r, g, b, 255))

    return result_img

def blend_images_overlay(img1, img2):
    img1 = img1.convert("RGBA")
    img2 = img2.convert("RGBA").resize(img1.size)

    result_img = Image.new('RGBA', img1.size)

    for x in range(img1.width):
        for y in range(img1.height):
            r1, g1, b1, a1 = img1.getpixel((x, y))
            r2, g2, b2, a2 = img2.getpixel((x, y))

            r1 /= 255
            g1 /= 255
            b1 /= 255
            r2 /= 255
            g2 /= 255
            b2 /= 255

            r = 2 * r1 * r2 if r1 < 0.5 else 1 - 2 * (1 - r1) * (1 - r2)
            g = 2 * g1 * g2 if g1 < 0.5 else 1 - 2 * (1 - g1) * (1 - g2)
            b = 2 * b1 * b2 if b1 < 0.5 else 1 - 2 * (1 - b1) * (1 - b2)

            r = int(r * 255)
            g = int(g * 255)
            b = int(b * 255)

            result_img.putpixel((x, y), (r, g, b, 255))

    return result_img
def blend_images_hard_light(img1, img2):
    img1 = img1.convert("RGBA")
    img2 = img2.convert("RGBA").resize(img1.size)

    result_img = Image.new('RGBA', img1.size)

    for x in range(img1.width):
        for y in range(img1.height):
            r1, g1, b1, a1 = img1.getpixel((x, y))
            r2, g2, b2, a2 = img2.getpixel((x, y))

            r1 /= 255
            g1 /= 255
            b1 /= 255
            r2 /= 255
            g2 /= 255
            b2 /= 255

            r = 2 * r1 * r2 if r2 < 0.5 else 1 - 2 * (1 - r1) * (1 - r2)
            g = 2 * g1 * g2 if g2 < 0.5 else 1 - 2 * (1 - g1) * (1 - g2)
            b = 2 * b1 * b2 if b2 < 0.5 else 1 - 2 * (1 - b1) * (1 - b2)

            r = int(r * 255)
            g = int(g * 255)
            b = int(b * 255)

            result_img.putpixel((x, y), (r, g, b, 255))

    return result_img
def blend_images_soft_light(img1, img2):
    img1 = img1.convert("RGBA")
    img2 = img2.convert("RGBA").resize(img1.size)

    result_img = Image.new('RGBA', img1.size)

    for x in range(img1.width):
        for y in range(img1.height):
            r1, g1, b1, a1 = img1.getpixel((x, y))
            r2, g2, b2, a2 = img2.getpixel((x, y))

            r1 /= 255
            g1 /= 255
            b1 /= 255
            r2 /= 255
            g2 /= 255
            b2 /= 255

            r = 2 * r1 * r2 + r1**2 * (1 - 2 * r2) if r2 < 0.5 else math.sqrt(r1) * (2 * r2 - 1) + 2 * r1 * (1 - r2)
            g = 2 * g1 * g2 + g1**2 * (1 - 2 * g2) if g2 < 0.5 else math.sqrt(g1) * (2 * g2 - 1) + 2 * g1 * (1 - g2)
            b = 2 * b1 * b2 + b1**2 * (1 - 2 * b2) if b2 < 0.5 else math.sqrt(b1) * (2 * b2 - 1) + 2 * b1 * (1 - b2)

            r = int(r * 255)
            g = int(g * 255)
            b = int(b * 255)

            result_img.putpixel((x, y), (r, g, b, 255))

    return result_img

def blend_images_color_dodge(img1, img2):
    img1 = img1.convert("RGBA")
    img2 = img2.convert("RGBA").resize(img1.size)

    result_img = Image.new('RGBA', img1.size)

    for x in range(img1.width):
        for y in range(img1.height):
            r1, g1, b1, a1 = img1.getpixel((x, y))
            r2, g2, b2, a2 = img2.getpixel((x, y))

            r1 /= 255
            g1 /= 255
            b1 /= 255
            r2 /= 255
            g2 /= 255
            b2 /= 255

            r = r1 / (1 - r2) if r2 < 1 else 1
            g = g1 / (1 - g2) if g2 < 1 else 1
            b = b1 / (1 - b2) if b2 < 1 else 1

            r = int(r * 255)
            g = int(g * 255)
            b = int(b * 255)

            result_img.putpixel((x, y), (r, g, b, 255))

    return result_img
def blend_images_color_burn(img1, img2):
    img1 = img1.convert("RGBA")
    img2 = img2.convert("RGBA").resize(img1.size)

    result_img = Image.new('RGBA', img1.size)

    for x in range(img1.width):
        for y in range(img1.height):
            r1, g1, b1, a1 = img1.getpixel((x, y))
            r2, g2, b2, a2 = img2.getpixel((x, y))

            r1 /= 255
            g1 /= 255
            b1 /= 255
            r2 /= 255
            g2 /= 255
            b2 /= 255

            r = 1 - (1 - r1) / r2 if r2 > 0 else 0
            g = 1 - (1 - g1) / g2 if g2 > 0 else 0
            b = 1 - (1 - b1) / b2 if b2 > 0 else 0

            r = int(r * 255)
            g = int(g * 255)
            b = int(b * 255)

            result_img.putpixel((x, y), (r, g, b, 255))

    return result_img
def blend_images_reflect(img1, img2):
    img1 = img1.convert("RGBA")
    img2 = img2.convert("RGBA").resize(img1.size)

    result_img = Image.new('RGBA', img1.size)

    for x in range(img1.width):
        for y in range(img1.height):
            r1, g1, b1, a1 = img1.getpixel((x, y))
            r2, g2, b2, a2 = img2.getpixel((x, y))

            r1 /= 255
            g1 /= 255
            b1 /= 255
            r2 /= 255
            g2 /= 255
            b2 /= 255

            r = r1**2 / (1 - r2) if r2 < 1 else 1
            g = g1**2 / (1 - g2) if g2 < 1 else 1
            b = b1**2 / (1 - b2) if b2 < 1 else 1

            r = int(r * 255)
            g = int(g * 255)
            b = int(b * 255)

            result_img.putpixel((x, y), (r, g, b, 255))

    return result_img
def blend_images_transparency(img1, img2, alpha):
    img1 = img1.convert("RGBA")
    img2 = img2.convert("RGBA").resize(img1.size)

    result_img = Image.new('RGBA', img1.size)

    for x in range(img1.width):
        for y in range(img1.height):
            r1, g1, b1, a1 = img1.getpixel((x, y))
            r2, g2, b2, a2 = img2.getpixel((x, y))

            r = int((1 - alpha) * r2 + alpha * r1)
            g = int((1 - alpha) * g2 + alpha * g1)
            b = int((1 - alpha) * b2 + alpha * b1)

            result_img.putpixel((x, y), (r, g, b, 255))

    return result_img


