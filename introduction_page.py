import tkinter as tk
from tkinter import ttk, messagebox

class Introduction:
    def __init__(self, window):
        self.frame_perkenalan = tk.Frame(window, width=1100, height=650)
        self.frame_perkenalan.place(x=0, y=0)
        
        self.backgroundd = tk.PhotoImage(file="bg/backgroundd.png")
        self.label = tk.Label(self.frame_perkenalan, image=self.backgroundd, borderwidth=0, highlightthickness=0)
        self.label.place(x=0, y=0, width=self.backgroundd.width(), height=self.backgroundd.height())

        #Text
        self.txtbackgroundd = tk.PhotoImage(file="bg/text_backgroundd.png")
        self.introduction = tk.Label(self.frame_perkenalan, text="INTRODUCTION", image=self.txtbackgroundd, font=("04b", 50), fg="white",compound="center", borderwidth=0, highlightthickness=0)
        self.introduction.place(x=0, y=85, width=self.txtbackgroundd.width(), height=self.txtbackgroundd.height())

        self.txtbackgroundd1 = tk.PhotoImage(file="bg/text_backgroundd1.png")
        self.subIntro = tk.Label(self.frame_perkenalan, text="TO OUR TEAM", image=self.txtbackgroundd1, font=("04b", 30), compound="center", borderwidth=0, highlightthickness=0)
        self.subIntro.place(x=0, y=172, width=self.txtbackgroundd1.width(), height=self.txtbackgroundd1.height())
        
        #Matahari + Awan Senja
        self.sun2 = tk.Label(self.frame_perkenalan, bg="#ffbb1b")
        self.sun2.place(x=55, y=240, width=91, height=70)

        self.awan = tk.Label(self.frame_perkenalan, bg="#d9d9d9")
        self.awan.place(x=95, y=236, width=91, height=38)
        
        self.awann1 = tk.Label(self.frame_perkenalan, bg="#d9d9d9")
        self.awann1.place(x=65, y=266, width=149, height=38)

        self.awann1 = tk.Label(self.frame_perkenalan, bg="#d9d9d9")
        self.awann1.place(x=30, y=301, width=216, height=26)

        #Awan 2
        self.awan2 = tk.Label(self.frame_perkenalan, bg="#d9d9d9")
        self.awan2.place(x=-30, y=510, width=123, height=40)
        
        self.awann2 = tk.Label(self.frame_perkenalan, bg="#d9d9d9")
        self.awann2.place(x=-45, y=550, width=160, height=44)

        #Awan 3
        self.awan3 = tk.Label(self.frame_perkenalan, bg="#d9d9d9")
        self.awan3.place(x=1020, y=290, width=124, height=39)
        
        self.awann3 = tk.Label(self.frame_perkenalan, bg="#d9d9d9")
        self.awann3.place(x=950, y=315, width=197, height=44)

        #Buwung Puyoh
        self.buwong = tk.Label(self.frame_perkenalan, bg="black")
        self.buwong.place(x=1000, y=300, width=41, height=11)
        
        self.buwong1 = tk.Label(self.frame_perkenalan, bg="black")
        self.buwong1.place(x=1050, y=300, width=41, height=11)

        self.buwongg1 = tk.Label(self.frame_perkenalan, bg="black")
        self.buwongg1.place(x=1030, y=310, width=29, height=13)

        #Next
        self.next = tk.Button(self.frame_perkenalan, text="Next", font=("pixelify sans", 20), bg="#6f6f6f", fg="white", command=self.to_menu)
        self.next.place(x=877, y=580, width=193, height=50)

        #Prev
        self.prev = tk.Button(self.frame_perkenalan, text="Prev", font=("pixelify sans", 20), bg="#6f6f6f", fg="white", command=self.to_welcome)
        self.prev.place(x=30, y=580, width=193, height=50)        
        
        #Foto
        self.foto1 = tk.PhotoImage(file="foto/Abdul.png")
        self.foto1 = self.foto1.subsample(4, 4)
        self.Foto1 = tk.Label(self.frame_perkenalan, image=self.foto1)
        self.Foto1.image = self.foto1
        self.Foto1.place(x=110, y=275)
        
        self.foto2 = tk.PhotoImage(file="foto/Araa.png")
        self.foto2 = self.foto2.subsample(4, 4)
        self.Foto2 = tk.Label(self.frame_perkenalan, image=self.foto2)
        self.Foto2.image = self.foto2
        self.Foto2.place(x=335, y=275)

        self.foto3 = tk.PhotoImage(file="foto/Rafly.png")
        self.foto3 = self.foto3.subsample(4, 4)
        self.Foto3 = tk.Label(self.frame_perkenalan, image=self.foto3)
        self.Foto3.image = self.foto3
        self.Foto3.place(x=560, y=275)
        
        self.foto4 = tk.PhotoImage(file="foto/Surya.png")
        self.foto4 = self.foto4.subsample(4, 4)
        self.Foto4 = tk.Label(self.frame_perkenalan, image=self.foto4)
        self.Foto4.image = self.foto4
        self.Foto4.place(x=785, y=275)
