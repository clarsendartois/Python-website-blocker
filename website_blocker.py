import tkinter as tk
import customtkinter as ctk
from PIL import Image
import ctypes
import sys

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class WebsiteBloker:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.geometry("600x300+0+0")
        self.window.resizable(0, 0)
        self.window.iconbitmap("./img/wsb_icon.ico")
        self.window.title("CLARSEN: Website Blocker")

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    website_blocker = WebsiteBloker()
    website_blocker.run()
