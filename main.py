import tweepy
import tkinter as tk

global AK, AKS, AT, AS

file = "TwitterKeys"
def getKeys(fileName):
    all_keys = open(fileName, 'r').read().splitlines()
    api_key = all_keys[0]
    api_key_secret = all_keys[1]
    access_token = all_keys[2]
    access_secret = all_keys[3]
    return api_key, api_key_secret, access_token, access_secret
def getKeysEntry():
    pass

class Frame1(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

class LogInWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Twitter Desktop")
        self.geometry(str(int(self.winfo_screenwidth()*0.7)) + "x" + str(int(self.winfo_screenheight()*0.7)))
        self.__create_top_widgets()
        self.__create_bottom_widgets()
    def __create_top_widgets(self):
        self.logIn = tk.Label(self, text = "Log in", font = ("Arial", 80, 'bold'))
        self.logIn.pack(pady = 100)
        self.description = tk.Label(self, text = "Enter your information to access your Twitter account", font = ("Arial", 20, 'bold'))
        self.description.pack(pady=30)
        self.window = Frame1(self)
        self.window.pack()
    def __create_bottom_widgets(self):
        self.api = tk.Label(self, text = "API Key:", font = ("Arial", 20, 'bold'), anchor="w").grid(row = 2, column = 0, sticky = "e")
        self.apis = tk.Label(self, text = "API Secret Key:", font = ("Arial", 20, 'bold')).grid(row = 3, column = 0, sticky = "e")
        self.access = tk.Label(self, text = "Access Token:", font = ("Arial", 20, 'bold')).grid(row = 4, column = 0, sticky = "e")
        self.accesss = tk.Label(self, text = "Access Secret Token:", font = ("Arial", 20, 'bold')).grid(row = 5, column = 0, sticky = "e")

        self.api_entry = tk.Entry(self, width = int(self.winfo_screenwidth()*0.025))
        self.api_entry.grid(row = 2, column = 1, sticky = "w")
        self.api_secret_entry = tk.Entry(self, width = int(self.winfo_screenwidth()*0.025))
        self.api_secret_entry.grid(row = 3, column = 1, sticky = "w")
        self.access_token = tk.Entry(self, width = int(self.winfo_screenwidth()*0.025))
        self.access_token.grid(row = 4, column = 1, sticky = "w")
        self.access_token_secret = tk.Entry(self, width = int(self.winfo_screenwidth()*0.025))
        self.access_token_secret.grid(row = 5, column = 1, sticky = "w")
        self.window = Frame1(self)
        self.window.pack()
        self.tk.Button(self, text = "Submit", width = 70, command = getKeysEntry).pack(pady = 40)

if __name__=="__main__":
    app = LogInWindow()
    app.mainloop()

AK, AKS, AT, AS = getKeysEntry(file)

authenticator = tweepy.OAuthHandler(AK, AKS)
authenticator.set_access_token(AT,AS)

api = tweepy.API(authenticator, wait_on_rate_limit=True)



