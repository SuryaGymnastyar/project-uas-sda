import tkinter as tk
from tkinter import ttk, messagebox

class Project:
    def __init__(self, window):
        #Frame Kiri
        self.frame_project_left = tk.Frame(window, bg="blue", width=550, height=650)
        self.frame_project_left.place(x=0, y=50)

        #Tulisan Angka Kiri
        self.angka1 = tk.Label(self.frame_project_left, text="0", font=("comic sans ms", 150), bg="blue", fg="white")
        self.angka1.place(x=42, y=45, height=200)
        
        #Timer Kiri
        self.Timer1 = tk.Label(self.frame_project_left, text="0:00", font=('digital-7', 100), bg="darkblue", fg="white", width=4)
        self.Timer1.place(x=150, y=365)
        
        #Tombol Kiri +
        self.tombol1 = tk.Button(self.frame_project_left, text="+1", font=("comic sans ms", 10), command=self.addleft)
        self.tombol1.place(x=50, y=250, width=30, height=30)
        #Tombol Kiri -
        self.tombol1 = tk.Button(self.frame_project_left, text="-1", width=3, font=("comic sans ms", 10), command=self.minleft)
        self.tombol1.place(x=124, y=250, width=30, height=30)
        
        #Pilihan Kiri
        self.pill = ["Abdul", "Rara", "Rafly", "Surya"]
        self.pilihanl = tk.StringVar()
        self.pilihanl.set("Pilihan")

        self.opsi1 = tk.OptionMenu(self.frame_project_left, self.pilihanl, *self.pill)
        self.opsi1.place(x=180, y=0)
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
        self.Gambarl.place(x=250, y=80)

        #===============================================================================================================================================

        #Frame Kanan
        self.frame_project_right = tk.Frame(window, bg="red", width=550, height=650)
        self.frame_project_right.place(x=550, y=50)

        #Tulisan Angka Kanan
        self.angka2 = tk.Label(self.frame_project_right, text="0", font=("comic sans ms", 150), bg="red", fg="white")
        self.angka2.place(x=42, y=45, height=200)
        
        #Timer Kanan
        self.Timer2 = tk.Label(self.frame_project_right, text="0:00", font=('digital-7', 100), bg="darkred", fg="white", width=4)
        self.Timer2.place(x=150, y=365)
        
        #Tombol Kanan +
        self.tombol2 = tk.Button(self.frame_project_right, text="+1", width=3, font=("comic sans ms", 10), command=self.addright)
        self.tombol2.place(x=50, y=250, width=30, height=30)
        #Tombol Kanan -
        self.tombol2 = tk.Button(self.frame_project_right, text="-1", width=3, font=("comic sans ms", 10), command=self.minright)
        self.tombol2.place(x=124, y=250, width=30, height=30)
        
        #Pilihan Kanan
        self.pilr = ["Naruto", "Sasuke", "Sakura", "Kakashi"]
        self.pilihanr = tk.StringVar()
        self.pilihanr.set("Pilihan")

        self.opsi2 = tk.OptionMenu(self.frame_project_right, self.pilihanr, *self.pilr)
        self.opsi2.place(x=180, y=0)
        self.opsi2.config(bg="red", fg="black", width=20, font=("Comic Sans MS", 10, "bold"))
        
        #Gambar Kanan
        self.gambarr = tk.PhotoImage(file="image/Red.png")
        self.gambarr = self.gambarr.subsample(6, 6)
        #Letak Gambar Kanan
        self.Gambarr = tk.Label(self.frame_project_right, image=self.gambarr)
        self.Gambarr.image = self.gambarr
        self.Gambarr.place(x=250, y=80)
        
        #================================================================================================================================================
        
        #Frame Atas
        self.frame_project_up = tk.Frame(window, width=1100, height=50, bg="#000000")
        self.frame_project_up.place(x=0, y=0)
        
        #Divisi atau Tingkatan
        self.tingkatan = ["Beginer", "Advance", "Intermediate", "Champion"]
        self.division = tk.StringVar()
        self.division.set("Beginer")

        self.tingkat = tk.OptionMenu(self.frame_project_up, self.division, *self.tingkatan)
        self.tingkat.place(x=475, y=0, width=150, height=50)
        self.tingkat.config(bg="black", fg="white", width=20, font=("Comic Sans MS", 12, "bold"), anchor="center")
        
        #Juri
        self.jugdes = tk.Label(self.window, text="Jugdes", font=("comic sans ms", 15), bg="black", fg="white", anchor="center")
        self.jugdes.place(x=515, y=85, width=70, height=30)
        
        #Jumlah Juri
        self.n_jugdes = tk.Label(self.window, text=5, font=("comic sans ms", 30, "bold"), bg="black", fg="white", anchor="center")
        self.n_jugdes.place(x=527, y=50, width=46, height=35)
        
        #Tim Biru
        self.Ao = tk.Label(self.frame_project_up, text="Ao", font=("comic sans ms", 30), bg="black", fg="blue")
        self.Ao.place(x=100, y=0, width=80, height=50)
        
        self.Ao_name = tk.Label(self.frame_project_up, text="Blockbuster", font=("comic sans ms", 25), bg="black", fg="blue")
        self.Ao_name.place(x=200, y=0, width=200, height=50)
        
        #Team Aka 
        self.Ao = tk.Label(self.frame_project_up, text="Aka", font=("comic sans ms", 30), bg="black", fg="red")
        self.Ao.place(x=650, y=0, width=100, height=50)
        
        self.Ao_name = tk.Label(self.frame_project_up, text="Nullbyte", font=("comic sans ms", 25), bg="black", fg="red")
        self.Ao_name.place(x=750, y=0, width=200, height=50)
        
        self.close = tk.Button(self.frame_project_up, text="close", font=("comic sans ms", 12, "italic", "bold"), fg="white", bg="red", anchor="center", command=self.back_to_menu)
        self.close.place(x=1000, y=10, width=80, height=30)
        
        #================================================================================================================================================

        #Frame Bawah
        self.frame_project_down = tk.Frame(window, width=1100, height=70, bg="#3b7099")
        self.frame_project_down.place(x=0, y=580)
        
        #Show/Hide Stopwach
        self.show_hide_stopwach = tk.Button(self.frame_project_down, text="Show/Hide\nStopwach", fg="black", bg="#009528", font=("Comic Sans MS", 12, "bold"), command=self.Show_hide_stowatch)
        self.show_hide_stopwach.place(x=25, y=10, width=150, height=50)
        
        #Shikkaku Kiri
        self.shikkakul = tk.Button(self.frame_project_down, text="Shikkaku", fg="white", bg="darkblue", font=("Comic Sans MS", 12, "bold"))
        self.shikkakul.place(x=195, y=15, width=130, height=40)
        
        #Kikken Kiri
        self.kikkenl = tk.Button(self.frame_project_down, text="Kikken", fg="white", bg="darkblue", font=("Comic Sans MS", 12, "bold"))
        self.kikkenl.place(x=335, y=15, width=130, height=40)
        
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
        self.reset = tk.Button(self.frame_project_down, text="Reset", fg="white", bg="black", font=("Comic Sans MS", 12, "bold"), command=self.reset_fnct)
        self.reset.place(x=950, y=18, width=120, height=35)
        
        #=======================================================================================================================================

    def addleft(self):
        angka1 = self.angka1.cget("text")
        angka1 = int(angka1)
        
        angka2 = self.angka2.cget("text")
        angka2 = int(angka2)
        
        jugdes = self.n_jugdes.cget("text")
        jugdes = int(jugdes)
        
        angka = angka1 + angka2
        
        if angka != jugdes:
            angka1 += 1
            
        if angka1 >= 10:
            self.angka1.place_configure(x=0)
            
        self.angka1.config(text=angka1)

    def minleft(self):
        angka = self.angka1.cget("text")
        angka = int(angka)
        if angka > 0:
            angka -= 1
            
        if angka < 10:
            self.angka1.place_configure(x=42)
            
        self.angka1.config(text=angka)

    def addright(self):
        angka2 = self.angka2.cget("text")
        angka2 = int(angka2)
        
        angka1 = self.angka1.cget("text")
        angka1 = int(angka1)
        
        jugdes = self.n_jugdes.cget("text")
        jugdes = int(jugdes)
        
        angka = angka1 + angka2
        
        if angka != jugdes:
            angka2 += 1
            
        if angka2 >= 10:
            self.angka1.place_configure(x=0)
            
        self.angka2.config(text=angka2)

    def minright(self):
        angka = self.angka2.cget("text")
        angka = int(angka)
        if angka > 0:
            angka -= 1
            
        if angka < 10:
            self.angka2.place_configure(x=42)
            
        self.angka2.config(text=angka)
 
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
            self.started = True
            self.start_stop.config(text="Stop")
            self.window.after(250)
            self.timer()
        elif self.start_stop.cget("text") == "Stop":
            if self.id_timer is not None:
                self.started = False
                self.window.after_cancel(self.id_timer)
                self.start_stop.config(text="Start")
                
    def reset_fnct(self):
        try:
            if not self.started:
                self.angka1.config(text="0")
                self.angka2.config(text="0")
                
                self.Timer1.config(text="0:00")
                self.Timer2.config(text="0:00")
                
                self.pilihanr.set("Pilihan")
                self.pilihanl.set("Pilihan")
        except AttributeError:
            self.started = False
            self.angka1.config(text="0")
            self.angka2.config(text="0")
                
            self.Timer1.config(text="0:00")
            self.Timer2.config(text="0:00")
                
            self.pilihanr.set("Pilihan")
            self.pilihanl.set("Pilihan")
    def done_fnct(self):
        # CSV
        pass
    
    def Shikkaku_left(self):
        # Tim kiri gugur
        pass
    
    def Kikken_left(self):
        # 1 Orang tim kiri gugur
        pass
        
    def Shikkaku_left(self):
        # Tim kiri gugur
        pass
        
    def Kikken_left(self):
        # 1 Orang tim kiri gugur
        pass
    
    def Show_hide_stowatch(self):
        try:
            if self.is_place:
                self.is_place = False
                self.start_stop.place_forget()
                self.Timer1.place_forget()
                self.Timer2.place_forget()
            elif not self.is_place:
                self.is_place = True
                self.start_stop.place(x=30, y=410)
                self.Timer1.place(x=150, y=365)
                self.Timer2.place(x=150, y=365)
        except AttributeError:
                self.is_place = False
                self.start_stop.place_forget()
                self.Timer1.place_forget()
                self.Timer2.place_forget()