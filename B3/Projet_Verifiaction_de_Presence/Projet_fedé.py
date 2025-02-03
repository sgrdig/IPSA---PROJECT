from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
import smtplib, ssl
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import face_recognition
import os
import numpy as np
from ultralytics import YOLO
import time
import os
from PIL import Image, ImageTk
import tkinter as tk
import torch


yolo_model = YOLO('yolov8s.pt')
device = 'cuda' if torch.cuda.is_available() else 'cpu'
yolo_model = YOLO('yolov8s.pt')
yolo_model.to(device)

image_states = {} 
detected_faces = []
detected_faces_status = {}  




def color_image(photos_de_reference):    
    global image_labels
    image_labels = []
    for idx, photo in enumerate(photos_de_reference):

        segments = photo.split(os.sep)  
        if len(segments) > 1:
            second_segment = segments[1]

        img = Image.open(photo)
        img = img.resize((150, 150))
        img_tk = ImageTk.PhotoImage(img)

        bg_color = "green" if detected_faces_status.get(second_segment, False) else "red"
        image_label = tk.Label(frame4, image=img_tk, bg=bg_color, width=150, height=150)
        image_label.image = img_tk
        image_label.grid(row=0, column=idx, padx=10, pady=10)
        image_labels.append(image_label)


def update_color_image(photos_de_reference):
    global image_labels
    for idx, photo in enumerate(photos_de_reference):
        segments = photo.split(os.sep)
        if len(segments) > 1:
            second_segment = segments[1]

        bg_color = "green" if detected_faces_status.get(second_segment, False) else "red"
        image_labels[idx].config(bg=bg_color)

    root.after(500, lambda: update_color_image(photos_de_reference))




def load_images():
    global photos_de_reference
    reference_images_folder = "Data"
    photos_de_reference = []
    photos = []

 
    for root, dirs, files in os.walk(reference_images_folder):
        if files:
       
            image_files = [f for f in files if f.endswith(".jpg") or f.endswith(".png")]
            
            if image_files:
                for image_file in image_files:
                    photos.append(os.path.join(root, image_file))
                
                first_image_path = os.path.join(root, image_files[0])
                photos_de_reference.append(first_image_path)
    
    print("Photos de référence :")
    print(photos_de_reference)
    
    print("\nToutes les photos :")
    print(photos)
    color_image(photos_de_reference=photos_de_reference)
    update_color_image(photos_de_reference=photos_de_reference)



def start_face_recognition():
    global video_capture  
    video_capture = cv2.VideoCapture(0)
    time.sleep(1)
    video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    reference_images_folder = "Data"
    known_face_encodings = []
    known_face_names = []

    for root, dirs, files in os.walk(reference_images_folder):
        for filou in files:
            if filou.endswith(".jpg") or filou.endswith(".png"):
                image_path = os.path.join(root, filou)
                image_reference = face_recognition.load_image_file(image_path)
                encodings = face_recognition.face_encodings(image_reference)
                if encodings:
                    known_face_encodings.append(encodings[0])
                    known_face_names.append(os.path.splitext(filou)[0])




    def update_frame():
        ret, frame = video_capture.read()
        if not ret:
            print("Erreur sur la caméra")
            return

        results = yolo_model(frame, conf=0.5, iou=0.4)

        for det in results[0].boxes:
            x1, y1, x2, y2 = map(int, det.xyxy[0])
            cls = int(det.cls[0])

            if cls == 0:
                face_crop = frame[y1:y2, x1:x2]
                face_crop_rgb = cv2.cvtColor(face_crop, cv2.COLOR_BGR2RGB)
                face_encoding = face_recognition.face_encodings(face_crop_rgb)

                name = "Inconnu"
                color = (0, 0, 255)

                if face_encoding:
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding[0])
                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding[0])

                    if True in matches:
                        best_match_index = np.argmin(face_distances)
                        if matches[best_match_index]:
                            name = known_face_names[best_match_index]
                            
                            if name not in detected_faces_status:
                                detected_faces_status[name] = False
                                color = (0, 255, 0)
                            else:
                                color = (0, 255, 0)
                            detected_faces.append(name)

                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        camera_label.imgtk = imgtk
        camera_label.configure(image=imgtk)
        camera_label.after(10, update_frame)

    update_frame()


def who_is_this(face_detected: list, path_dir: str):
    print(f'Visages détectés : {face_detected}')
    true_identity : list = []
    
    relevant_faces = [face for face in face_detected]
    image_extensions = ['.png', '.jpeg' , '.jpg']
    test = [face + ext for face in relevant_faces for ext in image_extensions]
    print(f'Noms de fichiers attendus (test) : {test}')
    
    for subdir in os.listdir(path_dir):
        sousdirectory_name = os.listdir(f'{path_dir}/{subdir}')
        
        if any(file in sousdirectory_name for file in test):
            true_identity.append(subdir)
    
    print(f'Identité(s) trouvée(s) : {true_identity}')
    return true_identity

def email(recap):
        smtp_server = 'smtp.gmail.com'
        port = 465
        destinateur = 'ipsa.presence@gmail.com' #adresse d'envoie crée
        password = 'uxsj qcxu xvfk scgc' #mot de passe adresse
        destinataire = "valentin.perrot@ipsa.fr" #adresse destinateur
        message = MIMEMultipart('alternative')
        message['Subject'] = 'Envoie Présence éléve'# objet mail
        message['From'] = destinateur
        message['To'] = destinataire
        message.attach(MIMEText(f"Bonjour,\n\nVoici votre compte-rendu des présences :\n\n{recap}", 'plain'))# message mail

        # with open(nom_fichier, 'rb') as attachment:
        #     file_part = MIMEBase('application', 'octet-stream')
        #     file_part.set_payload(attachment.read())
        #     encoders.encode_base64(file_part)
        #     file_part.add_header('Content-Disposition','attachment; filename='+ str(nom_fichier))
        #     message.attach(file_part)
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(destinateur, password)
            server.sendmail(destinateur, destinataire, message.as_string())

        messagebox.showinfo("Confirmation d\'envoie", "Votre compte-rendu des présences à bien été envoyer")


def open_new_window():
    unique_faces = []
    print(f'deteceted files {detected_faces}')
    for face in detected_faces:
        if face not in unique_faces:  
            unique_faces.append(face) 
            print(unique_faces)
    presence = {}


    cv2.destroyAllWindows()
    print('test')
    root.destroy()
    root.quit()

    new_window = ctk.CTk()
    new_window.title("Fiche de présences")
    new_window.attributes('-fullscreen', True)
    new_window.config(bg="black", bd=0, highlightthickness=0)

    label_title = ctk.CTkLabel(new_window, text="Liste des présences", font=("Arial Bold", 80))
    label_title.pack(pady=20)

    reference_images_folder = "Data"
    found_files = False  
    print(f'ta grand mere;{unique_faces}')
    lst_name = who_is_this(face_detected=unique_faces , path_dir=reference_images_folder)
    print(f'Unique :{lst_name}')
    print(os.listdir(reference_images_folder))
    for names in os.listdir(reference_images_folder):
        if names in lst_name:
            presence[names] = 'present'
        else : 
            presence[names] = 'absent'
    
    recap =  []

    encule  = os.listdir(reference_images_folder)
    for index, personnedetamere in enumerate(presence):
        label_text = f"{encule[index]} est {presence[personnedetamere]}"
        recap.append(label_text)
        print(recap)
        label = ctk.CTkLabel(new_window, text=label_text, font=("Arial Bold", 24), fg_color="black", text_color="white")
        label.pack(pady=10)

    email(recap)


    new_window.mainloop()



root = ctk.CTk()
karma = False
root.title("Application")
root.attributes('-fullscreen', True)
root.config(bg="black", bd=0, highlightthickness=0)

frame = ctk.CTkFrame(root, corner_radius=10)
frame.pack(fill=BOTH, expand=True)

frame3 = ctk.CTkFrame(root, corner_radius=10)
frame3.pack(fill=BOTH, expand=True)

frame4 = ctk.CTkFrame(root, corner_radius=10)
frame4.pack(fill=BOTH, expand=True)

frame5 = ctk.CTkFrame(root, corner_radius=10)
frame5.pack(fill=BOTH, expand=True)


label1 = ctk.CTkLabel(frame, text="Reconnaissance faciale", font=("Arial Bold", 24))
label1.pack(padx=10, pady=10)


camera_label = Label(frame3, bg="black")
camera_label.pack(fill=BOTH, expand=True)


boutton_start = ctk.CTkButton(frame5, width=150, height=50, corner_radius=10, text="Lancer", font=("Arial Bold", 18), command=start_face_recognition)
boutton_start.pack(side=LEFT, padx=20, pady=20)

boutton_quit = ctk.CTkButton(frame5, width=150, height=50, corner_radius=10, fg_color="red", hover_color="darkred", text_color="white", text="Quitter", font=("Arial Bold", 18), command=open_new_window)
boutton_quit.pack(side=RIGHT, padx=20, pady=20)

load_images()

root.mainloop()