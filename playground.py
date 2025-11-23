import customtkinter
from PIL import Image

class queueControl(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        upImage = customtkinter.CTkImage(
            light_image=Image.open("app/assets/ico/upModelL.png"),
            dark_image=Image.open("app/assets/ico/upModelD.png"))
        
        downImage = customtkinter.CTkImage(
            light_image=Image.open("app/assets/ico/downModelL.png"),
            dark_image=Image.open("app/assets/ico/downModelD.png"))

        self.buttonUp = customtkinter.CTkButton(
            self, text='', image=upImage,
            fg_color="transparent", hover=False,
            border_width=2, border_color=("#000000", "#FFFFFF"),
            width=50, height=50,
            command=self.buttonUp
        )
        self.buttonUp.grid(row=0, column=0, padx=10, pady=5, sticky="n")

        self.buttonDown = customtkinter.CTkButton(
            self, text='', image=downImage,
            fg_color="transparent", hover=False,
            border_width=2, border_color=("#000000", "#FFFFFF"),
            width=50, height=50,
            command=self.buttonDown
        )
        self.buttonDown.grid(row=2, column=0, padx=10, pady=5, sticky="s")
            
    def buttonUp(self):
        print("buttonUp pressed")

    def buttonDown(self):
        print("buttonDown pressed")

class modelDescription(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.label1 = customtkinter.CTkLabel(self, text="Halo Dunia", font=("Consolas", 30))
        self.label1.grid(row=0, column=1, padx=5, sticky="w")

        self.label2 = customtkinter.CTkLabel(self, text="Fox jump i dunno next Lorem ipsum dolor sit amet, consectetur adipiscing elit.", font=("Arial", 20))
        self.label2.grid(row=1, column=1, padx=5)

        self.progressbar = customtkinter.CTkProgressBar(self, orientation="horizontal", height=18)
        self.progressbar.grid(row=2, column=1, pady=5, sticky="wns", columnspan=3)
    
class utilitiesBox(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.queueFrame = queueControl(self)
        self.queueFrame.grid(row=0, column=0, padx=5, sticky="news")
        
        self.descriptionFrame = modelDescription(self)
        self.descriptionFrame.grid(row=0, column=1, padx=5, sticky="news")
        



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)


        self.my_frame = MyFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")



app = App()
app.mainloop()