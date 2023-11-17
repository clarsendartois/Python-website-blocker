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
font_style_block = ("Bookman Old Style", 30, "bold")

standard_bg_color = "#242424"

host_path = "C:\Windows\System32\drivers\etc\hosts"
ip_address = "127.0.0.1"


class WebsiteBloker:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.geometry("600x300+0+0")
        self.window.resizable(0, 0)
        self.window.iconbitmap("./img/wsb_icon.ico")
        self.window.title("CLARSEN: Website Blocker")

        self.elements = self.create_elements()
        self.admin = self.is_admin()

    def is_admin(self):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def create_elements(self):
        global website_enter

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
        block_btn = ctk.CTkButton(self.window, text="", image=block_img, border_width=0,
                                  width=1, bg_color=standard_bg_color, fg_color=standard_bg_color, command=self.block_site)
        block_btn.place(relx=0.5, rely=0.5, x=-260, y=1)

        unblock_img = ctk.CTkImage(light_image=Image.open(
            "./img/unblock.png"), size=(106, 106))
        unblock_btn = ctk.CTkButton(self.window, text="", image=unblock_img, border_width=0,
                                    width=1, bg_color=standard_bg_color, fg_color=standard_bg_color, command=self.unblock_site)
        unblock_btn.place(relx=0.5, rely=0.5, x=130, y=-3)

    def block_site(self):
        if self.admin:
            website_lists = website_enter.get(1.0, "end")
            website = list(website_lists.split(","))
            with open(host_path, "r+") as host_file:
                flle_content = host_file.read()
                for web in website:
                    if web in flle_content:
                        ctk.CTkLabel(self.window, text="Already Blocked",
                                     font=font_style_block).place(x=165, y=200)
                        pass
                    else:
                        add_text = ip_address + " " + web
                        host_file.write(add_text)
                        ctk.CTkLabel(self.window, text="Blocked",
                                     font=font_style_block).place(x=240, y=150)
        else:
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, " ".join(sys.argv), None, 1)

    def unblock_site(self):
        if self.admin:
            data_file = open(host_path, "r")
            lines = data_file.readlines()
            data_file.close()
            write_file = open(host_path, "w")
            for line in lines:
                string = website_enter.get(1.0, "end")
                str(string)
                if string not in line:
                    write_file.write(line)
                ctk.CTkLabel(self.window, text=" Full Access!",
                             font=font_style_block).place(x=200, y=250)
            write_file.close()
        else:
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, " ".join(sys.argv), None, 1)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    website_blocker = WebsiteBloker()
    website_blocker.run()
