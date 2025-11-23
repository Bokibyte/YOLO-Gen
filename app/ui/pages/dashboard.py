import customtkinter as ctk

class myRadiokBox(ctk.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.title = title
        self.values = values
        self.radiobuttons = []
        self.variable = ctk.StringVar(value="")

        self.title = ctk.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        for i, value in enumerate(self.values):
            radiobutton = ctk.CTkRadioButton(self, text=value,  value=value, variable=self.variable)
            radiobutton.grid(row=i+1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.radiobuttons.append(radiobutton)

    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)

class myCheckBox(ctk.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.title = title
        self.values = values
        self.checkboxes = []

        self.title = ctk.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        for i, value in enumerate(self.values):
            checkbox = ctk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)

    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes

class Dashboard(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure((0, 1), weight=1)

        self.checkbox_frame_1 = myCheckBox(self, "Values", values=["value 1", "value 2", "value 3"])
        self.checkbox_frame_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

        self.checkbox_frame_2 = myCheckBox(self, "Values", values=["value 1", "value 2", "value 3"])
        self.checkbox_frame_2.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="nsew")

        self.button = ctk.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=2, column=0, padx=10, pady=10, sticky="nsew", columnspan=3)

        self.radiobutton_frame_1 = myRadiokBox(self, "ambatukam?", values=["yes a lot", "nigga wtf u mean"])
        self.radiobutton_frame_1.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        
        self.radiobutton_frame_2 = myRadiokBox(self, "ambatublow?", values=["yea", "sybau"])
        self.radiobutton_frame_2.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")
        
    def button_callback(self):
        print("button pressed")
        print("checkbox_frame_1:", self.checkbox_frame_1.get())
        print("checkbox_frame_2:", self.checkbox_frame_2.get())
        print("checkbox_frame_1:", self.radiobutton_frame_1.get())
        print("checkbox_frame_2:", self.radiobutton_frame_2.get())




