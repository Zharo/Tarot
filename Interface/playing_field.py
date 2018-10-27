# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 19:22:48 2018

@author: Simon

Cette classe est un canvas géant (en hérite), elle représente le terrain de jeu, sur lequel
on va pouvoir installer les mains des joueurs, le tas du milieu etc...
Chacun de ces éléments devra avoir une position particulière (Nord, Sud, Est, Ouest pour les mains des joueurs,
milieu du terrain pour le tas)

"""
from tkinter import *

class Playing_Field(Canvas):
    
    def __inti__(self,parent):
        Canvas.__init__(self,parent)
        self.__parent = parent
        self.__width = 0
        self.__height = 0
        
    def place_hands(self,game):
        '''Cette méthode prend en argument le jeu donc la classe qui gère les cartes etc...,
        donc qui possède en attribut les mains des joueurs à la fois sous forme de tableau de classes
        héritant de Playing_Card_GUI'''
        
        #On initialise la position des points stratégiques EST,SUD,NORD et OUEST
        
        nord = (self.__width//2,0)
        sud = (self.__width//2,self.__height-100)
        est = (0,self.__height//2)
        ouest = (self.__width - 80,self.__height//2)
                
        h1 = game.get_p1().get_hand()
        h2 = game.get_p2().get_hand()
        h3 = game.get_p3().get_hand()
        h4 = game.get_p4().get_hand()
        
        h1.set_position(sud)
        h2.set_position(ouest)
        h3.set_posttion(nord)
        h4.set_position(est)