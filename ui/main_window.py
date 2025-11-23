import tkinter as tk
from ui.components import TitleLabel
from core.controller import AppController

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My Tkinter App")
        self.geometry("400x300")

        self.controller = AppController()

        TitleLabel(self, "Hello Tkinter!").pack(pady=20)
