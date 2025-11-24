import customtkinter
from PIL import Image

class queueControl(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, 
                         fg_color="transparent",
                         **kwargs)
        
        icoSize = 50
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        upImage = customtkinter.CTkImage(
            light_image=Image.open("app/assets/ico/upModelL.png"),
            dark_image=Image.open("app/assets/ico/upModelD.png"))
        
        downImage = customtkinter.CTkImage(
            light_image=Image.open("app/assets/ico/downModelL.png"),
            dark_image=Image.open("app/assets/ico/downModelD.png"))

        self.buttonUp = customtkinter.CTkButton(
            self, text='', image=upImage,
            fg_color="#424242", hover=False,
            width=icoSize, height=icoSize,
            command=self.buttonUp
        )
        self.buttonUp.grid(row=0, column=0, pady=5, sticky="n")

        self.buttonDown = customtkinter.CTkButton(
            self, text='', image=downImage,
            fg_color="#424242", hover=False,
            width=icoSize, height=icoSize,
            command=self.buttonDown
        )
        self.buttonDown.grid(row=2, column=0, pady=5, sticky="s")
            
    def buttonUp(self):
        print("buttonUp pressed")

    def buttonDown(self):
        print("buttonDown pressed")

class modelDescription(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            fg_color="transparent",
            corner_radius=10,
            **kwargs
        )

        self.grid_columnconfigure(0, weight=1)

        self.labelTitle = customtkinter.CTkLabel(
            self,
            text="AR Classification",
            font=("Consolas", 20, "bold"),
            fg_color="#2C2C2C",
            corner_radius=10,
            height=30,
            anchor="w"
        )
        self.labelTitle.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        self.labelDescription = customtkinter.CTkLabel(
            self,
            text="Fox jump i dunno next Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            font=("Arial", 15, "italic"),
            justify="left",
            anchor="w"
        )
        self.labelDescription.grid(row=1, column=0, padx=8, sticky="w")
        self.last_width = None

        self.bind("<Configure>", self._resizeWrap)

    def _resizeWrap(self, event):
        if event.width == self.last_width:
            return
        self.last_width = event.width
        wrap_len = max(event.width - 40, 200)
        self.labelDescription.configure(wraplength=wrap_len)


class modelProgress(customtkinter.CTkFrame):
    def __init__(self, master, progressNow=2, progressFinal=100,**kwargs):
        super().__init__(master, 
                         fg_color="transparent", 
                         **kwargs)
        
        self.grid_columnconfigure(0, weight=1)
        
        self.progressFinal = progressFinal
        self.progressNow = progressNow
        
        self.progressMeter = customtkinter.CTkProgressBar(self, 
                                                          orientation="horizontal",
                                                          border_width=3,
                                                          height=20,
                                                          progress_color="#FFFFFF")
        self.progressMeter.grid(row=0, column=0, sticky="ew")
        
        self.labelPercent = customtkinter.CTkLabel(self, text="0%")
        self.labelPercent.grid(row=0, column=1, padx=5, pady=5)
        
    def updateProgress(self, value):
        self.progressFinal = value
        ratio = self.progressNow / self.progressFinal
        ratio = max(0, min(ratio, 1))
        self.progressMeter.set(ratio)
        percent = int(ratio*100)
        self.labelPercent.configure(text=f"(percent)%")
        
class modelType(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, 
                         fg_color="transparent",
                         **kwargs)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.labelModel = customtkinter.CTkLabel(self, 
                                                 text="YOLOv8 \nNano", 
                                                 font=("Arial", 20),
                                                 fg_color="#242424",
                                                 corner_radius=20)
        self.labelModel.grid(row=1, column=2, padx=5, sticky="news")        
    
class utilitiesBox(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, 
                         fg_color="transparent",
                         **kwargs)
        
        buttonSize = 80
        borderWidth = 2
        buttonColorDark = "#000000"
        buttonColorLight = "#FFFFFF"
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((1, 2, 3, 4), weight=1)

        self.modelInfo = modelType(self)
        self.modelInfo.grid(row=0, column=0, padx=5, pady=15, sticky="news")
        
        self.buttonStartPause = customtkinter.CTkButton(
            self, text='P',
            fg_color="transparent", 
            hover=False,
            border_width=borderWidth, 
            border_color=(buttonColorDark, buttonColorLight),
            width=buttonSize, 
            height=buttonSize,
            command=self.buttonStartPause
        )
        self.buttonStartPause.grid(row=0, column=1, padx=5, pady=5, sticky="news")
        
        self.buttonReload = customtkinter.CTkButton(
            self, text='R',
            fg_color="transparent", 
            hover=False,
            border_width=borderWidth, 
            border_color=(buttonColorDark, buttonColorLight),
            width=buttonSize, 
            height=buttonSize,
            command=self.buttonReload
        )
        self.buttonReload.grid(row=0, column=2, padx=5, pady=5, sticky="news")
        
        self.buttonConfig = customtkinter.CTkButton(
            self, text='E',
            fg_color="transparent", 
            hover=False,
            border_width=borderWidth, 
            border_color=(buttonColorDark, buttonColorLight),
            width=buttonSize, 
            height=buttonSize,
            command=self.buttonConfig
        )
        self.buttonConfig.grid(row=0, column=3, padx=5, pady=5, sticky="news")
        
        self.buttonDelete = customtkinter.CTkButton(
            self, text='Del',
            fg_color="transparent", 
            hover=False,
            border_width=borderWidth, 
            border_color="#FF5E00",
            width=buttonSize, 
            height=buttonSize,
            command=self.buttonDelete
        )
        self.buttonDelete.grid(row=0, column=4, padx=5, pady=5, sticky="news")
        
    def buttonStartPause(self):
        print("buttonStart pressed")
        
    def buttonReload(self):
        print("buttonReload pressed")
        
    def buttonConfig(self):
        print("buttonConfig pressed")
        
    def buttonDelete(self):
        print("buttonDelete pressed")


class mainBar1(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, 
                         fg_color="#424242",
                         **kwargs)
        
        self.grid_columnconfigure(0, weight=1)
        
        self.descriptionFrame = modelDescription(self)
        self.descriptionFrame.grid(row=0, column=0, padx=5, sticky="nswe", columnspan=1)
        
        self.utilitiesFrame = utilitiesBox(self)
        self.utilitiesFrame.grid(row=0, column=1, padx=5, sticky="news")

class mainBar2(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, 
                         fg_color="transparent",
                         **kwargs)
        
        self.grid_columnconfigure(0, weight=1)
        
        self.mainBarFrame = mainBar1(self)
        self.mainBarFrame.grid(row=0, column=0, padx=5, sticky="nesw", columnspan=3)
        
        self.progressFrame = modelProgress(self)
        self.progressFrame.grid(row=1, column=0, padx=5, sticky="nesw", columnspan=3)

class joinFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, 
                         fg_color="transparent",
                         **kwargs)
        
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)  
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure(0, weight=1)
        
        self.queueFrame = queueControl(self)
        self.queueFrame.grid(row=0, column=0, padx=5, pady=10, sticky="news")
        
        self.mainBarFrame = mainBar2(self)
        self.mainBarFrame.grid(row=0, column=1, padx=5, pady=10, sticky="news")

class modelListFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            fg_color="#2C2C2C",
            corner_radius=20,
            border_color="#969696",
            border_width=3,
            **kwargs
        )
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.joinFrame = joinFrame(self)
        self.joinFrame.grid(
            row=0, column=0,
            sticky="nsew",
            padx=8,
            pady=8
        )

        
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()


        self.grid_columnconfigure(0, weight=1)
        self.geometry("1000x160")

        self.my_frame = modelListFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")



app = App()
app.mainloop()