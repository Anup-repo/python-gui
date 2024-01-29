from tkinter import *
from mydatabase import Database
from tkinter import messagebox
from myapi import API
import emoji


class NLP:
    def __init__(self):
        self.dbo = Database()
        self.api = API()

        self.root = Tk()
        self.root.title("NLP Application")
        self.root.geometry("500x600")
        self.root.configure(bg="#34495E")
        self.login_gui()
        self.root.mainloop()

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def header(self):
        header = Label(self.root, text="NLP Application")
        header.configure(font=("verdana", 24, "bold"), bg="#34495E", fg="white")
        header.pack(pady=(10, 10))

    def login_gui(self):
        self.clear()
        self.header()

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
            self.root, text="Register", height=1, width=10, command=self.register_gui
        )
        register.pack(pady=(10, 10))

    def register_gui(self):
        self.clear()
        self.header()

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

        if response == "Email already Exists":
            messagebox.showerror("Error", "Email already registered")
        elif response == "Please fill all fields":
            messagebox.showerror("Error", "It's mendatory to fill all fields")
        else:
            messagebox.showinfo("Success", "Registration successful, you can login now")

    def login(self):
        email = self.email.get()
        password = self.password.get()

        response = self.dbo.login(email, password)

        if response:
            messagebox.showinfo("Success", "Login successful")
            self.clear()
            self.home_gui()
        else:
            messagebox.showerror("Error", "Incorrect email/password.")

    def home_gui(self):
        self.clear()
        self.header()

        Label1 = Label(self.root, text="Sentiment Analysis")
        Label1.pack(pady=(10, 10))

        sentiment_btn = Button(
            self.root,
            text="Sentiment Analysis",
            height=4,
            width=30,
            command=self.sentiment_analysis,
        )
        sentiment_btn.pack(pady=(10, 10))

        Label2 = Label(self.root, text="Named Entity Recognition")
        Label2.pack(pady=(10, 10))

        ncr_btn = Button(
            self.root,
            text="Named Entity Recognition",
            height=4,
            width=30,
            command=self.ner_analysis,
        )
        ncr_btn.pack(pady=(10, 10))

        Label3 = Label(self.root, text="Abusive Content Classifier")
        Label3.pack(pady=(10, 10))

        emotion_btn = Button(
            self.root,
            text="Abusive Content Classifier",
            height=4,
            width=30,
            command=self.emotion_analysis,
        )
        emotion_btn.pack(pady=(10, 10))

        logout_btn = Button(self.root, text="Logout", command=self.login_gui)
        logout_btn.pack(pady=(10, 10))

    def sentiment_analysis(self):
        self.clear()
        self.header()

        heading2 = Label(self.root, text="Sentiment Analysis", bg="#34495E", fg="white")
        heading2.pack(pady=(10, 20))
        heading2.configure(font=("verdana", 20))

        label1 = Label(self.root, text="Enter the text")
        label1.pack(pady=(10, 10))

        self.sentiment_input = Entry(self.root, width=50)
        self.sentiment_input.pack(pady=(5, 10), ipady=4)

        sentiment_btn = Button(
            self.root, text="Analyze Sentiment", command=self.do_sentiment_analysis
        )
        sentiment_btn.pack(pady=(10, 10))

        self.sentiment_result = Label(self.root, text="", bg="#34495E", fg="white")
        self.sentiment_result.pack(pady=(10, 10))
        self.sentiment_result.configure(font=("verdana", 16))

        goback_btn = Button(self.root, text="Go Back", command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def do_sentiment_analysis(self):
        input = self.sentiment_input.get()
        result = self.api.sen_analysis(input)

        res = ""
        for i in result["sentiment"]:
            if i == "negative":
                res += (
                    emoji.emojize(":disappointed_face:")
                    + " "
                    + str(result["sentiment"][i])
                )
            if i == "neutral":
                res += (
                    emoji.emojize(":slightly_smiling_face:")
                    + " "
                    + str(result["sentiment"][i])
                )
            if i == "positive":
                res += (
                    emoji.emojize(":smiling_face_with_smiling_eyes:")
                    + " "
                    + str(result["sentiment"][i])
                )
        self.sentiment_result["text"] = res

    def ner_analysis(self):
        self.clear()
        self.header()

        heading2 = Label(
            self.root, text="Name Entity Recognition", bg="#34495E", fg="white"
        )
        heading2.pack(pady=(10, 20))
        heading2.configure(font=("verdana", 20))

        label1 = Label(self.root, text="Enter the text")
        label1.pack(pady=(10, 10))

        self.ner_input = Entry(self.root, width=50)
        self.ner_input.pack(pady=(5, 10), ipady=4)

        ner_btn = Button(self.root, text="Analyze NER", command=self.do_ner_analysis)
        ner_btn.pack(pady=(10, 10))

        self.ner_result = Label(self.root, text="", bg="#34495E", fg="white")
        self.ner_result.pack(pady=(10, 10))
        self.ner_result.configure(font=("verdana", 14))

        goback_btn = Button(self.root, text="Go Back", command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def do_ner_analysis(self):
        input = self.ner_input.get()
        result = self.api.n_analysis(input)

        res = ""
        for i in result["entities"]:
            for j in i:
                if j != "confidence_score":
                    res += str(j) + "->" + str(i[j]) + "\n"

        self.ner_result["text"] = res

    def emotion_analysis(self):
        self.clear()
        self.header()

        heading2 = Label(
            self.root, text="Abusive Content Classifier", bg="#34495E", fg="white"
        )
        heading2.pack(pady=(10, 20))
        heading2.configure(font=("verdana", 20))

        label1 = Label(self.root, text="Enter the text")
        label1.pack(pady=(10, 10))

        self.emotion_input = Entry(self.root, width=50)
        self.emotion_input.pack(pady=(5, 10), ipady=4)

        emotion_btn = Button(
            self.root,
            text="Abusive Content Classifier",
            command=self.do_emotion_analysis,
        )
        emotion_btn.pack(pady=(10, 10))

        self.emotion_result = Label(self.root, text="", bg="#34495E", fg="white")
        self.emotion_result.pack(pady=(10, 10))
        self.emotion_result.configure(font=("verdana", 14))

        goback_btn = Button(self.root, text="Go Back", command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def do_emotion_analysis(self):
        input = self.emotion_input.get()
        result = self.api.em_analysis(input)

        res = ""
        for i in result:
            res += str(i) + "->" + str(result[i]) + "\n"

        self.emotion_result["text"] = res


nlp = NLP()
