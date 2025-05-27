from menu_page import Menu
import tkinter as tk
from tkinter import ttk, messagebox

class Introduction:
    def __init__(self, window):
        self.window = window
        self.frame_perkenalan = tk.Frame(window, width=1100, height=650)
        self.frame_perkenalan.place(x=0, y=0)
        
        #Text
        self.introduction = tk.Label(self.frame_perkenalan, text="INTRODUCTION", font=("04b", 50))
        self.introduction.place(x=200, y=150)
        
        #Foto
        self.foto1 = tk.PhotoImage(file="foto/Abdul.png")
        self.foto1 = self.foto1.subsample(7, 7)
        self.Foto1 = tk.Label(self.frame_perkenalan, image=self.foto1)
        self.Foto1.image = self.foto1
        self.Foto1.place(x=200, y=300)
        
        self.foto2 = tk.PhotoImage(file="foto/Araa.png")
        self.foto2 = self.foto2.subsample(7, 7)
        self.Foto2 = tk.Label(self.frame_perkenalan, image=self.foto2)
        self.Foto2.image = self.foto2
        self.Foto2.place(x=400, y=300)

        self.foto3 = tk.PhotoImage(file="foto/Rafly.png")
        self.foto3 = self.foto3.subsample(7, 7)
        self.Foto3 = tk.Label(self.frame_perkenalan, image=self.foto3)
        self.Foto3.image = self.foto3
        self.Foto3.place(x=600, y=300)
        
        self.foto4 = tk.PhotoImage(file="foto/Surya.png")
        self.foto4 = self.foto4.subsample(7, 7)
        self.Foto4 = tk.Label(self.frame_perkenalan, image=self.foto4)
        self.Foto4.image = self.foto4
        self.Foto4.place(x=800, y=300)
        
        self.next = tk.Button(self.frame_perkenalan, text="Next", font=("pixelify sans", 20), command=self.to_menu)
        self.next.place(x=980, y=580)
        
    def to_menu(self):
        self.frame_perkenalan.place_forget
        menu = Menu(self.window)