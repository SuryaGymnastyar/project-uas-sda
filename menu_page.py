import tkinter as tk
from tkinter import ttk, messagebox
from component.awan import Awan

class Menu:
    def __init__(self, window):
        self.frame_menu = tk.Frame(window, width=1100, height=650)
        self.frame_menu.place(x=0, y=0)

        self.backgrounddd = tk.PhotoImage(file="bg/bg_menu.png")
        self.label = tk.Label(self.frame_menu, image=self.backgrounddd, borderwidth=0, highlightthickness=0)
        self.label.place(x=0, y=0, width=self.backgrounddd.width(), height=self.backgrounddd.height())

        #Prev
        self.prev = tk.Button(self.frame_menu, text="Prev", font=("pixelify sans", 20), bg="#6f6f6f", fg="white", command=self.back_to_introduction)
        self.prev.place(x=30, y=580, width=193, height=50)      
        
        #frame header
        self.bgrr = tk.PhotoImage(file="bg/bg_header.png")
        self.header = tk.Label(self.frame_menu, image=self.bgrr, borderwidth=0, highlightthickness=0, relief="flat", bd=0)
        self.header.place(relwidth=.9, y=50, x=60)
        
        self.logo = tk.PhotoImage(file="image/logo.png")
        self.profile = tk.Label(self.header, image=self.logo, bd=0, width="150", height="150", relief="flat", highlightthickness=0, borderwidth=0)
        self.profile.pack(side="left")

        self.bkr = tk.PhotoImage(file="bg/bg_head1.png") 
        self.h1_canvas = tk.Canvas(
            self.header, 
            width=self.bkr.width(), 
            height=self.bkr.height(),
            highlightthickness=0,
            borderwidth=0
        )
        self.h1_canvas.pack(side="left", padx=20)
        
        # Tambahkan gambar background
        self.h1_canvas.create_image(
            self.bkr.width()//2, 
            self.bkr.height()//2, 
            image=self.bkr
        )
        
        # Tambahkan teks di atas gambar
        self.h1_canvas.create_text(
            self.bkr.width()//2, 
            self.bkr.height()//2, 
            text="BLOCKBUSTER UwU", 
            fill="#FFFFFF", 
            font=("04b", 30)
        )
        
        self.bkrr = tk.PhotoImage(file="bg/bg_head2.png")
        self.h2_canvas = tk.Canvas(
            self.frame_menu, 
            width=self.bkrr.width(), 
            height=self.bkrr.height(),
            highlightthickness=0,
            borderwidth=0
        )
        self.h2_canvas.place(x=55, y=240)
        
        # Tambahkan gambar background
        self.h2_canvas.create_image(
            self.bkrr.width()//2, 
            self.bkrr.height()//2, 
            image=self.bkrr
        )
        
        # Tambahkan teks di atas gambar
        self.h2_canvas.create_text(
            self.bkrr.width()//2, 
            self.bkrr.height()//2, 
            text="Our Project:", 
            fill="#FFFFFF", 
            font=("04b", 20)
        )

        self.bgr = tk.PhotoImage(file="bg/bg_project.png")
        self.project = tk.Label(self.frame_menu, image=self.bgr, borderwidth=0, highlightthickness=0)
        self.project.place(x=35, y=290, relwidth=.9)
        
        
        
        self.project_image = [
            [tk.PhotoImage(file="image/alien.png"), lambda: self.information_project("Nama Project: Alien\nAuthor:Rafly, Tisya, Abdul\n\nPenjelasan:\nIni adalah project game pesawat untuk tembak tembak musuh aja sampe menang")], 
            [tk.PhotoImage(file="image/ff.png"), lambda: self.information_project("Nama Project: Freeding Frenzy\nAuthor:Surya, Tiwi, Alyssa\n\nPenjelasan:\nIni adalah project game ikan tapi mirip ular ketika dia makan dia akan bertumbuh")], 
            [tk.PhotoImage(file="image/kalkulator.png"), lambda: self.information_project("Nama Project: Kobiko\nAuthor:Rafly, Abdul, Tisya\n\nPenjelasan:\nIni adalah project konversi bilangan biner")], 
            [tk.PhotoImage(file="image/MiniProject.png"), self.to_project]
        ]

        self.bgrrr = tk.PhotoImage(file="bg/bg_judul.png")
        for i in range(4):
            self.image = tk.Button(self.project, image=self.project_image[i][0], borderwidth=0, highlightthickness=0, command=self.project_image[i][1])
            self.image.grid(column=i, row=0, padx=25)

            self.judul_canvas = tk.Canvas(
                self.project, 
                width=self.bgrrr.width(), 
                height=self.bgrrr.height(),
                highlightthickness=0,
                borderwidth=0
            )
            self.judul_canvas.grid(column=i, row=1, pady=10)
            
            # Tambahkan gambar background
            self.judul_canvas.create_image(
                self.bgrrr.width()//2, 
                self.bgrrr.height()//2, 
                image=self.bgrrr
            )
            
            # Tambahkan teks di atas gambar
            self.judul_canvas.create_text(
                self.bgrrr.width()//2, 
                self.bgrrr.height()//2, 
                text=f"Project {i + 1}", 
                fill="#FFFFFF", 
                font=("04b", 15)
            )
            
            # self.judul = tk.Label(self.project, image=self.bgrrr, borderwidth=0, highlightthickness=0, text=f"Project {i + 1}", fg="#000000", font=("04b", 15), compound="center", bg=self.header["bg"])
            # self.judul.grid(column=i, row=1, pady=10)
        
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
        
    def information_project(self, information):
        messagebox.showinfo("INFORMATION", information)
