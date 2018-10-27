# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 19:34:25 2018

@author: Simon
"""

class Hand():
    
    def __init__(self, cards, position):
        self.__cards = cards #On indique a la main quelles cartes elle possède
        self.__position = position
        
        for i in range(len(self.__cards)):
            self.__cards[i].set_position(self.__position[0]+i*WIDTH,self.__position[1])
            #On affiche les cartes l'une à côté de l'autre ici
            #Peut etre prévoir un affichage différent pour les mains de côité ?
        
    '''Les deux fonctions suivantes permettront d'afficher ou de cacher la main en fonction
    de si le joueur concerné joue ou non'''
    
    def show(self):    
        for c in self.__cards:
            c.set_face_up(True) #A créé dans la classe Playing_Card_GUI
            
    def hide(self):
        for c in self.__cards:
            c.set_face_up(False)
            
    def set_position(self, pos):
        '''reçoit en argument un tuple (x,y)'''
        self.__position = pos
        
        #On replce ensuite toutes les cartaes
        for i in range(len(self.__cards)):
            self.__cards[i].set_position(self.__position[0]+i*WIDTH,self.__position[1])