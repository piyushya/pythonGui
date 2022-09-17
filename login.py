import tkinter as tk
import sqlite3 as database
from tkinter import Widget, ttk
from ctypes import windll
from tkinter.messagebox import showinfo
from werkzeug.security import generate_password_hash, check_password_hash
windll.shcore.SetProcessDpiAwareness(1)

class Login(tk.Tk) :
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
            text="Login Window",
            background="white",
            padding=10,
            width=100,
            font=("Verdana", 14),
            foreground="black"
        )
        self.label.pack()

        # store address and password
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        username_fr = ttk.Frame(self)
        password_fr = ttk.Frame(self)

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
        signUp_label = ttk.Label(
            self,
            text="New Registration?",
            foreground="blue"
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

        username_fr.pack(expand=True)
        password_fr.pack(expand=True)
        
        user_label.pack(expand=True, side=tk.LEFT)
        password_label.pack(expand=True, side=tk.LEFT)
        
        self.user_entry.pack(expand=True, padx=20)
        self.password_entry.pack(expand=True, padx=20)

        # login button
        login_button = ttk.Button(
            self,
            text="Login",
            command=self.login_clicked,
            padding=5
        )
        login_button.pack(pady=30)
        signUp_label.pack(expand=True)
        signUp_label.bind("<Button>", self.signUp_link)
    
    def signUp_link(self, event) :
        self.destroy()
        signUpWindow = SignUp()
        signUpWindow.mainloop()

    def resetFields(self):
        self.user_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')

    def login_clicked(self):
        #callback when the login button clicked
        if (not self.username.get()) or (not self.password.get()) :
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
        qry="SELECT * FROM user WHERE username=?"
        try:
            cur = db.cursor()
            cur.execute(qry, (self.username.get(),))
            db.commit()
            data = cur.fetchall()
            db.close()
            if data :
                if check_password_hash(data[0][3], self.password.get()) :
                    self.msg = "Login Succesfull"
                    return
                self.msg = "Wrong Password"
                return
            self.msg = "user not logged in try signing Up instead"
        except:
            self.msg = "database error"
            db.rollback()
        db.close()
        return

from signUp import SignUp