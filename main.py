import tkinter as tk
from cgitb import text
from tkinter import ttk


import tweepy
from PIL import Image, ImageTk
global AK, AKS, AT, ATS, AS, authenticator, api

global file
fileName = "TwitterKeys"


class FrameLogin(tk.Frame):
    def __init__(self):
        super().__init__()
        self.logIn = tk.Label(self, text="Log in", font=("Arial", 80, 'bold'))
        self.logIn.pack(pady=100)
        self.description = tk.Label(self, text="Enter your information to access your Twitter account",
                                    font=("Arial", 20, 'bold'))
        self.description.pack(pady=30)


class FrameEntry(tk.Frame):

    def __init__(self):
        super().__init__()
        tk.Label(self, text="API Key:", font=("Arial", 20, 'bold'), anchor="w").grid(row=2, column=0,
                                                                                     sticky="e")
        tk.Label(self, text="API Secret Key:", font=("Arial", 20, 'bold')).grid(row=3, column=0, sticky="e")
        tk.Label(self, text="Access Token:", font=("Arial", 20, 'bold')).grid(row=4, column=0, sticky="e")
        tk.Label(self, text="Access Secret Token:", font=("Arial", 20, 'bold')).grid(row=5, column=0,
                                                                                     sticky="e")

        self.api_entry = tk.Entry(self, width=int(self.winfo_screenwidth() * 0.025))
        self.api_entry.grid(row=2, column=1, sticky="w")
        self.api_secret_entry = tk.Entry(self, width=int(self.winfo_screenwidth() * 0.025))
        self.api_secret_entry.grid(row=3, column=1, sticky="w")
        self.access_token = tk.Entry(self, width=int(self.winfo_screenwidth() * 0.025))
        self.access_token.grid(row=4, column=1, sticky="w")
        self.access_token_secret = tk.Entry(self, width=int(self.winfo_screenwidth() * 0.025))
        self.access_token_secret.grid(row=5, column=1, sticky="w")


class LogInWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Twitter Desktop Log In")
        self.geometry(str(int(self.winfo_screenwidth() * 0.7)) + "x" + str(int(self.winfo_screenheight() * 0.7)))

        self.topPart = FrameLogin()
        self.topPart.pack()
        self.bottomPart = FrameEntry()
        self.bottomPart.pack()
        self.submission = tk.Button(self, text="Submit", width=70, command=self.getKeysEntry)
        self.submission.pack(pady=40)
        self.fromFile = tk.Button(self, text="Get keys from the file", width=70, command=self.getKeys)
        self.fromFile.pack()
        self.incorrect = tk.Label(self, text="Incorrect information. Please try again", font=("Arial", 15, 'bold'),
                                  fg="red")

    def getKeysEntry(self):
        AK = self.bottomPart.api_entry.get()
        AS = self.bottomPart.api_secret_entry.get()
        AT = self.bottomPart.access_token.get()
        ATS = self.bottomPart.access_token_secret.get()

        self.Authenticate(AK, AS, AT, ATS)

    def Authenticate(self, AK, AS, AT, ATS):
        global api, client
        try:
            authenticator = tweepy.OAuthHandler(AK, AS)
            authenticator.set_access_token(AT, ATS)
            api = tweepy.API(authenticator, wait_on_rate_limit=True)
            api.mentions_timeline()
        except:
            self.incorrect.pack()
        else:
            authenticator = tweepy.OAuthHandler(AK, AS)
            authenticator.set_access_token(AT, ATS)
            api = tweepy.API(authenticator, wait_on_rate_limit=True)
            self.destroy()
            main = MainWindow()
            main.mainloop()

    def getKeys(self):
        all_keys = open(fileName, 'r').read().splitlines()
        AK = all_keys[0]
        AS = all_keys[1]
        AT = all_keys[2]
        ATS = all_keys[3]

        self.Authenticate(AK, AS, AT, ATS)


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Twitter Desktop")
        self.geometry(str(int(self.winfo_screenwidth())) + "x" + str(int(self.winfo_screenheight())))
        self.Headline = tk.Label(self, text="Use this Twitter Desktop application to:", font=("Arial", 35, 'bold'))
        self.Headline.pack(pady=40)

        self.tabControl = ttk.Notebook(self, width=int(self.winfo_screenwidth()*0.9), height=int(self.winfo_screenheight()*0.75))
        self.style = ttk.Style()
        self.style.theme_create("MyStyle", parent="alt", settings={
            "TNotebook.Tab": {"configure": {"padding": [30, 30]}, }})

        self.style.theme_use("MyStyle")


        self.home = tk.Frame(self.tabControl)
        self.tab1 = tk.Frame(self.tabControl)
        self.tab2 = tk.Frame(self.tabControl)
        self.tab3 = tk.Frame(self.tabControl)
        self.tab4 = tk.Frame(self.tabControl)
        self.tab5 = tk.Frame(self.tabControl)

        self.container = tk.Frame(self.tabControl)
        self.container.pack(fill="both", expand=True)
        self.tabControl.add(self.container, text='Home')
        self.canvas = tk.Canvas(self.container, width=200, height=400)
        self.scroll = tk.Scrollbar(self.container, command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.scroll.set, scrollregion=(0, 0, 10000, 20000))
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scroll.pack(side="right", fill="y")

        self.tabControl.add(self.tab1, text="Send a Tweet")
        self.tabControl.add(self.tab2, text="Respond to a Tweet")
        self.tabControl.add(self.tab3, text="Retrieve a Tweet under a specific hashtag")
        self.tabControl.add(self.tab4, text="Find locally trending subjects")
        self.tabControl.add(self.tab5, text="Upload a media file")



        public_tweets = api.home_timeline(count = 30000)
        sum = 0
        sum1 = 0

        for i, tweet in enumerate(public_tweets):
            #self.temp = tk.Label(self.canvas, text = tweet.text, font =("Arial", 20),width=500)
            #self.temp.pack()
            self.canvas.create_text(self.winfo_screenwidth()*0.45, (30 + 150 * i + sum), text=tweet.text, font="Times 20 bold")
            sum += 15 * (tweet.text.count("\n"))
            self.canvas.create_text(self.winfo_screenwidth()*0.45, (70 + 150 * i + sum), text=tweet.author.screen_name, font="Times 15 italic")
            print(sum)
            #self.temp1.pack()

        self.tabControl.pack(pady=40)
        self.tweetLabel = tk.Label(self.tab1, text = "What would you like to tweet about?", font=("Arial", 20, 'bold'))
        self.tweetLabel.grid(row=0, column=0, padx=20, pady=20)
        self.tweetEntry = tk.Entry(self.tab1, width=60)
        self.tweetEntry.grid(row=1, column=0, padx=20, pady=20)

        self.image = Image.open("pngtree-vector-right-arrow-icon-png-image_956430.png")
        self.image = self.image.resize((50, 50))
        self.photo = ImageTk.PhotoImage(self.image)
        self.go = tk.Button(self.tab1, image=self.photo, command=self.Sending)
        self.go.grid(row=0, column=1, rowspan=2)
    def Sending(self):
        api.update_status(self.tweetEntry.get())


if __name__ == "__main__":
    app = LogInWindow()
    app.mainloop()
