import tkinter as tk
from tkinter import ttk, messagebox

class Project:
    def __init__(self, window):
        #Frame Kiri
        self.frame_project_left = tk.Frame(window, bg="blue", width=550, height=650)
        self.frame_project_left.place(x=0, y=0)