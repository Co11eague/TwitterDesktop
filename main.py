import tweepy
import tkinter as tk


file = "TwitterKeys"
def getKeys(fileName):
    all_keys = open(fileName, 'r').read().splitlines()
    api_key = all_keys[0]
    api_key_secret = all_keys[1]
    access_token = all_keys[2]
    access_secret = all_keys[3]
    return api_key, api_key_secret, access_token, access_secret

AK, AKS, AT, AS = getKeys(file)

authenticator = tweepy.OAuthHandler(AK, AKS)
authenticator.set_access_token(AT,AS)

api = tweepy.API(authenticator, wait_on_rate_limit=True)

window = tk.Tk()
top_frame = tk.Frame(window)
top_frame.pack()

bottom_frame = tk.Frame(window)
bottom_frame.pack()

window.title("Twitter Desktop")
window.geometry(str(int(window.winfo_screenwidth()*0.7)) + "x" + str(int(window.winfo_screenheight()*0.7)))

tk.Label(top_frame, text = "Log in", font = ("Arial", 80, 'bold')).pack(pady = 100)
tk.Label(top_frame, text = "Enter your information to access your Twitter account", font = ("Arial", 20, 'bold')).pack(pady = 30)

tk.Label(bottom_frame, text = "API Key:", font = ("Arial", 20, 'bold'), anchor="w").grid(row = 2, column = 0, sticky = "e")
tk.Label(bottom_frame, text = "API Secret Key:", font = ("Arial", 20, 'bold')).grid(row = 3, column = 0, sticky = "e")
tk.Label(bottom_frame, text = "Access Token:", font = ("Arial", 20, 'bold')).grid(row = 4, column = 0, sticky = "e")
tk.Label(bottom_frame, text = "Access Secret Token:", font = ("Arial", 20, 'bold')).grid(row = 5, column = 0, sticky = "e")

api_entry = tk.Entry(bottom_frame, width = int(window.winfo_screenwidth()*0.025))
api_entry.grid(row = 2, column = 1, sticky = "w")
api_secret_entry = tk.Entry(bottom_frame, width = int(window.winfo_screenwidth()*0.025))
api_secret_entry.grid(row = 3, column = 1, sticky = "w")
access_token = tk.Entry(bottom_frame, width = int(window.winfo_screenwidth()*0.025))
access_token.grid(row = 4, column = 1, sticky = "w")
access_token_secret = tk.Entry(bottom_frame, width = int(window.winfo_screenwidth()*0.025))
access_token_secret.grid(row = 5, column = 1, sticky = "w")

tk.Button(window, text = "Submit", width = 70).pack(pady = 40)


window.mainloop()

