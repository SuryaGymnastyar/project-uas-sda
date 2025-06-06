import tkinter as tk
from tkinter import ttk, messagebox
from component.awan import Awan

class Menu:
    def __init__(self, window):
        self.frame_menu = tk.Frame(window, width=1100, height=650)
        self.frame_menu.place(x=0, y=0)

        #Prev
        self.prev = tk.Button(self.frame_menu, text="Prev", font=("pixelify sans", 20), bg="#6f6f6f", fg="white", command=self.to_menu)
        self.prev.place(x=30, y=580, width=193, height=50)      
        
        #frame header
        self.header = tk.Label(self.frame_menu, border=0)
        self.header.place(relwidth=.9, y=50, x=60)
        
        self.profile = tk.Frame(self.header, bd=2, width="150", height="150", relief="solid")
        self.profile.pack(side="left")
        
        self.h1 = tk.Label(self.header, border=0, text="Rafsanss", font=("04b", 40), fg="#000", highlightthickness=0)
        self.h1.pack(side="left", padx=20)
        
        self.h2 = tk.Label(self.frame_menu, text="Our Project:", font=("04b", 20), fg="#000", highlightthickness=0)
        self.h2.place(x=55, y=240)
        
        self.project = tk.Label(self.frame_menu)
        self.project.place(x=35, y=290, relwidth=.9)
        
        for i in range(4):
            self.box = tk.Frame(self.project, bd=2, relief="solid", width="200", height="200", background="#f6f6f6")
            self.box.grid(column=i, row=0, padx=25)
            
            self.judul = tk.Label(self.project, text=f"Project {i + 1}", fg="#000000", font=("04b", 15))
            self.judul.grid(column=i, row=1, pady=10)
            
        # KOMPONEN
        self.elm = tk.Frame(self.frame_menu, width=10, height=10, bg="#FCF998")
        self.elm.place(x=15, y=120)
        
        # ELEMEN
        self.elm = tk.Frame(self.frame_menu, width=10, height=10, bg="#FCF998")
        self.elm.place(x=230, y=30)
        self.elm = tk.Frame(self.frame_menu, width=10, height=10, bg="#FCF998")
        self.elm.place(x=430, y=45)
        self.elm = tk.Frame(self.frame_menu, width=10, height=10, bg="#FCF998")
        self.elm.place(x=630, y=60)
        self.elm = tk.Frame(self.frame_menu, width=10, height=10, bg="#FCF998")
        self.elm.place(x=1050, y=30)
        self.elm = tk.Frame(self.frame_menu, width=10, height=10, bg="#FCF998")
        self.elm.place(x=770, y=180)
        self.elm = tk.Frame(self.frame_menu, width=10, height=10, bg="#FCF998")
        self.elm.place(x=900, y=100)
        
        # matahari
        self.elm = tk.Frame(self.frame_menu, width=100, height=80, bg="#FCF998")
        self.elm.place(x=910, y=120)
        
        # awan
        Awan(tk=tk, frame=self.frame_menu, bgcolor="#d9d9d9", horizontal=970, vertical=155, width=110, height=30)
        Awan(tk=tk, frame=self.frame_menu, bgcolor="#d9d9d9", horizontal=950, vertical=180, width=147, height=38)
        Awan(tk=tk, frame=self.frame_menu, bgcolor="#d9d9d9", horizontal=910, vertical=210, width=300, height=25)