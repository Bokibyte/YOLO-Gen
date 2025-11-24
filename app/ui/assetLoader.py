from PIL import Image
import customtkinter as ctk

class assetLoader:
    _paths = {
        "arrow-repeat": ("app/assets/ico/arrow-repeat.ico",""),
        "gear": ("app/assets/ico/gear.ico", ""),
        "pause": ("app/assets/ico/pause.ico", ""),
        "play": ("app/assets/ico/play.ico", ""),
        "trash": ("app/assets/ico/trash.ico", ""),
    }
    
    _pil_cache = {}
    
    @classmethod
    def _get_pil(cls name):
        if name not in cls._pil_cahce:
            light, dark = cls._paths[name]
            cls._pil_cahce[name] = (
                Image.open(light),
                Image.open(dark)
            )
        return cls._pil_cache[name]
    
    
        