import tkinter as tk
from tkinter import ttk, messagebox
import random

class Introduction:
    def __init__(self, window):
        self.window = window
        self.frame_perkenalan = tk.Frame(window, width=1100, height=650)
        self.frame_perkenalan.place(x=0, y=0)

        self.backgroundd = tk.PhotoImage(file="bg/backgroundd.png")
        self.label = tk.Label(self.frame_perkenalan, image=self.backgroundd, borderwidth=0, highlightthickness=0)
        self.label.place(x=0, y=0, width=self.backgroundd.width(), height=self.backgroundd.height())

        self.txtbackgroundd = tk.PhotoImage(file="bg/text_backgroundd.png")
        self.introduction = tk.Label(self.frame_perkenalan, text="INTRODUCTION", image=self.txtbackgroundd, font=("04b", 50), fg="white", compound="center", borderwidth=0, highlightthickness=0)
        self.introduction.place(x=0, y=85, width=self.txtbackgroundd.width(), height=self.txtbackgroundd.height())

        self.txtbackgroundd1 = tk.PhotoImage(file="bg/text_backgroundd1.png")
        self.subIntro = tk.Label(self.frame_perkenalan, text="TO OUR TEAM", image=self.txtbackgroundd1, font=("04b", 30), compound="center", borderwidth=0, highlightthickness=0)
        self.subIntro.place(x=0, y=172, width=self.txtbackgroundd1.width(), height=self.txtbackgroundd1.height())

        self.sun2 = tk.Label(self.frame_perkenalan, bg="#ffbb1b")
        self.sun2.place(x=55, y=240, width=91, height=70)

        self.awan = tk.Label(self.frame_perkenalan, bg="#d9d9d9")
        self.awan.place(x=95, y=236, width=91, height=38)

        self.awann1 = tk.Label(self.frame_perkenalan, bg="#d9d9d9")
        self.awann1.place(x=65, y=266, width=149, height=38)

        self.awann1 = tk.Label(self.frame_perkenalan, bg="#d9d9d9")
        self.awann1.place(x=30, y=301, width=216, height=26)

        self.awan2 = tk.Label(self.frame_perkenalan, bg="#d9d9d9")
        self.awan2.place(x=-30, y=510, width=123, height=40)

        self.awann2 = tk.Label(self.frame_perkenalan, bg="#d9d9d9")
        self.awann2.place(x=-45, y=550, width=160, height=44)

        self.awan3 = tk.Label(self.frame_perkenalan, bg="#d9d9d9")
        self.awan3.place(x=1020, y=290, width=124, height=39)

        self.awann3 = tk.Label(self.frame_perkenalan, bg="#d9d9d9")
        self.awann3.place(x=950, y=315, width=197, height=44)

        self.buwong = tk.Label(self.frame_perkenalan, bg="black")
        self.buwong.place(x=1000, y=300, width=41, height=11)

        self.buwong1 = tk.Label(self.frame_perkenalan, bg="black")
        self.buwong1.place(x=1050, y=300, width=41, height=11)

        self.buwongg1 = tk.Label(self.frame_perkenalan, bg="black")
        self.buwongg1.place(x=1030, y=310, width=29, height=13)

        self.next = tk.Button(self.frame_perkenalan, text="Next", font=("pixelify sans", 20), bg="#6f6f6f", fg="white", command=self.to_menu)
        self.next.place(x=877, y=580, width=193, height=50)

        self.prev = tk.Button(self.frame_perkenalan, text="Prev", font=("pixelify sans", 20), bg="#6f6f6f", fg="white", command=self.back_to_welcome)
        self.prev.place(x=30, y=580, width=193, height=50)

        self.sort_button = tk.Button(self.frame_perkenalan, text="Urutkan Nickname", font=("pixelify sans", 16), bg="#4a90e2", fg="white", command=self.sort_anggota)
        self.sort_button.place(x=450, y=580, width=200, height=50)

        self.anggota_asli = [
            ["Kyzo", "foto/Abdul.png", self.info_abdul],  
            ["Araa", "foto/Araa.png", self.info_araa],    
            ["Flyy", "foto/Rafly.png", self.info_rafly],  
            ["Kalv", "foto/Surya.png", self.info_surya],          ]

        self.anggota = self.anggota_asli.copy()
        random.shuffle(self.anggota)

        self.foto_buttons = []
        self.nama_labels = []

        self.bnd = tk.PhotoImage(file="bg/bg_bok.png")
        self.bok = tk.Label(self.frame_perkenalan, image=self.bnd, borderwidth=0, highlightthickness=0)
        self.bok.place(x=100, y=480, width=950, height=30)

        self.tampilkan_anggota()

    def tampilkan_anggota(self):
        for btn in self.foto_buttons:
            btn.destroy()
        for lbl in self.nama_labels:
            lbl.destroy()

        self.foto_buttons.clear()
        self.nama_labels.clear()

        x_pos = 110
        for nama, path_foto, fungsi in self.anggota:
            foto = tk.PhotoImage(file=path_foto).subsample(4, 4)
            btn = tk.Button(self.frame_perkenalan, image=foto, borderwidth=0, highlightthickness=0, command=fungsi)
            btn.image = foto
            btn.place(x=x_pos, y=275)
            self.foto_buttons.append(btn)
            x_pos += 225

        for i, data in enumerate(self.anggota):
            lbl = tk.Label(self.bok, text=data[0], fg="#000000", font=("04b", 15))
            lbl.grid(column=i, row=1, padx=77, pady=5)
            self.nama_labels.append(lbl)

        self.shuffle_button = tk.Button(self.frame_perkenalan, text="Acak Lagi", font=("pixelify sans", 16), bg="#e26a6a", fg="white", command=self.acak_anggota)
        self.shuffle_button.place(x=240, y=580, width=200, height=50)

        self.khusus_button = tk.Button(self.frame_perkenalan, text="Urut Nama Asli", font=("pixelify sans", 16), bg="#7abf5c", fg="white", command=self.urutkan_khusus)
        self.khusus_button.place(x=660, y=580, width=200, height=50)

    def acak_anggota(self):
        random.shuffle(self.anggota)
        self.tampilkan_anggota()

    def sort_anggota(self):
        n = len(self.anggota)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if self.anggota[j][0] > self.anggota[j + 1][0]:
                    self.anggota[j], self.anggota[j + 1] = self.anggota[j + 1], self.anggota[j]
        self.tampilkan_anggota()

    def urutkan_khusus(self):
        urutan_nama_asli = ["Abdul", "Araa", "Rafly", "Surya"]
        urutan_alias = ["Kyzo", "Araa", "Flyy", "Kalv"]

        mapping_nama = {
            "Abdul": "Kyzo",
            "Araa": "Araa",
            "Rafly": "Flyy",
            "Surya": "Kalv"
        }

        hasil = []
        for nama in urutan_nama_asli:
            for anggota in self.anggota_asli:
                if anggota[0] == mapping_nama[nama]:
                    hasil.append(anggota)
                    break

        self.anggota = hasil
        self.tampilkan_anggota()

    def info_abdul(self):
        messagebox.showinfo("BIODATA ANGGOTA 1", "Nama : Abdul Ghodir Firdiansyah\nNPM   : 2417051054\nKelas  : ILKOM B\nKata Motivasi : Jangan lupa sda")

    def info_araa(self):
        messagebox.showinfo("BIODATA ANGGOTA 2", "Nama : Annisa Azzahra\nNPM   : 2417051059\nKelas  : ILKOM B\nKata Motivasi : Jangan lupa design")

    def info_rafly(self):
        messagebox.showinfo("BIODATA KETUA PROJECT", "Nama : M. Rafly Saputra\nNPM   : 2417051049\nKelas  : ILKOM B\nKata Motivasi : Jangan lupa petruk")

    def info_surya(self):
        messagebox.showinfo("BIODATA ANGGOTA 3", "Nama : M. Surya Gymnastyar\nNPM   : 2417051011\nKelas  : ILKOM B\nKata Motivasi : Jangan lupa so")