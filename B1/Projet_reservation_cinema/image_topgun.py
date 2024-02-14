from PIL import Image, ImageTk
import tkinter as tk

def image_topgun():
    topgun = tk.Tk()
    topgun.title("Top Gun")

    im1 = Image.open('topgun.jpg')
    logo = ImageTk.PhotoImage(im1)

    dessin = tk.Canvas(topgun, width=im1.size[0], height=im1.size[1])
    logo1 = dessin.create_image(0, 0, anchor=tk.NW, image=logo)
    dessin.pack()

    topgun.mainloop()
