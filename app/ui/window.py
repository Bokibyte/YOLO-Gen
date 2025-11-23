import customtkinter as ctk
from .pages.dashboard import Dashboard

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Dashboard")
        self.geometry("900x600")

        self.page = Dashboard(self)
        self.page.pack(fill="both", expand=True)
