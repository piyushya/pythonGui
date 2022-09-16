import tkinter as tk
import sqlite3 as database
from tkinter import Widget, ttk
from ctypes import windll
from tkinter.messagebox import showinfo
from werkzeug.security import generate_password_hash, check_password_hash
windll.shcore.SetProcessDpiAwareness(1)

class signUp(tk.Tk) :
    def __init__(self) :
        super().__init__()
        self.title('User Interface 1.0')
        windowWidth = 600
        windowHeight = 400
        padLeft = int(self.winfo_screenwidth()/2 - windowWidth/2)
        padTop = int(self.winfo_screenheight()/2 - windowHeight/2)

        self.geometry(f'{windowWidth}x{windowHeight}+{padLeft}+{padTop}')
        self.resizable(False, False)
        self.attributes('-alpha', 0.9)
        self.iconbitmap('assets/icon.ico')

        self.label = ttk.Label(
            self, 
            text="SignUp Window",
            background="white",
            padding=10, 
            width=100,
            font=("Verdana", 14),
            foreground="black"
        )
        self.label.pack()

        # store email address and password
        self.email = tk.StringVar()
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        email_fr = ttk.Frame(self)
        username_fr = ttk.Frame(self)
        password_fr = ttk.Frame(self)

        email_label = ttk.Label(
            email_fr, 
            text="Email :", 
            font=("Georgia", 12)
        )
        user_label = ttk.Label(
            username_fr,
            text="Username :",
            font=("Georgia", 12)
        )
        password_label = ttk.Label(
            password_fr,
            text="Password :",
            font=("Georgia", 12)
        )

        email_entry = ttk.Entry(
            email_fr, 
            textvariable=self.email
        )
        user_entry = ttk.Entry(
            username_fr, 
            textvariable=self.username
        )
        password_entry = ttk.Entry(
            password_fr, 
            textvariable=self.password, 
            show="*"
        )

        email_fr.pack(expand=True)
        username_fr.pack(expand=True)
        password_fr.pack(expand=True)

        
        email_label.pack(side=tk.LEFT, expand=True)
        user_label.pack(expand=True, side=tk.LEFT)
        password_label.pack(expand=True, side=tk.LEFT)
        
        email_entry.pack(expand=True, padx=20)
        user_entry.pack(expand=True, padx=20)
        password_entry.pack(expand=True, padx=20)

        email_entry.focus()
        # login button
        login_button = ttk.Button(self, text="Signup", command=self.signup_clicked, padding=5)
        login_button.pack(pady=30)
    
    def signup_clicked(self):
            #callback when the login button clicked
            if (not self.username.get()) or (not self.email.get()) or (not self.password.get()) :
                showinfo(
                    title='error',
                    message="Empty field"
                )
                return
            self.dbOps()
            msg = f"Login Successfull for user : {self.username.get()}"
            showinfo(
                title='Information',
                message=msg
            )
    def dbOps(self):
        # database opeartion start
        try :
            conn = database.connect("data.db")
            curr = conn.cursor()
        except :
            print("Error in database")
        conn.close()
        #database operation end

window = signUp()
window.mainloop()