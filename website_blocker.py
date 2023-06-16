import tkinter as tk
import customtkinter as ctk
from PIL import Image
import ctypes
import sys

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

text_text1 = "Website Blocker"
text_text2 = "Enter your website:"
text_text3 = "www.example.com"

font_style_text1 = ("Bookman Old Style", 60, "bold")
font_style_text2 = ("Bookman Old Style", 30, "bold")
font_style_text3 = ("Bookman Old Style", 15)
font_style_website_enter = ("Bookman Old Style", 30)

standard_bg_color = "#242424"


class WebsiteBloker:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.geometry("600x300+0+0")
        self.window.resizable(0, 0)
        self.window.iconbitmap("./img/wsb_icon.ico")
        self.window.title("CLARSEN: Website Blocker")

        self.elements = self.create_elements()

    def create_elements(self):
        text1 = ctk.CTkLabel(self.window, text=text_text1,
                             font=font_style_text1)
        text1.pack()

        text2 = ctk.CTkLabel(self.window, text=text_text2,
                             font=font_style_text2)
        text2.place(relx=0.5, rely=0.5, x=-280, y=-50)

        text3 = ctk.CTkLabel(self.window, text=text_text3,
                             font=font_style_text3)
        text3.place(relx=0.5, rely=0.5, x=85, y=-70)

        website_enter = tk.Text(
            self.window, font=font_style_website_enter, height="1", width="20")
        website_enter.place(x=650, y=213)

        block_img = ctk.CTkImage(light_image=Image.open(
            "./img/block.png"), size=(100, 100))
        del_btn = ctk.CTkButton(self.window, text="", image=block_img, border_width=0,
                                width=1, bg_color=standard_bg_color, fg_color=standard_bg_color)
        del_btn.place(relx=0.5, rely=0.5, x=-230, y=1)

        unblock_img = ctk.CTkImage(light_image=Image.open(
            "./img/unblock.png"), size=(106, 106))
        del_btn = ctk.CTkButton(self.window, text="", image=unblock_img, border_width=0,
                                width=1, bg_color=standard_bg_color, fg_color=standard_bg_color)
        del_btn.place(relx=0.5, rely=0.5, x=100, y=-3)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    website_blocker = WebsiteBloker()
    website_blocker.run()
