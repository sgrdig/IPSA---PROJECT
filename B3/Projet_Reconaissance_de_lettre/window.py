import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
from main import start

prev_x, prev_y = None, None
image = None
draw = None

def start_draw(event):
    global prev_x, prev_y
    prev_x, prev_y = event.x, event.y

def draw_on_canvas(event):
    global prev_x, prev_y, image, draw
    if prev_x is not None and prev_y is not None:
        canvas.create_line(prev_x, prev_y, event.x, event.y, fill="black", width=2)
        draw.line((prev_x, prev_y, event.x, event.y), fill="black", width=2)
    prev_x, prev_y = event.x, event.y

def save_canvas_to_file(filepath):
    global image
    if image is not None:
        image.save(filepath)
        print(f"Image save in the path : {filepath}")
    else:
        print("Erreur")

def reset_canvas():
    global image, draw
    image = Image.new("RGB", (512, 512), "white")
    draw = ImageDraw.Draw(image)
    canvas.delete("all")

def init_image():
    global image, draw
    image = Image.new("RGB", (512, 512), "white")
    draw = ImageDraw.Draw(image)

def analyse_canva():
    save_canvas_to_file("C:/Users/huetb/Desktop/Cours/Bachelor 3/Projet Lettre ML/code/final/projetml 1/image/image.png") 
    display_result_window()
    reset_canvas()

def display_result_window():
    global lettre
    
    result_window = tk.Toplevel(fenetre)
    result_window.title("Résultat")
    result_window.geometry("400x300")
    result_window.configure(bg="#303a71") 

    title_label = tk.Label(
        result_window,
        text="Vous avez écrit la lettre",
        font=("Arial", 20, "bold"),
        bg="#303a71",
        fg="white"
    )
    title_label.pack(pady=20)

    result_frame = tk.Frame(result_window, bg="#303a71", bd=2, relief="ridge")
    result_frame.pack(pady=10, padx=20, fill="both", expand=True)
    
    lettre = start()
    
    result_text = tk.Label(
        result_frame,
        text=f"{lettre}", 
        font=("Arial", 24, "bold"),
        bg="#2b3c62",
        fg="white"
    )
    result_text.pack(pady=40)

    close_button = tk.Button(
        result_window,
        text="Fermer",
        font=("Arial", 14),
        bg="#f05454",
        fg="white",
        activebackground="#d94343",
        activeforeground="white",
        relief="flat",
        command=result_window.destroy
    )
    close_button.pack(pady=20, ipadx=20, ipady=5)

fenetre = tk.Tk()
fenetre.title("Slurp")
fenetre.geometry("700x680")
fenetre.configure(bg="#303a71")  

reset_image = Image.open("C:/Users/huetb/Desktop/Cours/Bachelor 3/Projet Lettre ML/code/src/delete.png").convert("RGBA")
analyse_image = Image.open("C:/Users/huetb/Desktop/Cours/Bachelor 3/Projet Lettre ML/code/src/play.png").convert("RGBA")

reset_photo = ImageTk.PhotoImage(reset_image)
analyse_photo = ImageTk.PhotoImage(analyse_image)

title_frame = tk.Frame(fenetre, bg="#303a71")
title_frame.pack(pady=10)

title_label = tk.Label(title_frame, text="Dessinez votre lettre", font=("Arial", 20, "bold"), bg="#303a71", fg="white")
title_label.pack()

canvas_frame = tk.Frame(fenetre, bg="#303a71")
canvas_frame.pack(pady=10)

canvas = tk.Canvas(canvas_frame, width=512, height=512, bg="white", bd=2, relief="ridge")
canvas.pack()

canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw_on_canvas)

button_frame = tk.Frame(fenetre, bg="#303a71")
button_frame.pack(pady=20)

reset_button = tk.Label(button_frame, image=reset_photo, bg="#303a71", cursor="hand2")
reset_button.grid(row=0, column=0, padx=10)
reset_button.bind("<Button-1>", lambda e: reset_canvas()) 

analyse_button = tk.Label(button_frame, image=analyse_photo, bg="#303a71", cursor="hand2")
analyse_button.grid(row=0, column=1, padx=10)
analyse_button.bind("<Button-1>", lambda e: analyse_canva())  

init_image()

fenetre.mainloop()
