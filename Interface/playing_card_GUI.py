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
    
    def __init__(self,image_on):
        self.__image_on = image_on
        self.__image = self.__image_on
        self.__image_down = ...#Charger l'image d'une carte face verso
        
        #Deux lignes suivantes à modifier selon la taille réelle
        #La position correspond au bord haut gauche de la carte
        self.__position = []
        self.__size = [self.__image.size[0],self.__image.size[1]] #(largeur, hauteur)
        self.__hitbox(self.__position[0], self.__position[1], self.__size[0], self.size[1])
        
    def is_mouse_over(self,m_x,m_y):
        #Si la souris a le focus sur la carte, on la surélève (et on la fait briller ?)
        flag_x = (m_x > self.__hitbox[0] and m_x < self.__hitbox[0]+self.__hitbox[2])
        flag_y = (m_y > self.__hitbox[1] and m_y < self.__hitbox[1]+self.__hitbox[3])
        
        return flag_x and flag_y

    def hover(self):#Fonction de surélèvelent
        self.set_position(self.get_position()[0],self.get_postion()[1]+20) #On surélève de 20px par exemple
    
    def set_postion(self,x,y):
        self.__position[0] = x
        self.__position[1] = y
        
    def get_position(self):
        return self.__position
    
    def set_face_up(self,b):
        if b:
            self.__image = self.__image_on
        else:
            self.__image = self.__image_down
            
    #def onClick(self,game): #On définit ce qu'on doit faire avec la carte une fois cliquée (l'ajouter au tas)
        
            
def load_images():
    
    colors = ["coeur","carreau","pique","trèfle"]
    heads = ["Valet","Cavalier","Dame","Roi"]
    
    for i in range(1,10):
        for c in colors:
            if i == 1:
                CARDS_FACE.append(PhotoImage(file="cards_img/As "+c+".jpg")) #convertir les JPG en PNG sinon erreur ! 
            else:
                CARDS_FACE.append(PhotoImage(file="cards_img/"+i+" "+c+".jpg"))
    
    for i in heads:
        for c in colors:
            CARDS_FACE.append(PhotoImage(file="cards_img/"+i+" "+c+".jpg"))
            
    for i in range(1,21):
        CARDS_FACE.append(PhotoImage(file="cards_img/"+i+" atout.jpg"))
        
    CARDS_FACE.append(PhotoImage(file="cards_img/Excuse.jpg"))

root = Tk()
load_images()
    
''' Ne pas oublier de créer une classe/fonction qui attribue à chaque carte la bonne image en 
fonction de ses attribus'''
            