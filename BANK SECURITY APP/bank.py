from tkinter import *
from PIL import ImageTk, Image, ImageSequence
from tkinter import messagebox

class Atm:
    __counter=0
    def __init__(self):
        self.__pin=""
        self.__balance=100000
        self.CARD_NO=Atm.__counter
        Atm.__counter+=1
        self.menu()