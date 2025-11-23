import tkinter as tk
from ui.styles import FONT_TITLE

class TitleLabel(tk.Label):
    def __init__(self, parent, text):
        super().__init__(parent, text=text, font=FONT_TITLE)
