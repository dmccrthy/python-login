import tkinter as tk
from tkinter.messagebox import showinfo
import src.main as main

def errorprompt(error):
    showinfo(
        title='ERROR',
        message=f'ERROR: {error}'
    )

def success(type):
    showinfo(
        title="Success",
        message=f"{type} Successful!"
    )

def createwindow():
    win = tk.Frame(root, padx=250, pady=250)
    win.pack(fill="both", expand=True)

    ul = tk.Label(win, text="Email:", fg="blue",)
    ul.pack(fill="both", expand=True, side="left")
    name = tk.StringVar()
    ue = tk.Entry(win, textvariable=name)
    ue.pack(fill="both", expand=True, side="left", pady=50)

    pl = tk.Label(win, text="Password:", fg="blue",)
    pl.pack(fill="both", expand=True, side="left")
    password = tk.StringVar()
    pe = tk.Entry(win, textvariable=password, show="*")
    pe.pack(fill="both", expand=True, side="bottom")

    plc = tk.Label(win, text="Confirm Password:", fg="blue",)
    plc.pack(fill="both", expand=True, side="left")
    confpass = tk.StringVar()
    pec = tk.Entry(win, textvariable=confpass, show="*")
    pec.pack(fill="both", expand=True, side="bottom")

    def create():
        n = name.get()
        p = password.get()
        c = confpass.get()
        result = main.createacc(n, p, c)
        if result == 1:
            errorprompt("Passwords Don't Match")
        elif result == 2:
            errorprompt("Email Already in Use")
        elif result == 0:
            success("Account Creation")

    crtacc = tk.Button(win, text="Create Account", command=create)
    crtacc.pack(fill="both", expand=True, side="right")
    

def loginwindow():
    win = tk.Frame(root, padx=250, pady=250)
    win.pack(fill="both", expand=True)

    ul = tk.Label(win, text="Email:", fg="blue",)
    ul.pack(fill="both", expand=True, side="left")
    name = tk.StringVar()
    ue = tk.Entry(win, textvariable=name)
    ue.pack(fill="both", expand=True, side="left", pady=50)

    pl = tk.Label(win, text="Password:", fg="blue",)
    pl.pack(fill="both", expand=True, side="left")
    password = tk.StringVar()
    pe = tk.Entry(win, textvariable=password, show="*")
    pe.pack(fill="both", expand=True, side="bottom")

    def create():
        n = name.get()
        p = password.get()
        result = main.login(n, p)
        if result == 1:
            errorprompt("Incorrect Password")
        elif result == 2:
            errorprompt("Email not Associated with Account")
        elif result == 0:
            success("Login")

    crtacc = tk.Button(win, text="Create Account", command=create)
    crtacc.pack(fill="both", expand=True, side="right")

root = tk.Tk()
root.title("Python Account System")

start = tk.Frame(root, padx=250, pady=200)
start.pack(fill="both", expand=True)

text = tk.Label(start, text="Login\n or\n Create Account")
text.pack(fill="both", expand=True, side="top", pady=50)

def crt():
    start.destroy()
    createwindow()

crtacc = tk.Button(start, text="Create Account", command=crt)
crtacc.pack(fill="both", expand=True, side="left", padx=25)

def log():
    start.destroy()
    loginwindow()

login = tk.Button(start, text="Login", command=log)
login.pack(fill="both", expand=True, side="right")

root.mainloop()

