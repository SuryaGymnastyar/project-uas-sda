import tkinter as tk
from tkinter import ttk, messagebox
import csv

class Project:
    def __init__(self, window):
        self.data_pemainL = {
            "pemain": None,
            "voting": 0,
            "status": "Aman"
        }
        
        self.data_pemainR = {
            "pemain": None,
            "voting": 0,
            "status": "Aman"
        }
        
        self.pemain_aktif = [False, False]
        self.pemain_selesai = []
        
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

        self.opsi1 = tk.OptionMenu(self.frame_project_left, self.pilihanl, *self.pill, command=lambda value: self.simpan_pemain(value, "rafly"))
        self.opsi1.place(x=180, y=0)
        self.opsi1.config(bg="blue", fg="black", width=20, font=("Comic Sans MS", 10, "bold"))
        
        #Tombol Start/Stop
        self.start_stop = tk.Button(self.frame_project_left, state="disabled", text="Start", fg="white", bg="green", font=("Comic Sans MS", 12, "bold"), command=self.start_stop_fnct)
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

        self.opsi2 = tk.OptionMenu(self.frame_project_right, self.pilihanr, *self.pilr, command=lambda value: self.simpan_pemain(value, "naruto"))
        self.opsi2.place(x=180, y=0)
        self.opsi2.config(bg="red", fg="black", width=20, font=("Comic Sans MS", 10, "bold"))
        
        #Gambar Kanan
        self.gambarr = tk.PhotoImage(file="image/Red.png")
        self.gambarr = self.gambarr.subsample(6, 6)
        #Letak Gambar Kanan
        self.Gambarr = tk.Label(self.frame_project_right, image=self.gambarr)
        self.Gambarr.image = self.gambarr
        self.Gambarr.place(x=250, y=80)
        
        self.next_round = tk.Button(self.frame_project_right, state="disabled", text="Next\nRound", bg="darkred", fg="white",  font=("Comic Sans MS", 12, "bold"), command=self.Next_Round)
        self.next_round.place(x=440, y=400, width=80, height=50)
        
        self.round = tk.Label(self.frame_project_left, text="Round 1", bg="darkblue", fg="white",  font=("Comic Sans MS", 12, "bold"))
        self.round.place(x=25, y=5, width=80, height=40)
        
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
        
        self.close = tk.Button(self.frame_project_up, text="close", font=("comic sans ms", 12, "italic", "bold"), fg="white", bg="red", anchor="center", command=self.Close)
        self.close.place(x=1000, y=10, width=80, height=30)
        
        #================================================================================================================================================

        #Frame Bawah
        self.frame_project_down = tk.Frame(window, width=1100, height=70, bg="#3b7099")
        self.frame_project_down.place(x=0, y=580)
        
        #Show/Hide Stopwach
        self.show_hide_stopwach = tk.Button(self.frame_project_down, text="Show/Hide\nStopwach", fg="black", bg="#009528", font=("Comic Sans MS", 12, "bold"), command=self.Show_hide_stowatch)
        self.show_hide_stopwach.place(x=25, y=10, width=150, height=50)
        
        #Shikkaku Kiri
        self.shikkakul = tk.Button(self.frame_project_down, state="disabled", text="Shikkaku", fg="white", bg="darkblue", font=("Comic Sans MS", 12, "bold"), command=self.Shikkaku_left)
        self.shikkakul.place(x=195, y=15, width=130, height=40)
        
        #Kikken Kiri
        self.kikkenl = tk.Button(self.frame_project_down, state="disabled", text="Kikken", fg="white", bg="darkblue", font=("Comic Sans MS", 12, "bold"), command=self.Kikken_left)
        self.kikkenl.place(x=335, y=15, width=130, height=40)
        
        #Done
        self.done = tk.Button(self.frame_project_down, state="disabled", text="Done", fg="black", bg="#009528", font=("Comic Sans MS", 12, "bold"), command=self.done_fnct)
        self.done.place(x=475, y=10, width=150, height=50)
        
        #Shikkaku Kanan
        self.shikkakuR = tk.Button(self.frame_project_down, state="disabled", text="Shikkaku", fg="white", bg="darkred", font=("Comic Sans MS", 12, "bold"), command=self.Shikkaku_right)
        self.shikkakuR.place(x=635, y=15, width=130, height=40)
        
        #Kikken Kanan
        self.kikkenR = tk.Button(self.frame_project_down, state="disabled", text="Kikken", fg="white", bg="darkred", font=("Comic Sans MS", 12, "bold"), command=self.Kikken_right)
        self.kikkenR.place(x=775, y=15, width=130, height=40)
        
        #Reset Timer
        self.reset = tk.Button(self.frame_project_down, text="Reset", fg="white", bg="black", font=("Comic Sans MS", 12, "bold"), command=self.reset_fnct)
        self.reset.place(x=950, y=18, width=120, height=35)
        
        #=======================================================================================================================================

    def addleft(self):
        angka1 = int(self.angka1.cget("text"))
        
        angka2 = int(self.angka2.cget("text"))
        
        jugdes = int(self.n_jugdes.cget("text"))
        
        angka = angka1 + angka2
        
        if angka != jugdes:
            angka1 += 1
            
        if angka1 >= 10:
            self.angka1.place_configure(x=0)
            
        self.data_pemainL["voting"] = angka1
        self.angka1.config(text=angka1)

    def minleft(self):
        angka = int(self.angka1.cget("text"))
        if angka > 0:
            angka -= 1
            
        if angka < 10:
            self.angka1.place_configure(x=42)
            
        self.data_pemainL["voting"] = angka
        self.angka1.config(text=angka)

    def addright(self):
        angka2 = int(self.angka2.cget("text"))
        angka1 = int(self.angka1.cget("text"))
        jugdes = int(self.n_jugdes.cget("text"))
        
        angka = angka1 + angka2
        
        if angka != jugdes:
            angka2 += 1
            
        if angka2 >= 10:
            self.angka1.place_configure(x=0)
            
        self.data_pemainR["voting"] = angka2
        self.angka2.config(text=angka2)

    def minright(self):
        angka = int(self.angka2.cget("text"))
        if angka > 0:
            angka -= 1
            
        if angka < 10:
            self.angka2.place_configure(x=42)
            
        self.data_pemainR["voting"] = angka
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
            self.opsi1.place_forget()
            self.opsi2.place_forget()
            self.tingkat.place_forget()
            self.done.config(state="disabled")
            self.reset.config(state="disabled")
            self.kikkenl.config(state="normal")
            self.kikkenR.config(state="normal")
            self.shikkakul.config(state="normal")
            self.shikkakuR.config(state="normal")
            self.started = True
            self.start_stop.config(text="Stop")
            self.window.after(250)
            self.timer()
        elif self.start_stop.cget("text") == "Stop":
            if self.id_timer is not None:
                self.done.config(state="normal")
                self.reset.config(state="normal")
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
                self.done.config(state="disabled")
                self.start_stop.config(state="disabled")
                self.pemain_aktif = [False, False]
                self.data_pemainL = {"pemain": None, "voting": None, "status": "Aman" }
                self.data_pemainR = {"pemain": None, "voting": None, "status": "Aman" }
                self.opsi1.place(x=180, y=0)
                self.opsi2.place(x=180, y=0)
                
        except AttributeError:
            self.started = False
            self.angka1.config(text="0")
            self.angka2.config(text="0")
                
            self.Timer1.config(text="0:00")
            self.Timer2.config(text="0:00")
        
            self.pilihanr.set("Pilihan")
            self.pilihanl.set("Pilihan")
            self.done.config(state="disabled")
            self.start_stop.config(state="disabled")
            self.pemain_aktif = [False, False]
            self.data_pemainL = {"pemain": None, "voting": None, "status": "Aman" }
            self.data_pemainR = {"pemain": None, "voting": None, "status": "Aman" }
            self.opsi1.place(x=180, y=0)
            self.opsi2.place(x=180, y=0)
            
    def simpan_pemain(self, value, tim):   
        if tim == "rafly":
            del self.pemain_aktif[0]
            self.data_pemainL["pemain"] = value
            self.pemain_aktif.insert(0, value)
        else:
            del self.pemain_aktif[1]
            self.data_pemainR["pemain"] = value
            self.pemain_aktif.insert(1, value)   
        
        self.cek_pemain_aktif()
        
    def cek_pemain_aktif(self):
        if False not in self.pemain_aktif:
            self.start_stop.config(state="normal")
            
    def Next_Round(self):
        if len(self.pill) > 0:
            self.next_round.config(state="disabled")
            round = int(self.round.cget("text").split(" ")[1])
            round = f"Ronde {round + 1}"
            self.round.config(text=round)
        
            # TAMPILKAN OPSI
            self.opsi1.place(x=180, y=0)
            self.opsi2.place(x=180, y=0)
            self.tingkat.place(x=475, y=0, width=150, height=50)
            self.shikkakul.config(state="disabled")
            self.shikkakuR.config(state="disabled")
            self.kikkenl.config(state="disabled")
            self.kikkenR.config(state="disabled")
        
    def done_fnct(self):
        data = [self.data_pemainL, self.data_pemainR]
        
        self.writeData(match=self.round.cget("text"), level=self.division.get(), time=self.Timer1.cget("text"), data=data)
        self.next_round.config(state="normal")
        
        # CEK PILIHAN
        if len(self.pill) <= 1: self.next_round.config(state="disabled")
        
         # HILANGKAN OPSI PEMAIN YANG SUDAH MAIN
        self.pill.remove(self.pemain_aktif[0])
        self.pilr.remove(self.pemain_aktif[1])
        
        self.opsi1["menu"].delete(0, "end")
        self.opsi2["menu"].delete(0, "end")
        
        for item in self.pill:
            self.opsi1["menu"].add_command(
            label=item,
            command=tk._setit(self.pilihanl, item, lambda value=item: self.simpan_pemain(value, "rafly"))
        )
            
        for item in self.pilr:
            self.opsi2["menu"].add_command(
            label=item,
            command=tk._setit(self.pilihanr, item, lambda value=item: self.simpan_pemain(value, "naruto"))
        )
            
        self.reset_fnct()
        self.opsi1.place_forget()
        self.opsi2.place_forget()
    
    def Shikkaku_left(self):
        self.start_stop.config(state="disabled")
        self.shikkakul.config(state="disabled")
        self.shikkakuR.config(state="disabled")
        self.kikkenl.config(state="disabled")
        self.kikkenR.config(state="disabled")
           
        self.started = False
        self.window.after_cancel(self.id_timer)
        
        self.data_pemainL["status"] = "diskualifikasi"
        self.data_pemainL["pemain"] = "Blockbuster"
        data = [self.data_pemainL, self.data_pemainR]
        self.writeData(match=self.round.cget("text"), level=self.division.get(), time=self.Timer1.cget("text"), data=data)
        
    
    def Kikken_left(self):
        self.reset.config(state="disabled")
        self.next_round.config(state="normal")
        self.shikkakul.config(state="disabled")
        self.shikkakuR.config(state="disabled")
        self.kikkenl.config(state="disabled")
        self.kikkenR.config(state="disabled")
        self.started = False
        self.window.after_cancel(self.id_timer)
        self.start_stop.config(text="Start")
        
        
        self.data_pemainL["status"] = "diskualifikasi"
        data = [self.data_pemainL, self.data_pemainR]
        self.writeData(match=self.round.cget("text"), level=self.division.get(), time=self.Timer1.cget("text"), data=data)
        self.pill.remove(self.pemain_aktif[0])
        self.pilr.remove(self.pemain_aktif[1])
        
        self.opsi1["menu"].delete(0, "end")
        self.opsi2["menu"].delete(0, "end")
        
        for item in self.pill:
            self.opsi1["menu"].add_command(
            label=item,
            command=tk._setit(self.pilihanl, item, lambda value=item: self.simpan_pemain(value, "rafly"))
        )
            
        for item in self.pilr:
            self.opsi2["menu"].add_command(
            label=item,
            command=tk._setit(self.pilihanr, item, lambda value=item: self.simpan_pemain(value, "naruto"))
        )
        
        self.reset_fnct()
        self.opsi1.place_forget()
        self.opsi2.place_forget()
        
        
    def Shikkaku_right(self):
        self.start_stop.config(state="disabled")
        self.shikkakul.config(state="disabled")
        self.shikkakuR.config(state="disabled")
        self.kikkenl.config(state="disabled")
        self.kikkenR.config(state="disabled")
        self.started = False
        self.window.after_cancel(self.id_timer)
        
        self.data_pemainR["status"] = "diskualifikasi"
        self.data_pemainR["pemain"] = "Nullbyte"
        data = [self.data_pemainL, self.data_pemainR]
        self.writeData(match=self.round.cget("text"), level=self.division.get(), time=self.Timer1.cget("text"), data=data)
        
    def Kikken_right(self):
        self.reset.config(state="disabled")
        self.next_round.config(state="normal")
        self.shikkakul.config(state="disabled")
        self.shikkakuR.config(state="disabled")
        self.kikkenl.config(state="disabled")
        self.kikkenR.config(state="disabled")
        self.started = False
        self.window.after_cancel(self.id_timer)
        self.start_stop.config(text="Start")
        
        
        self.data_pemainR["status"] = "diskualifikasi"
        data = [self.data_pemainL, self.data_pemainR]
        self.writeData(match=self.round.cget("text"), level=self.division.get(), time=self.Timer1.cget("text"), data=data)
        self.pill.remove(self.pemain_aktif[0])
        self.pilr.remove(self.pemain_aktif[1])
        
        self.opsi1["menu"].delete(0, "end")
        self.opsi2["menu"].delete(0, "end")
        
        for item in self.pill:
            self.opsi1["menu"].add_command(
            label=item,
            command=tk._setit(self.pilihanl, item, lambda value=item: self.simpan_pemain(value, "rafly"))
        )
            
        for item in self.pilr:
            self.opsi2["menu"].add_command(
            label=item,
            command=tk._setit(self.pilihanr, item, lambda value=item: self.simpan_pemain(value, "naruto"))
        )
            
        self.reset_fnct()
        self.opsi1.place_forget()
        self.opsi2.place_forget()
    
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
                
    def Close(self):
        try:
            if not self.started:
                self.back_to_menu()
        except AttributeError:
            self.back_to_menu()
            
    def getData(self):
        data = []
        with open('data.csv', newline='', encoding='utf-8') as file:
            read = csv.DictReader(file)
            for baris in read:
                data.append(baris)    
            file.close()
        return data
    
    def writeData(self, match, time, level, data):
        newData = [
            {
                "match": match,
                "time": time,
                "level": level,
                **data[0]
            },
            {
                "match": match,
                "time": time,
                "level": level,
                **data[1]
            }
        ]
        with open('data.csv', mode='a', newline='', encoding='utf-8') as file:
            write = csv.DictWriter(file, fieldnames=["match","pemain","time","voting","level","status"])
            if isinstance(data, list):
                write.writerows(newData)
            else:
                write.writerow(data)