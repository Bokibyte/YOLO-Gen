import customtkinter as ctk

class Dashboard(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        ctk.CTkLabel(self, text="Dashboard").pack(pady=20)
