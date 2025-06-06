import tkinter as tk
from tkinter import ttk, messagebox
from component.awan import Awan
from component.burung import Burung

class Welcome:
    def __init__(self, window):
        #Frame Welcome
        self.frame_welcome = tk.Frame(window, width=1100, height=650)
        self.frame_welcome.place(x=0, y=0)
        
        #background
        self.background = tk.PhotoImage(file="bg/background.png")
        self.label = tk.Label(self.frame_welcome, image=self.background, borderwidth=0, highlightthickness=0)
        self.label.place(x=0, y=0, width=self.background.width(), height=self.background.height())
        
        #Teks
        self.backgroundtxt = tk.PhotoImage(file="bg/text_background.png")
        self.welcome = tk.Label(self.frame_welcome, text="WELCOME", font=("04b", 88), fg="white", image=self.backgroundtxt, compound="center", borderwidth=0, highlightthickness=0)
        self.welcome.place(x=10, y=40, width=self.backgroundtxt.width(), height=self.backgroundtxt.height())
        
        self.backgroundtxtt = tk.PhotoImage(file="bg/text_background1.png")
        self.subWelcome = tk.Label(self.frame_welcome, text="TO OUR PROJECT", font=("04b", 30), image=self.backgroundtxtt, compound="center", borderwidth=0, highlightthickness=0)
        self.subWelcome.place(x=110, y=169, width=self.backgroundtxtt.width(), height=self.backgroundtxtt.height())
        
        #Button
        self.button_start = tk.Button(self.frame_welcome, text="Start", font=("pixelify sans", 20),bg="#6f6f6f", fg="white", command=self.to_introduction)
        self.button_start.place(x=325, y=280, width=450, height=50)
        
        self.button_about = tk.Button(self.frame_welcome, text="About", font=("pixelify sans", 20), bg="#6f6f6f", fg="white", command=self.about)
        self.button_about.place(x=325, y=375, width=450, height=50)
        
        self.button_about = tk.Button(self.frame_welcome, text="Exit", font=("pixelify sans", 20), bg="#6f6f6f", fg="white", command=self.exit)
        self.button_about.place(x=325, y=470, width=450, height=50)
        
        #Tanah bro
        self.dirt = tk.Label(self.frame_welcome, bg="#553c2f")
        self.dirt.place(x=0, y=600, width=1100, height=50)
        
        self.dirt1 = tk.Label(self.frame_welcome, bg="#412D23")
        self.dirt1.place(x=100, y=639, width=134, height=11)
        
        self.dirt2 = tk.Label(self.frame_welcome, bg="#412D23")
        self.dirt2.place(x=500, y=620, width=79, height=12)
        
        self.dirt3 = tk.Label(self.frame_welcome, bg="#412D23")
        self.dirt3.place(x=900, y=639, width=70, height=14)
        
        self.dirt4 = tk.Label(self.frame_welcome, bg="#412D23")
        self.dirt4.place(x=1050, y=615, width=70, height=14)
        
        self.grass = tk.Label(self.frame_welcome, bg="#43772e")
        self.grass.place(x=0, y=580, width=1100, height=20)
        
        #Awan bwangg
        self.sun = tk.Label(self.frame_welcome, bg="#ffe11b")
        self.sun.place(x=55, y=227, width=91, height=70)
        
        Awan(tk=tk, frame=self.frame_welcome, bgcolor="#d9d9d9", horizontal=50, vertical=310, width=216, height=26)
        Awan(tk=tk, frame=self.frame_welcome, bgcolor="#d9d9d9", horizontal=88, vertical=274, width=149, height=38)
        Awan(tk=tk, frame=self.frame_welcome, bgcolor="#d9d9d9", horizontal=115, vertical=250, width=91, height=25)
        
        #Awan 2 bang
        Awan(tk=tk, frame=self.frame_welcome, bgcolor="#d9d9d9", horizontal=860, vertical=198, width=197, height=44.22)
        Awan(tk=tk, frame=self.frame_welcome, bgcolor="#d9d9d9", horizontal=905, vertical=170, width=123, height=28)

        #burung
        self.bird = tk.Label(self.frame_welcome, bg="black")
        self.bird.place(x=1003, y=195, width=54, height=13)
        
        self.bird1 = tk.Label(self.frame_welcome, bg="black")
        self.bird1.place(x=1080, y=196, width=54, height=15)
        
        self.bird2 = tk.Label(self.frame_welcome, bg="black")
        self.bird2.place(x=1050, y=203, width=38, height=16)
        
        #Awan 3 bang
        Awan(tk=tk, frame=self.frame_welcome, bgcolor="#d9d9d9", horizontal=1000, vertical=320, width=123.12, height=38.7)
        Awan(tk=tk, frame=self.frame_welcome, bgcolor="#d9d9d9", horizontal=950, vertical=355, width=197, height=44.22)
        
    def about(self):
        pass
    
    def exit(self):
        self.window.destroy()