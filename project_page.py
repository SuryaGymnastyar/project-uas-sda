import tkinter as tk
from tkinter import ttk, messagebox

class Project:
    def __init__(self, window):
        self.window = window
        self.frame_project = tk.Frame(window, width=1100, height=650)
        self.frame_project.place(x=0, y=0)
        
        #Teks
        self.welcome = tk.Label(self.frame_project, text="PROJEK BROO", font=("04b", 80))
        self.welcome.place(x=0, y=150)