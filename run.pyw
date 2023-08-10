import tkinter as tk
import sys
import os

def resource_path(relative_path):
     if hasattr(sys, '_MEIPASS'):
         return os.path.join(sys._MEIPASS, relative_path)
     return os.path.join(os.path.abspath("."), relative_path)

root = tk.Tk()
root.title("Image_Viewer_v1.0.0")
root.resizable(False, False)
root.iconbitmap(default=resource_path("./logo.ico"))
root.configure(background="white")

root.focus_force()

text = "Image_Viewer_v1.0.0"
text_label = tk.Label(root, text=text, font=("Noto Sans JP", 15, "bold"), background="white")
text_label.grid(row=0, column=0, padx=5, pady=5)

img = tk.PhotoImage(file="./img.png")
img_label = tk.Label(root, image=img, background="white")
img_label.grid(row=1, column=0, padx=5, pady=5)

root.mainloop()
