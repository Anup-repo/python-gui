from tkinter import *
from mydatabase import Database
from tkinter import messagebox
from myapi import API
from home import HomePage


class NLP:
    def __init__(self):
        self.dbo = Database()
        self.api = API()
        self.home = HomePage()

        self.root = Tk()
        self.root.title("NLP Application")
        self.root.geometry("500x500")
        self.root.configure(bg="black")
        self.login_gui()
        self.root.mainloop()

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def login_gui(self):
        self.clear()
        header = Label(self.root, text="NLP Application")
        header.configure(font=("arial", 24, "bold"), bg="black", fg="white")
        header.pack(pady=(10, 10))

        Label1 = Label(self.root, text="Enter your Email")
        Label1.pack(pady=(10, 10))
        self.email = Entry(self.root, width=30)
        self.email.pack(pady=(10, 10), ipady=5)

        Label2 = Label(self.root, text="Enter your Password")
        Label2.pack(pady=(10, 10))
        self.password = Entry(self.root, width=30, show="*")
        self.password.pack(pady=(10, 10), ipady=5)

        login = Button(
            self.root, text="Sign in", height=1, width=10, command=self.login
        )
        login.pack(pady=(10, 10))

        lablel3 = Label(self.root, text="New user?")
        lablel3.pack(pady=(10, 10))
        register = Button(
            self.root, text="Register", height=1, width=10, command=self.register
        )
        register.pack(pady=(10, 10))

    def register(self):
        self.clear()
        header = Label(self.root, text="NLP Application")
        header.configure(font=("arial", 24, "bold"), bg="black", fg="white")
        header.pack(pady=(10, 10))

        Label0 = Label(self.root, text="Enter your Name")
        Label0.pack(pady=(10, 10))
        self.name_input = Entry(self.root, width=30)
        self.name_input.pack(pady=(10, 10), ipady=5)

        Label1 = Label(self.root, text="Enter your Email")
        Label1.pack(pady=(10, 10))
        self.email_input = Entry(self.root, width=30)
        self.email_input.pack(pady=(10, 10), ipady=5)

        Label2 = Label(self.root, text="Enter your Password")
        Label2.pack(pady=(10, 10))
        self.password_input = Entry(self.root, width=30, show="*")
        self.password_input.pack(pady=(10, 10), ipady=5)

        login = Button(
            self.root, text="Sign up", height=1, width=10, command=self.registration
        )
        login.pack(pady=(10, 10))

        lablel3 = Label(self.root, text="Already a user?")
        lablel3.pack(pady=(10, 10))
        register = Button(
            self.root, text="Log in", height=1, width=10, command=self.login_gui
        )
        register.pack(pady=(10, 10))

    def registration(self):
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.regsiter(name, email, password)

        if response:
            messagebox.showinfo("Success", "Registration successful, you can login now")
        else:
            messagebox.showerror("Error", "Email already registered")

    def login(self):
        email = self.email.get()
        password = self.password.get()

        response = self.dbo.login(email, password)

        if response:
            messagebox.showinfo("Success", "Login successful")
            self.home.home_gui()
        else:
            messagebox.showerror("Error", "Incorrect email/password.")



nlp = NLP()
