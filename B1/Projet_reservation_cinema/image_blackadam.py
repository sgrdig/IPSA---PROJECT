from PIL import Image, ImageTk
import tkinter as tk


def image_blackadam():

    blackadam = tk.Tk()
    blackadam.title("Blackadam")

    im1 = Image.open('blackadam.jpg')
    logo = ImageTk.PhotoImage(im1, master=blackadam)

    dessin = tk.Canvas(blackadam, width = im1.size[0], height = im1.size[1])
    logo1 = dessin.create_image(0,0, anchor = tk.NW, image = logo)
    dessin.grid()
    blackadam.mainloop()

