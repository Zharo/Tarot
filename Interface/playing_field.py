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
from playing_card_GUI import *
from player import *
from random import *
from hand import *

class Playing_Field(Canvas):
    
    def __init__(self,parent):
        Canvas.__init__(self,parent,background="white",width = parent.get_width(), height = parent.get_height() )
        self.__parent = parent
        self.__width = parent.get_width()
        self.__height = parent.get_height()
        self.__players = []
        self.__deck = self.create_deck()
        
    def create_deck(self):
        """Creates a tarot deck of 78 cards"""
        L=[]
        for i in range(1, 22):
            L.append(Playing_Card_GUI("cards_img/"+str(i)+" atout.png"))
        for s in ('pique', 'coeur', 'carreau', 'trèfle'):
            for i in range(1, 11):
                if i == 1 :
                    L.append(Playing_Card_GUI("cards_img/As "+s+".png"))
                elif i!=9 and s != 'pique':
                    L.append(Playing_Card_GUI("cards_img/"+str(i)+" "+s+".png"))
            for j in ('valet','cavalier','dame','roi'):
                L.append(Playing_Card_GUI("cards_img/"+j+" "+s+".png"))
        L.append(Playing_Card_GUI("cards_img/Excuse.png"))
        return L
    
    #Il faut maintenant gérer les évênements, à savoir : lorsqu'une carte est cliqué,
    #Elle est posée devant le joueur (modifier playing_card_GUI, playing_field)
    
    def place_hands(self):
        '''Cette méthode prend en argument le jeu donc la classe qui gère les cartes etc...,
        donc qui possède en attribut les mains des joueurs à la fois sous forme de tableau de classes
        héritant de Playing_Card_GUI'''

        #On initialise la position des points stratégiques EST,SUD,NORD et OUEST
        
        nord = (self.__width//2-2*50,50)
        sud = (self.__width//2-2*50,self.__height-100)
        est = (50,self.__height//2)
        ouest = (self.__width - 50*5,self.__height//2)
                
        side = [sud,est,nord,ouest]
        
        #On initialise les joueurs
        for i in range(4):
            p = Player()
            cards = []
            for j in range(4):
                r = randint(0,len(self.__deck)-2)
                cards.append(self.__deck[r])
                self.__deck.pop(r)
            #On donne une main au joueur aléatoirement
            #print(Hand(cards,side[i]))
            h = Hand(cards,side[i])
    
            p.set_hand(h)
            
            self.__players.append(p)
        
        h1 = self.__players[0].get_hand()
        h2 = self.__players[1].get_hand()
        h3 = self.__players[2].get_hand()
        h4 = self.__players[3].get_hand()
        
#        h1.set_position(sud)
#        h2.set_position(ouest)
#        h3.set_position(nord)
#        h4.set_position(est)
        h1.show(self)
        h2.show(self)
        h3.show(self)
        h4.show(self)