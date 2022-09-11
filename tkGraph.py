import tkinter as tk
from tkinter import Widget, ttk
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

def launch(event) :
    print("rocket lanuched")

def log(event):
    print("logged")

root = tk.Tk()
root.title('Rocket Interface')

windowWidth = 600
windowHeight = 400

padLeft = int(root.winfo_screenwidth()/2 - windowWidth/2)
padTop = int(root.winfo_screenheight()/2 - windowHeight/2)

root.geometry(f'{windowWidth}x{windowHeight}+{padLeft}+{padTop}')
root.resizable(False, False)
root.attributes('-alpha', 0.9)
root.iconbitmap('C:/Users/piyus/Desktop/Python projects/graphics/icon.ico')

label = ttk.Label(root, text="Rocket Dashboard")
button = ttk.Button(root, text = 'Launch Rocket')
label.pack()
button.pack()

button.bind('<Button>', launch)
button.bind('<Button>', log, add='+')

root.mainloop()