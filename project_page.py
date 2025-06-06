import tkinter as tk
from tkinter import ttk, messagebox

class Project:
    def __init__(self, window):
        #Frame Kiri
        self.frame_project_left = tk.Frame(window, bg="blue", width=550, height=650)
        self.frame_project_left.place(x=0, y=0)

        #Tulisan Angka Kiri
        self.angka1 = tk.Label(self.frame_project_left, text="0", font=("pixelify sans", 150), bg="blue", fg="white")
        self.angka1.place(x=40, y=5)
        
        #Timer Kiri
        self.Timer1 = tk.Label(self.frame_project_left, text="0:00", font=('digital-7', 100), bg="darkblue", fg="white", width=4)
        self.Timer1.place(x=150, y=365)
        
        #Tombol Kiri +
        self.tombol1 = tk.Button(self.frame_project_left, text="+1", font=("pixelify sans", 10), command=self.addleft)
        self.tombol1.place(x=50, y=210, width=30, height=30)
        #Tombol Kiri -
        self.tombol1 = tk.Button(self.frame_project_left, text="-1", width=3, font=("pixelify sans", 10), command=self.minleft)
        self.tombol1.place(x=124, y=210, width=30, height=30)
        
        #Pilihan Kiri
        self.pill = ["Shukaku", "Matatabi", "Isobu", "Son Goku"]
        self.pilihanl = tk.StringVar()
        self.pilihanl.set("Pilihan")

        self.opsi1 = tk.OptionMenu(self.frame_project_left, self.pilihanl, *self.pill)
        self.opsi1.place(x=0, y=0)
        self.opsi1.config(bg="blue", fg="black", width=20, font=("Comic Sans MS", 10, "bold"))
        
        #Tombol Start/Stop
        self.start_stop = tk.Button(self.frame_project_left, text="Start", fg="white", bg="green", font=("Comic Sans MS", 12, "bold"), command=self.start_stop_fnct)
        self.start_stop.place(x=30, y=410, width=70, height=50)

        #Gambar Kiri
        self.gambarl = tk.PhotoImage(file="image/Blue.png")
        self.gambarl = self.gambarl.subsample(2, 2)
        #Letak Gambar Kiri
        self.Gambarl = tk.Label(self.frame_project_left, image=self.gambarl)
        self.Gambarl.image = self.gambarl
        self.Gambarl.place(x=250, y=40)

        #===============================================================================================================================================

        #Frame Kanan
        self.frame_project_right = tk.Frame(window, bg="red", width=550, height=650)
        self.frame_project_right.place(x=550, y=0)

        #Tulisan Angka Kanan
        self.angka2 = tk.Label(self.frame_project_right, text="0", font=("pixelify sans", 150), bg="red", fg="white")
        self.angka2.place(x=40, y=5)
        
        #Timer Kanan
        self.Timer2 = tk.Label(self.frame_project_right, text="0:00", font=('digital-7', 100), bg="darkred", fg="white", width=4)
        self.Timer2.place(x=150, y=365)
        
        #Tombol Kanan +
        self.tombol2 = tk.Button(self.frame_project_right, text="+1", width=3, font=("pixelify sans", 10), command=self.addright)
        self.tombol2.place(x=50, y=210, width=30, height=30)
        #Tombol Kanan -
        self.tombol2 = tk.Button(self.frame_project_right, text="-1", width=3, font=("pixelify sans", 10), command=self.minright)
        self.tombol2.place(x=124, y=210, width=30, height=30)
        
        #Pilihan Kanan
        self.pilr = ["Abdul", "Rara", "Rafly", "Surya"]
        self.pilihanr = tk.StringVar()
        self.pilihanr.set("Pilihan")

        self.opsi2 = tk.OptionMenu(self.frame_project_right, self.pilihanr, *self.pilr)
        self.opsi2.place(x=0, y=0)
        self.opsi2.config(bg="red", fg="black", width=20, font=("Comic Sans MS", 10, "bold"))
        
        #Gambar Kanan
        self.gambarr = tk.PhotoImage(file="image/Red.png")
        self.gambarr = self.gambarr.subsample(6, 6)
        #Letak Gambar Kanan
        self.Gambarr = tk.Label(self.frame_project_right, image=self.gambarr)
        self.Gambarr.image = self.gambarr
        self.Gambarr.place(x=250, y=40)
        
        #================================================================================================================================================

        #Frame Bawah
        self.frame_project_down = tk.Frame(window, width=1100, height=70, bg="#3b7099")
        self.frame_project_down.place(x=0, y=580)
        
        #Show/Hide Stopwach
        self.show_hide_stopwach = tk.Button(self.frame_project_down, text="Show/Hide\nStopwach", fg="black", bg="#009528", font=("Comic Sans MS", 12, "bold"))
        self.show_hide_stopwach.place(x=25, y=10, width=150, height=50)
        
        #Shikkaku Kiri
        self.shikkakul = tk.Button(self.frame_project_down, text="Shikkaku", fg="white", bg="darkblue", font=("Comic Sans MS", 12, "bold"))
        self.shikkakul.place(x=335, y=15, width=130, height=40)
        
        #Kikken Kiri
        self.kikkenl = tk.Button(self.frame_project_down, text="Kikken", fg="white", bg="darkblue", font=("Comic Sans MS", 12, "bold"))
        self.kikkenl.place(x=195, y=15, width=130, height=40)
        
        #Done
        self.done = tk.Button(self.frame_project_down, text="Done", fg="black", bg="#009528", font=("Comic Sans MS", 12, "bold"))
        self.done.place(x=475, y=10, width=150, height=50)
        
        #Shikkaku Kanan
        self.shikkakul = tk.Button(self.frame_project_down, text="Shikkaku", fg="white", bg="darkred", font=("Comic Sans MS", 12, "bold"))
        self.shikkakul.place(x=635, y=15, width=130, height=40)
        
        #Kikken Kanan
        self.shikkakul = tk.Button(self.frame_project_down, text="Kikken", fg="white", bg="darkred", font=("Comic Sans MS", 12, "bold"))
        self.shikkakul.place(x=775, y=15, width=130, height=40)
        
        #Reset Timer
        self.reset = tk.Button(self.frame_project_down, text="Reset", fg="white", bg="black", font=("Comic Sans MS", 12, "bold"))
        self.reset.place(x=950, y=18, width=120, height=35)
        
        #=======================================================================================================================================

    def addleft(self):
        temp = self.angka1.cget("text")
        temp = int(temp)
        temp += 1
            
        if temp >= 10:
            self.angka1.place_configure(x=15)
            
        self.angka1.config(text=temp)

    def minleft(self):
        temp = self.angka1.cget("text")
        temp = int(temp)
        temp -= 1
            
        if temp < 10:
            self.angka1.place_configure(x=40)
            
        self.angka1.config(text=temp)

    def addright(self):
        temp = self.angka2.cget("text")
        temp = int(temp)
        temp += 1
            
        if temp >= 10:
            self.angka2.place_configure(x=15)
            
        self.angka2.config(text=temp)

    def minright(self):
        temp = self.angka2.cget("text")
        temp = int(temp)
        temp -= 1
            
        if temp < 10:
            self.angka2.place_configure(x=40)
            
        self.angka2.config(text=temp)
            
    def timer(self):
        #Timer Kiri
        time = self.Timer1.cget("text").split(":")
        time[1] = int(time[1]) + 1
        time[0] = str(int(time[0]) + time[1] // 60)
        time[1] = str(int(time[1]) % 60)
            
        if int(time[1]) < 10:
            time[1] = "0" + time[1]
                
        time = time[0] + ":" + time[1]
            
        #Timer Kanan
        time = self.Timer2.cget("text").split(":")
        time[1] = int(time[1]) + 1
        time[0] = str(int(time[0]) + time[1] // 60)
        time[1] = str(int(time[1]) % 60)
            
        if int(time[1]) < 10:
            time[1] = "0" + time[1]
            
        time = time[0] + ":" + time[1]
            
        #Perbarui Waktu
        self.Timer1.config(text=time)
        self.Timer2.config(text=time)
            
        self.id_timer = self.window.after(1000, self.timer)
            
    def start_stop_fnct(self):
        if self.start_stop.cget("text") == "Start":
            self.start_stop.config(text="Stop")
            self.window.after(250)
            self.timer()
        elif self.start_stop.cget("text") == "Stop":
            if self.id_timer is not None:
                self.window.after_cancel(self.id_timer)
                self.start_stop.config(text="Start")