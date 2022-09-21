import tweepy
import tkinter as tk

global AK, AKS, AT, AS

file = "TwitterKeys"


def getkeys(fileName):
    all_keys = open(fileName, 'r').read().splitlines()
    api_key = all_keys[0]
    api_key_secret = all_keys[1]
    access_token = all_keys[2]
    access_secret = all_keys[3]
    return api_key, api_key_secret, access_token, access_secret


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
        self.title("Twitter Desktop")
        self.geometry(str(int(self.winfo_screenwidth() * 0.7)) + "x" + str(int(self.winfo_screenheight() * 0.7)))

        self.topPart = FrameLogin()
        self.topPart.pack()
        self.bottomPart = FrameEntry()
        self.bottomPart.pack()
        self.submission = tk.Button(self, text="Submit", width=70, command=self.getKeysEntry)
        self.submission.pack(pady=40)
        self.incorrect = tk.Label(self, text="Incorrect information. Please try again", font=("Arial", 15, 'bold'),
                                  fg="red")

    def getKeysEntry(self):
        AK = self.bottomPart.api_entry.get()
        AS = self.bottomPart.api_secret_entry.get()
        AT = self.bottomPart.access_token.get()
        ATS = self.bottomPart.access_token_secret.get()

        try:
            authenticator = tweepy.OAuthHandler(AK, AS)
            authenticator.set_access_token(AT, ATS)
            api = tweepy.API(authenticator, wait_on_rate_limit=True)

        except Exception:
            self.incorrect.pack()


if __name__ == "__main__":
    app = LogInWindow()
    app.mainloop()
