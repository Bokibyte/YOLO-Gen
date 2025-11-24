import customtkinter
from PIL import Image

class queueControl(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        icoSize = 10
        
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
            width=icoSize, height=icoSize,
            command=self.buttonUp
        )
        self.buttonUp.grid(row=0, column=0, padx=10, pady=5, sticky="n")

        self.buttonDown = customtkinter.CTkButton(
            self, text='', image=downImage,
            fg_color="transparent", hover=False,
            border_width=2, border_color=("#000000", "#FFFFFF"),
            width=icoSize, height=icoSize,
            command=self.buttonDown
        )
        self.buttonDown.grid(row=2, column=0, padx=10, pady=5, sticky="s")
            
    def buttonUp(self):
        print("buttonUp pressed")

    def buttonDown(self):
        print("buttonDown pressed")

class modelDescription(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, 
                         fg_color="#414141",
                         corner_radius=10,
                         **kwargs)
        
        
        self.labelTitle = customtkinter.CTkLabel(self, text="AR Classification",
                                             font=("Consolas", 20, "bold"))
        self.labelTitle.grid(row=0, column=1, padx=5, sticky="w")

        self.labelDescription = customtkinter.CTkLabel(self, text="Fox jump i dunno next Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 
                                             font=("Arial", 15, "italic"),
                                             justify="left")
        self.labelDescription.grid(row=1, column=1, padx=8, sticky="w")
        
        self.bind("<Configure>",self._resizeWrap)
        
    def _resizeWrap(self, event):
        width = max(event.width - 40, 250)
        self.labelDescription.configure(wraplength=width)

class modelProgress(customtkinter.CTkFrame):
    def __init__(self, master, progressNow=2, progressFinal=100,**kwargs):
        super().__init__(master, **kwargs)
        
        self.progressFinal = progressFinal()
        self.progressNow = progressNow()
        
        self.progressMeter = customtkinter.CTkProgressBar(app, orientation="horizontal")
        self.progressMeter.grid(row=0, column=0)
        
        self.labelPercent = customtkinter.CTkLabel(self, text="0%")
        self.labelPercent.grid(row=0, column=1)
        
    def updateProgress(self, value):
        self.progressFinal = value
        ratio = self.progressNow / self.progressFinal
        ratio = max(0, min(ratio, 1))
        self.progressMeter.set(ratio)
        percent = int(ratio*100)
        self.labelPercent.configure(text=f"(percent)%")
        
class modelType(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.labelModel = customtkinter.CTkLabel(self, text="YOLO v8 Nano", font=("Arial", 10))
        self.labelModel.grid(row=1, column=2, padx=5)        
       
class utilitiesBox(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        buttonSize = 20
        buttonColorDark = "#000000"
        buttonColorLight = "#FFFFFF"
        
        self.buttonStartPause = customtkinter.CTkButton(
            self, text='S',
            fg_color="transparent", 
            hover=False,
            border_width=2, 
            border_color=(buttonColorDark, buttonColorLight),
            width=buttonSize, 
            height=buttonSize,
            command=self.buttonStartPause
        )
        self.buttonStartPause.grid(row=0, column=0, padx=5, pady=5, sticky="news")
        
        self.buttonReload = customtkinter.CTkButton(
            self, text='S',
            fg_color="transparent", 
            hover=False,
            border_width=2, 
            border_color=(buttonColorDark, buttonColorLight),
            width=buttonSize, 
            height=buttonSize,
            command=self.buttonReload
        )
        self.buttonConfig.grid(row=0, column=1, padx=5, pady=5, sticky="news")
        
        self.button = customtkinter.CTkButton(
            self, text='S',
            fg_color="transparent", 
            hover=False,
            border_width=2, 
            border_color=(buttonColorDark, buttonColorLight),
            width=buttonSize, 
            height=buttonSize,
            command=self.buttonConfig
        )
        self.buttonDelete.grid(row=0, column=2, padx=5, pady=5, sticky="news")
        
        self.button = customtkinter.CTkButton(
            self, text='S',
            fg_color="transparent", 
            hover=False,
            border_width=2, 
            border_color=(buttonColorDark, buttonColorLight),
            width=buttonSize, 
            height=buttonSize,
            command=self.buttonDelete
        )
        self.button.grid(row=0, column=3, padx=5, pady=5, sticky="news")
        
    def buttonStartPause(self):
        print("buttonStart pressed")
        
    def buttonReload(self):
        print("buttonReload pressed")
        
    def buttonConfig(self):
        print("buttonConfig pressed")
        
    def buttonDelete(self):
        print("buttonDelete pressed")

class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)   # <-- ini yang bikin melebar
        self.grid_columnconfigure(2, weight=0)
        
        self.queueFrame = queueControl(self)
        self.queueFrame.grid(row=0, column=0, padx=5, sticky="nws")
        
        self.descriptionFrame = modelDescription(self)
        self.descriptionFrame.grid(row=0, column=1, padx=5, sticky="news")
        
        self.descriptionFrame = modelType(self)
        self.descriptionFrame.grid(row=0, column=2, padx=5, sticky="nes")
        
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)


        self.my_frame = MyFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")



app = App()
app.mainloop()