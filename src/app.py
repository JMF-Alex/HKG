import tkinter as tk

from src.config.settings import APP_GEOMETRY, APP_TITLE
from src.ui.main_window import MainWindow


def run() -> None:
    root = tk.Tk()
    root.title(APP_TITLE)
    root.geometry(APP_GEOMETRY)

    app = MainWindow(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()