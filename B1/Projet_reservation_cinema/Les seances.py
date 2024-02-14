from tkinter import *
from image_blackadam import *
from image_topgun import *
import matplotlib 
from matplotlib import pyplot
from login import *
#------------------------------------------

def stats():
    csv_file = open('Seance.csv')
    blackadam = 0
    topgun = 0
    douze = 0
    vingts = 0
    blackadamdouze = 0
    blackadamvingts = 0
    topgundouze = 0
    topgunvingts = 0
    
    for row in csv_file: #nous permet de loop le nombre de fois le nombre de ligne du fichier ouvert

        if row[0]== "B" :           #on obtient le filme (blackadam) 
            blackadam = blackadam + 1

            if row[1] == "0": #systeme de trie entre les horaires
                douze = douze + 1
                blackadamdouze = blackadamdouze + 1

            if row[1] == "1":
                vingts = vingts + 1
                blackadamvingts = blackadamvingts +1

        elif row[0]== "T" :          #on obtient le film (topgun)
            topgun = topgun + 1

            if row[1] == "3": #systeme de trie entre les horaires
                douze = douze + 1
                topgundouze = topgundouze + 1

            if row[1] == "2":
                vingts = vingts + 1
                topgunvingts = topgunvingts + 1

    print(topgun,blackadam,douze,vingts)
    print(blackadamdouze,blackadamvingts,topgundouze,topgunvingts)
    csv_file.close()

    pyplot.figure(figsize = (4, 4))
    x = [blackadam,topgun]
    pyplot.pie(x, labels = ['blackadam','topgun'], normalize = True,autopct='%1.1f%%')
    pyplot.show()

    pyplot.figure(figsize = (4, 4))
    x = [douze,vingts]
    pyplot.pie(x, labels = ['12h','20h'], normalize = True,autopct='%1.1f%%')
    pyplot.show()

    pyplot.figure(figsize = (4, 4))
    x = [blackadamdouze,blackadamvingts,topgundouze,topgunvingts]
    pyplot.pie(x, labels = ['blackadam 12H','blackadam 20H','topgun 12H','topgun 20H'], normalize = True,autopct='%1.1f%%')
    pyplot.show()





#------------------------------------------
film = Tk()
film.title('Les Films')
film.iconbitmap(r'icone.ico')

l1=Label(film,text="Les Seances :")
l1.grid(row=1,column=1)

b1=Button(film,text="Film 1 : Black Adam",width=15, height=2,command=image_blackadam)
b1.grid(row=2,column=0)

b2=Button(film,text="Film 1 : Top Gun",width=15, height=2,command=image_topgun)
b2.grid(row=3,column=0)

b3=Button(film,text="12h00",width=15, height=2,command=reserver_blackadam_12)
b3.grid(row=2,column=2)

b4=Button(film,text="20h00",width=15, height=2,command=reserver_blackadam)
b4.grid(row=2,column=3)

b5=Button(film,text="12h00",width=15, height=2,command=reserver_topgun_12)
b5.grid(row=3,column=2)

b6=Button(film,text="20h00",width=15, height=2,command=reserver_topgun)
b6.grid(row=3,column=3)

b7=Button(film,text="Inscription/Connexion",width=20, height=1,command=login)
b7.grid(row=0,column=3)

b8=Button(film,text="Stats",width=20, height=1,command=stats)
b8.grid(row=0,column=0)

film.mainloop
