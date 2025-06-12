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
        Awan(tk=tk, frame=self.frame_welcome, bgcolor="#A5A2A2", horizontal=1000, vertical=320, width=123.12, height=38.7)
        Awan(tk=tk, frame=self.frame_welcome, bgcolor="#A5A2A2", horizontal=950, vertical=355, width=197, height=44.22)
        
        #Easter Egg
        self.getCodee = tk.Button(self.frame_welcome, text="", bg="#d9d9d9", command=self.easter_egg, borderwidth=0, highlightthickness=0)
        self.getCodee.place(x=115, y=250, width=91, height=25)
        
        self.buttonCode = tk.Button(self.frame_welcome, text="", bg="#d9d9d9", command=self.getCodew, borderwidth=0, highlightthickness=0)
        self.buttonCode.place(x=88, y=274, width=149, height=38)
        
        self.buttonCode1 = tk.Button(self.frame_welcome, text="", bg="#d9d9d9", command=self.getCodeww, borderwidth=0, highlightthickness=0)
        self.buttonCode1.place(x=905, y=170, width=123, height=28)
        
        self.buttonCode2 = tk.Button(self.frame_welcome, text="", bg="#A5A2A2", command=self.getCodewww, borderwidth=0, highlightthickness=0)
        self.buttonCode2.place(x=950, y=355, width=197, height=44.22)
        
    def easter_egg(self):
        pop_up = tk.Toplevel(bg="pink")
        pop_up.resizable(False, False)
        window_width = 550
        window_height = 325
        
        screen_width = pop_up.winfo_screenwidth()
        screen_height = pop_up.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        pop_up.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        list_code = {
            "chweyi"    : "one",
            "crabywan"  : "two",
            "yippiee"    : "three",
        }
        
        code = tk.Entry(pop_up)
        code.pack(pady=50)
        
        meme1 = tk.PhotoImage(file="image/meme1.png")
        meme1_label = tk.Label(self.frame_welcome, image=meme1, borderwidth=0, highlightthickness=0)
        meme1_label.image = meme1
        
        meme2 = tk.PhotoImage(file="image/meme2.png")
        meme2_label = tk.Label(self.frame_welcome, image=meme2, borderwidth=0, highlightthickness=0)
        meme2_label.image = meme2
        
        meme3 = tk.PhotoImage(file="image/meme3.png")
        meme3_label = tk.Label(self.frame_welcome, image=meme3, borderwidth=0, highlightthickness=0)
        meme3_label.image = meme3
        
        teks = tk.Label(pop_up, text="", bg="pink")
        teks.pack()
        
        def redeem_code():
            code_redeem = code.get()
            
            try:
                if list_code[code_redeem] == "one":
                    pop_up.destroy()
                    meme1_label.place(x=966, y=10, width=meme1.width(), height=meme1.height())
                if list_code[code_redeem] == "two":
                    pop_up.destroy()
                    meme2_label.place(x=80, y=430, width=meme2.width(), height=meme2.height())
                if list_code[code_redeem] == "three":
                    pop_up.destroy()
                    meme3_label.place(x=890, y=453, width=meme3.width(), height=meme3.height())
            except KeyError:
                teks.config(text="KODE REDEEM TIDAK VALID")
                    
            redeem.pack_forget()
            code.pack_forget()
        
        redeem = tk.Button(pop_up, text="Redeem", command=redeem_code)
        redeem.pack()
        
    def getCodew(self):
        messagebox.showinfo("yeyy", "Redeem Code : crabywan")
    
    def getCodeww(self):
        messagebox.showinfo("for u too", "Redeem Code : yippiee")
        
    def getCodewww(self):
        messagebox.showinfo("for u", "Redeem Code : chweyi")
        
    def about(self):
        self.frame_welcome.place_forget()
        
        #Frame About
        self.frame_about = tk.Frame(self.window, width=1100, height=650)
        self.frame_about.place(x=0, y=0)
        
        #background about
        self.bg_about = tk.PhotoImage(file="bg/bg_about.png")
        self.about_label = tk.Label(self.frame_about, image=self.bg_about, borderwidth=0, highlightthickness=0)
        self.about_label.place(x=0, y=0, width=self.bg_about.width(), height=self.bg_about.height())
        
        self.bubble1 = tk.PhotoImage(file="image/bubble1.png")
        self.bubble1_label = tk.Label(self.frame_about, image=self.bubble1, borderwidth=0, highlightthickness=0)
        self.bubble1_label.image = self.bubble1
        self.bubble1_label.place(x=250, y=125, width=self.bubble1.width(), height=self.bubble1.height())
        
        self.bubble1 = tk.PhotoImage(file="image/pillagy.png")
        self.bubble1_label = tk.Label(self.frame_about, image=self.bubble1, borderwidth=0, highlightthickness=0)
        self.bubble1_label.place(x=285, y=429, width=self.bubble1.width(), height=self.bubble1.height())
        
        about_text = ["MAU TAU BERBAGAI GAME SERU\nDALAM PROGRAM INI?", "Hmmmmmm??\n(Translate: Apaan tuuh??)", "MULAI DARI UAP INVADER, GAME PESAWAT YANG\nMENANTANG UNTUK MENEMBAK MUSUH-MUSUHNYA,\nFEEDING FRENZY, PERMAINAN SERU TENTANG\nIKAN YANG SALING MEMANGSA,", "Hmmmmmm Hmmm...\n(Translate: Eh eh tapii....)", "RASAKAN PENGALAMAN BERMAIN YANG\nMENYENANGKAN DAN MENANTANG\nDISETIAP GAMENYA,CUMA DI PROJEK\nBLOCKBUSTER UwU AJA LOCHH", "Hmmmmmmm Hmmmmm Hmmm\n(Translate: ada kejutam lain juga lohh)", "Hmmm? Hmmm hmmm\n(Translate: Mau tau? kadang awan\npunya banyak rahasia tauu...)"]
        
        self.text1 = tk.Label(self.frame_about, text=about_text.pop(0), font=("pixelify sans", 20), bg="#fefefe", anchor="center")
        self.text1.place(x=325, y=255, width=460, height=105)
        
        def next():
            if len(about_text) != 0:
                self.text1.config(text=about_text.pop(0), font=("pixelify sans", 15))
                
                if len(about_text) == 0:
                    self.next.config(text="> Exit <", command=back)
        
        def back():
            self.frame_about.place_forget()
            Welcome.__init__(self, self.window)
        
        self.next = tk.Button(text="Next >>", command=next, bg="#fefefe", borderwidth=0, highlightthickness=0, font=("pixelify sans", 12))
        self.next.place(x=730, y=325, width=60, height=35)
    
    def exit(self):
        self.window.destroy()