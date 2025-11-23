def center_window(app):
    app.update_idletasks()
    w = app.winfo_width()
    h = app.winfo_height()
    x = (app.winfo_screenwidth() - w) // 2
    y = (app.winfo_screenheight() - h) // 2
    app.geometry(f"{w}x{h}+{x}+{y}")
