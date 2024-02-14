import tkinter
from tkinter import messagebox

csv_file = open('Database.csv')
aero = 0
bachelor = 0
Aero1 = 0
Aero2 = 0
Aero3 = 0
Aero4 = 0
Aero5 = 0
bachelor1 = 0
bachelor2 = 0
bachelor3 = 0
total = 0
for row in csv_file: #nous permet de loop le nombre de fois le nombre de ligne du fichier ouvert
    total = total+1
    
    if row[0]== "A" :           #on obtient le nombre de aero 
        aero = aero + 1
        

        if row[1] == "1": #systeme de trie entre les annees
            Aero1 = Aero1 + 1
        
        if row[1] == "2":
            Aero2 = Aero2 + 1
        
        if row[1] == "3":
            Aero3 = Aero3 + 1
        
        if row[1] == "4":
            Aero4 = Aero4 + 1

        if row[1] == "5":
            Aero5 = Aero5 + 1



    elif row[0]== "B" :
        bachelor = bachelor + 1   
        #on obtient le nombre de bachelor 
        

        if row[1] == "1": #systeme de trie entre les annees
           bachelor1 = bachelor1 + 1
        
        if row[1] == "2":
            bachelor2 = bachelor2 + 1
        
        if row[1] == "3":
            bachelor3  = bachelor3  + 1


pourcentage_aero =(aero * 100 /total) #nous permet d'obtenir des donnes chiffres
pourcentage_bachelor =(bachelor * 100 /total) 

csv_file.close()
