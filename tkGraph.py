import tkinter as tk
from tkinter import Widget, ttk
from ctypes import windll
from tkinter.messagebox import showinfo
windll.shcore.SetProcessDpiAwareness(1)

#learning

def launch(event) :
    print("rocket lanuched")

def log(event):
    print("logged")

def download(event):
    showinfo(
        title='Information',
        message='Download button clicked!'
    )
    with open("download.txt", "r+") as file :
        content = file.read()
        if not content :
            file.write("1")
            return
        file.write(str(int(content)+1))

root = tk.Tk()
root.title('Rocket Interface 1.0')

windowWidth = 600
windowHeight = 400
padLeft = int(root.winfo_screenwidth()/2 - windowWidth/2)
padTop = int(root.winfo_screenheight()/2 - windowHeight/2)

root.geometry(f'{windowWidth}x{windowHeight}+{padLeft}+{padTop}')
root.resizable(False, False)
root.attributes('-alpha', 0.9)
root.iconbitmap('assets/icon.ico')

download_icon = tk.PhotoImage(file='./assets/download.png')
label = ttk.Label(
    root, 
    text="Rocket Dashboard", 
    background="white", 
    padding=10, 
    width=100,
    font=("Verdana", 14), foreground="black"
)
launch_button = ttk.Button(
    root, 
    text = 'Launch Rocket',
    padding=10
)
download_button = ttk.Button(
    root,
    image=download_icon,
    padding=5,
    text='Download',
    compound=tk.LEFT,
)

label.pack()
launch_button.pack(expand=True)
download_button.pack(expand=True)

launch_button.bind('<Button>', launch)
launch_button.bind('<Button>', log, add='+')
download_button.bind('<Button>', download)

root.mainloop()