import tkinter as tk
import sqlite3 as database
from tkinter import ttk
from tkinter.messagebox import showinfo
from ctypes import windll
from werkzeug.security import generate_password_hash
windll.shcore.SetProcessDpiAwareness(1)

class SignUp(tk.Tk) :
    def __init__(self) :
        super().__init__()
        self.msg = ""
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
        login_label = ttk.Label(
            self,
            text="Already Signed Up?",
            foreground="blue"
        )

        self.email_entry = ttk.Entry(
            email_fr,
            textvariable=self.email
        )
        self.user_entry = ttk.Entry(
            username_fr,
            textvariable=self.username
        )
        self.password_entry = ttk.Entry(
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

        self.email_entry.pack(expand=True, padx=20)
        self.user_entry.pack(expand=True, padx=20)
        self.password_entry.pack(expand=True, padx=20)

        self.email_entry.focus()
        # login button
        login_button = ttk.Button(
            self,
            text="Signup",
            command=self.signup_clicked,
            padding=5
        )
        login_button.pack(pady=30)
        login_label.pack(expand=True)
        login_label.bind("<Button>", self.login_link)

    def login_link(self, event) :
        self.destroy()
        loginWindow = Login()
        loginWindow.mainloop()

    def resetFields(self):
        self.user_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')

    def signup_clicked(self):
            #callback when the login button clicked
            if not self.username.get() or not self.email.get() or not self.password.get() :
                showinfo(
                    title='error',
                    message="Empty field"
                )
                return
            self.dbOps() #execute database operations
            showinfo(
                title='Information',
                message=self.msg
            )
            self.resetFields()

    def dbOps(self):
        # database opeartion start
        db = database.connect("data.db")
        hash = generate_password_hash(self.password.get(), "sha256")
        try :
            qry="INSERT INTO user (username, email, hash) VALUES (?,?,?);"
            cur=db.cursor()
            cur.execute(qry, (self.username.get(), self.email.get(), hash))
            db.commit()
            self.msg = f"SignUp Successfull for user : {self.username.get()}"
        except :
            db.rollback()
            self.msg = "Email or/and username is already taken try logging in instead"
        db.close()
        #database operation end

from login import Login