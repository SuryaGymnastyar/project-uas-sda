from project_page import Project
from introduction_page import Introduction
from menu_page import Menu
from welcome_page import Welcome
from project_page import Project
import tkinter as tk

class Main(Project, Welcome, Introduction, Menu):
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
        self.frame_main = tk.Frame(self.window, width=1100, height=650)
        self.frame_main.pack(fill="both", expand=True)
    
    def Start(self):
        Welcome.__init__(self, self.window)
        
    def to_menu(self):
        self.frame_welcome.place_forget()
        Menu.__init__(self, self.window)
        
    def to_introduction(self):
        self.frame_welcome.place_forget()
        Introduction.__init__(self, self.window)
        
    def to_project(self):
        self.frame_perkenalan.place_forget()
        Project.__init__(self, self.window)
        
    def to_welcome(self):
        self.frame_perkenalan.place_forget()
        Welcome.__init__(self, self.window)
        
    def mainloop(self):
        self.window.mainloop()
        
    
if __name__ == "__main__":
    App = Main()
    App.Start()
    App.mainloop()