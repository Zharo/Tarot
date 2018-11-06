# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 16:51:56 2018

@author: Simon

Cette classe sera liée à toutes les PlayingCards et constitue leur aspect physique

"""

from tkinter import *

#Contient TOUS les fichiers images des cartes
CARDS_FACE= []

#Taille des cartes : 48x89 à peu près
WIDTH = 48
HEIGHT = 89

class Playing_Card_GUI():
    
    def __init__(self,str_image_on):
        self.__name = str_image_on
        self.__image_on = PhotoImage(file=str_image_on)
        self.__image = self.__image_on
        self.__image_down = ...#Charger l'image d'une carte face verso
        
        #Essentiel de rattache l'image à un label pour l'afficher effectivement
        self.__label = Label(image = self.__image_on)
        self.__label.image = self.__image_on
        
        #Deux lignes suivantes à modifier selon la taille réelle
        #La position correspond au bord haut gauche de la carte
        self.__position = [0,0]
        self.__size = [self.__image.width(),self.__image.height()] #(largeur, hauteur)
        self.__hitbox = [self.__position[0], self.__position[1], self.__size[0], self.__size[1]]
        
    def motion_hitbox(self,event):
        #Si la souris a le focus sur la carte, on la surélève (et on la fait briller ?)
        flag_x = (event.x > self.__hitbox[0] and event.x < self.__hitbox[0]+self.__hitbox[2])
        flag_y = (event.y > self.__hitbox[1] and event.y < self.__hitbox[1]+self.__hitbox[3])
        
        if flag_x and flag_y:
            print(self.__name," : focused")
        else:
            print(self.__name," : not focused")

    def hover(self):#Fonction de surélèvelent
        self.set_position(self.get_position()[0],self.get_postion()[1]+20) #On surélève de 20px par exemple
    
    def set_position(self,x,y):
        self.__position[0] = x
        self.__position[1] = y
        
    def get_position(self):
        return self.__position
    
    def draw(self,canvas):
        canvas.create_image(self.__position[0],self.__position[1],anchor=NW,image=self.__image_on)
        #canvas.config(height=self.__size[0],width=self.__size[1])
        
    def set_face_up(self,b):
        if b:
            self.__image = self.__image_on
        else:
            self.__image = self.__image_down
    #def onClick(self,game): #On définit ce qu'on doit faire avec la carte une fois cliquée (l'ajouter au tas)
    def get_name(self):
        return self.__name
    
    def __str__(self):
        return self.get_name()
    
def load_images():
    
    colors = ["coeur","carreau","pique","trèfle"]
    heads = ["Valet","Cavalier","Dame","Roi"]
    
    for i in range(1,10):
        for c in colors:
            if i == 1:
                CARDS_FACE.append(PhotoImage(file="cards_img/As "+c+".png")) #convertir les JPG en PNG sinon erreur ! 
            elif i != 9 and c != "pique":
                CARDS_FACE.append(PhotoImage(file="cards_img/"+str(i)+" "+c+".png"))
    
    for i in heads:
        for c in colors:
            CARDS_FACE.append(PhotoImage(file="cards_img/"+str(i)+" "+c+".png"))
            
    for i in range(1,21):
        CARDS_FACE.append(PhotoImage(file="cards_img/"+str(i)+" atout.png"))
        
    CARDS_FACE.append(PhotoImage(file="cards_img/Excuse.png"))

    
''' Ne pas oublier de créer une classe/fonction qui attribue à chaque carte la bonne image en 
fonction de ses attribus'''
            