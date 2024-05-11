import tkinter as tk
from tkinter import filedialog, Menu, simpledialog, messagebox
from PIL import Image, ImageTk
from image_transformation import transform_image, make_negative,power_transform
from image_blending import *
from contrast import *
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from histogram import *
from blur import *
from image_sharpening import *
from filtry import *

def main():
    def update_image():
        nonlocal img
        nonlocal tk_img
        if power_transform_mode.get():
            if negative.get():
                img = make_negative(img)
            img = power_transform(img, brightness_power, darkness_power)  # Apply power transform
        if negative.get():
                img = make_negative(img)
        img = transform_image(img, brightness.get(), darkness.get())  # Apply linear transform
        tk_img = ImageTk.PhotoImage(img)
        img_label.config(image=tk_img)
        img_label.image = tk_img

    def show_histogram():
        r_histogram, g_histogram, b_histogram = generate_rgb_histogram(img)
        fig = Figure(figsize=(5, 4), dpi=100)
        plot = fig.add_subplot(1, 1, 1)
        plot.plot(r_histogram, color='red')
        plot.plot(g_histogram, color='green')
        plot.plot(b_histogram, color='blue')
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack()
    def blend_image(blend_func):
        nonlocal img
        nonlocal tk_img
        blend_img_path = filedialog.askopenfilename()
        blend_img = Image.open(blend_img_path)
        if blend_func == blend_images_transparency:
            alpha = simpledialog.askfloat("Input", "Enter alpha value:", parent=window)
            img = blend_func(img, blend_img, alpha)
        else:
            img = blend_func(img, blend_img)
        tk_img = ImageTk.PhotoImage(img)
        img_label.config(image=tk_img)
        img_label.image = tk_img

    def contrast_up():
        nonlocal img
        nonlocal tk_img
        img = increase_contrast(img, 10)  # Zwiększamy kontrast o 10
        tk_img = ImageTk.PhotoImage(img)
        img_label.config(image=tk_img)
        img_label.image = tk_img

    def contrast_down():
        nonlocal img
        nonlocal tk_img
        img = decrease_contrast(img, 10)  # Zmniejszamy kontrast o 10
        tk_img = ImageTk.PhotoImage(img)
        img_label.config(image=tk_img)
        img_label.image = tk_img

    def blur_image():
        nonlocal img
        nonlocal tk_img
        blur_strength = simpledialog.askinteger("Wprowadź wartość rozmycia", "Podaj wartość rozmycia (1-4)",minvalue=1, maxvalue=4)
        for _ in range(blur_strength):
            img = apply_box_filter(img)
        tk_img = ImageTk.PhotoImage(img)
        img_label.config(image=tk_img)
        img_label.image = tk_img

    def sharpen_image(sharpen_func):
        nonlocal img
        nonlocal tk_img
        img_array = np.array(img.convert('L'))
        img_array = sharpen_func(img_array)
        img = Image.fromarray(img_array.astype(np.uint8))
        tk_img = ImageTk.PhotoImage(img)
        img_label.config(image=tk_img)
        img_label.image = tk_img

    def filter_image(filter_func):
        nonlocal img
        nonlocal tk_img
        rozmiar_maski = simpledialog.askinteger("Wprowadź wartość maski", "Podaj rozmiar maski")
        # Sprawdzenie, czy podana liczba jest parzysta
        while int(rozmiar_maski) % 2 != 0:
            messagebox.showerror("Błąd", "Podana liczba nie jest parzysta. Podaj parzystą liczbę dla rozmiaru maski.")
            rozmiar_maski = simpledialog.askinteger("Wprowadź wartość maski", "Podaj rozmiar maski")
        rozmiar_maski = int(rozmiar_maski)
        img_array = np.array(img)  # Usunięto .convert('L')
        img_array = filter_func(img_array, rozmiar_maski=rozmiar_maski)
        # Konwersja z powrotem do uint8 przed wyświetleniem
        img_array = np.clip(img_array, 0, 255)  # Upewniamy się, że wartości są w zakresie 0-255
        img = Image.fromarray(img_array.astype(np.uint8))
        tk_img = ImageTk.PhotoImage(img)
        img_label.config(image=tk_img)
        img_label.image = tk_img

    def increase_power_brightness():
        brightness_power.set(max(0.1, brightness_power.get() - 0.1))  # Decrease brightness power with each click
        update_image()  # Update the image

    def increase_power_darkness():
        darkness_power.set(min(10, darkness_power.get() + 0.1))  # Increase darkness power with each click
        update_image()  # Update the image
    def increase_brightness():
        brightness.set(min(255, brightness.get() + 1))
        update_image()
    def increase_darkness():
        darkness.set(min(255, darkness.get() + 1))
        update_image()

    def reset_values():
        brightness.set(50)
        darkness.set(50)
        negative.set(False)
        nonlocal img
        nonlocal tk_img
        img = Image.open(img_path)
        max_size = (600, 600)
        img.thumbnail(max_size, Image.LANCZOS)
        tk_img = ImageTk.PhotoImage(img)
        img_label.config(image=tk_img)
        img_label.image = tk_img

    def load_image():
        nonlocal img_path
        nonlocal img
        nonlocal tk_img
        img_path = filedialog.askopenfilename()
        img = Image.open(img_path)
        max_size = (600, 600)
        img.thumbnail(max_size, Image.LANCZOS)
        tk_img = ImageTk.PhotoImage(img)
        img_label.config(image=tk_img)
        img_label.image = tk_img

    def save_image_as():
        nonlocal img_path
        if img_path is None:
            messagebox.showerror("Error", "No image loaded")
            return
        save_path = filedialog.asksaveasfilename(defaultextension=".png")
        if save_path:
            img.save(save_path)


    def hide_all_buttons():
        for button in buttons:
            button.pack_forget()

    def show_controls():
        hide_all_buttons()
        power_transform_mode.set(False)
        reset_button.pack()
        increase_brightness_button.pack()
        decrease_darkness_button.pack()
        negative_button.pack()

    def show_controls_power():
        hide_all_buttons()
        power_transform_mode.set(True)
        reset_button.pack()
        increase_power_brightness_button.pack()
        decrease_power_darkness_button.pack()

    def show_blend_controls():
        hide_all_buttons()
        reset_button.pack()
        for button in buttons[2:17]:  # Przyciski blend_button1 do blend_button16
            button.pack()

    def show_contrast_controls():
        hide_all_buttons()
        power_transform_mode.set(False)
        increase_contrast_button.pack()
        decrease_contrast_button.pack()
        reset_button.pack()

    def show_histogram_controls():
        hide_all_buttons()
        histogram_button.pack()
        reset_button.pack()

    def show_blur_controls():
        hide_all_buttons()
        blur_button.pack()
        reset_button.pack()
    def show_sharpening_controls():
        hide_all_buttons()
        sharpening_button1.pack()
        sharpening_button2.pack()
        sharpening_button3.pack()
        sharpening_button4.pack()
        sharpening_button5.pack()
        sharpening_button6.pack()
        sharpening_button7.pack()
        reset_button.pack()
    def show_filtrs_controls():
        hide_all_buttons()
        filtr_button1.pack()
        filtr_button2.pack()
        filtr_button3.pack()
        reset_button.pack()


    window = tk.Tk()
    window.title("Photoshop")
    brightness = tk.IntVar(window)
    brightness.set(50)  # default value
    power_transform_mode = tk.BooleanVar()
    power_transform_mode.set(False)
    darkness = tk.IntVar(window)
    darkness.set(50)  # default value
    brightness_power = tk.DoubleVar(window)
    brightness_power.set(1.0)  # default value
    darkness_power = tk.DoubleVar(window)
    darkness_power.set(1.0)  # default value
    negative = tk.BooleanVar(window)
    negative.set(False)  # default value

    # Create a menu bar
    menubar = Menu(window)
    window.config(menu=menubar)

    # Create a File menu
    filemenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="Open", command=load_image)
    filemenu.add_command(label="Save Image As", command=save_image_as)

    # Create a Transform menu
    transformmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Transform", menu=transformmenu)
    transformmenu.add_command(label="Linear Transform", command=show_controls)
    transformmenu.add_command(label="Power Transform", command=show_controls_power)

    blendimagesmenu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Blend",menu=blendimagesmenu)
    blendimagesmenu.add_command(label="Blend Images",command=show_blend_controls)

    contrastmenu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Contrast",menu=contrastmenu)
    contrastmenu.add_command(label="Modify contrast",command=show_contrast_controls)

    histogrammenu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Histogram",menu=histogrammenu)
    histogrammenu.add_command(label="Create histogram",command=show_histogram_controls)

    blurmenu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Blur",menu=blurmenu)
    blurmenu.add_command(label="Blur image",command=show_blur_controls)

    sharpeningmenu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Sharpening",menu=sharpeningmenu)
    sharpeningmenu.add_command(label="Sharpening image",command=show_sharpening_controls)

    filtrsmenu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Filtrs",menu=filtrsmenu)
    filtrsmenu.add_command(label="Image filter",command=show_filtrs_controls)


    img_path = None
    img = None
    tk_img = None
    img_label = tk.Label(window)
    img_label.pack()

    reset_button = tk.Button(window, text="Reset", command=reset_values)
    increase_brightness_button = tk.Button(window, text="Lighter", command=increase_brightness)
    decrease_darkness_button = tk.Button(window, text="Darker", command=increase_darkness)
    negative_button = tk.Checkbutton(window, text="Negatyw", variable=negative, command=update_image)

    reset_button = tk.Button(window, text="Reset", command=reset_values)
    increase_power_brightness_button = tk.Button(window, text="Lighter", command=increase_power_brightness)
    decrease_power_darkness_button = tk.Button(window, text="Darker", command=increase_power_darkness)
    blend_button=tk.Button(window,text="Blend image",command=blend_image)

    blend_button1 = tk.Button(window, text="Blend Image Additive", command=lambda: blend_image(blend_images_additive))

    blend_button2 = tk.Button(window, text="Blend Image Subtractive",command=lambda: blend_image(blend_images_subtractive))

    blend_button3 = tk.Button(window, text="Blend Image Difference",command=lambda: blend_image(blend_images_difference))

    blend_button4 = tk.Button(window, text="Blend Image Multiply", command=lambda: blend_image(blend_images_multiply))

    blend_button5 = tk.Button(window, text="Blend Image Screen", command=lambda: blend_image(blend_images_screen))

    blend_button6 = tk.Button(window, text="Blend Image Negation", command=lambda: blend_image(blend_images_negation))

    blend_button7 = tk.Button(window, text="Blend Image Darken", command=lambda: blend_image(blend_images_darken))

    blend_button8 = tk.Button(window, text="Blend Image Lighten", command=lambda: blend_image(blend_images_lighten))

    blend_button9 = tk.Button(window, text="Blend Image Exclusion", command=lambda: blend_image(blend_images_exclusion))

    blend_button10 = tk.Button(window, text="Blend Image Overlay", command=lambda: blend_image(blend_images_overlay))

    blend_button11 = tk.Button(window, text="Blend Image Hard Light",command=lambda: blend_image(blend_images_hard_light))

    blend_button12 = tk.Button(window, text="Blend Image Soft Light",command=lambda: blend_image(blend_images_soft_light))

    blend_button13 = tk.Button(window, text="Blend Image Color Dodge",command=lambda: blend_image(blend_images_color_dodge))

    blend_button14 = tk.Button(window, text="Blend Image Color Burn",command=lambda: blend_image(blend_images_color_burn))

    blend_button15 = tk.Button(window, text="Blend Image Reflect", command=lambda: blend_image(blend_images_reflect))

    blend_button16 = tk.Button(window, text="Blend Image Transparency",command=lambda: blend_image(blend_images_transparency))

    increase_contrast_button = tk.Button(window, text="Increase Contrast", command=contrast_up)

    decrease_contrast_button = tk.Button(window, text="Decrease Contrast", command=contrast_down)

    histogram_button = tk.Button(window, text="Show Histogram", command=show_histogram)

    blur_button=tk.Button(window,text="Blur image",command=blur_image)

    sharpening_button1=tk.Button(window,text="Operator Robertsa poziomo",command=lambda: sharpen_image(wyostrzanie_robertsa_poziomy))

    sharpening_button2 = tk.Button(window, text="Operator Robertsa pionowo",command=lambda: sharpen_image(wyostrzanie_robertsa_pionowy))

    sharpening_button3 = tk.Button(window, text="Operator Prewitta poziomo",command=lambda: sharpen_image(filtr_prewitta_poziomy))

    sharpening_button4 = tk.Button(window, text="Operator Prewitta pionowo", command=lambda: sharpen_image(filtr_prewitta_pionowy))

    sharpening_button5 = tk.Button(window, text="Operator Sobela poziomo",command=lambda: sharpen_image(filtr_sobela_poziomy))

    sharpening_button6 = tk.Button(window, text="Operator Sobela pionowo",command=lambda: sharpen_image(filtr_sobela_pionowy))

    sharpening_button7 = tk.Button(window, text="Filtr laplace'a",command=lambda: sharpen_image(filtr_laplacea))

    filtr_button1=tk.Button(window,text="Filtr min",command=lambda: filter_image(filtr_minimum))

    filtr_button2 = tk.Button(window, text="Filtr max", command=lambda: filter_image(filtr_maksimum))

    filtr_button3 = tk.Button(window, text="Filtr median", command=lambda: filter_image(filtr_medianowy))



    buttons = [negative_button, blend_button1, blend_button2, blend_button3, blend_button4,
               blend_button5, blend_button6, blend_button7, blend_button8, blend_button9, blend_button10,
               blend_button11, blend_button12, blend_button13, blend_button14, blend_button15, blend_button16,
               increase_brightness_button, decrease_darkness_button, increase_power_brightness_button,
               decrease_power_darkness_button, increase_contrast_button, decrease_contrast_button, histogram_button,
               blur_button, reset_button,sharpening_button1,sharpening_button2,sharpening_button3,sharpening_button4,sharpening_button5,sharpening_button6,sharpening_button7
               ,filtr_button1,filtr_button2,filtr_button3]






    window.mainloop()
# Wywołanie funkcji
if __name__ == "__main__":
    main()













