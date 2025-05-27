from introduction_page import Introduction
import tkinter as tk
from tkinter import ttk, messagebox

class Welcome:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Aplikasi Skor")
        
        window_width = 1100
        window_height = 650
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        
        self.window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.window.resizable(False, False)
        
        #Frame Welcome
        self.frame_welcome = tk.Frame(self.window, width=1100, height=650)
        self.frame_welcome.pack(fill="both", expand=True)
        
        #Teks
        self.welcome = tk.Label(self.frame_welcome, text="WELCOME", font=("04b", 80))
        self.welcome.place(x=200, y=150)
        
        #Button
        self.button_start = tk.Button(self.frame_welcome, text="Start", font=("pixelify sans", 20), command=self.to_introduction)
        self.button_start.place(x=500, y=400)
        
    def to_introduction(self):
        self.frame_welcome.place_forget
        perkealan = Introduction(self.window)
        
    def mainloop(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = Welcome()
    app.mainloop()