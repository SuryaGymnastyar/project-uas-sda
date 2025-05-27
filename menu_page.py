from project_page import Project
import tkinter as tk
from tkinter import ttk, messagebox

class Menu:
    def __init__(self, window):
        self.window = window
        self.frame_menu = tk.Frame(window, width=1100, height=650)
        self.frame_menu.place(x=0, y=0)
        
        #Teks
        self.welcome = tk.Label(self.frame_menu, text="MENU", font=("04b", 80))
        self.welcome.place(x=350, y=150)
        
        #Button
        self.button_start = tk.Button(self.frame_menu, text="Go To Project", font=("pixelify sans", 20), command=self.to_project)
        self.button_start.place(x=450, y=400)
        
    def to_project(self):
        self.frame_menu.place_forget
        project = Project(self.window)