# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 20:21:31 2018

@author: Simon
"""

from tkinter import *

class Window(Tk):
    
    def __init__(self,width,height):
        
        assert self.__class__ is not Window #Classe absraite
        Tk.__init__(self)
        self.__width = width
        self.__height = height
        self.__bg_color = "white"
        
        #Canvas associé à la fenêtre
        self.__canvas = Canvas(self, width = width, height = height, bg = self.__bg_color)
        self.__canvas.pack()
        
#La fenêtre de jeu principale
class GameWindow(Window):
    
    def __init__(self,w,h):
        Window.__init__(self,w,h)
        
        
     
win = GameWindow(450,320)
#win.title("Jeu de Tarot") BUG
win.mainloop()