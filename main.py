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

window.title("Twitter Desktop")
window.geometry(str(int(window.winfo_screenwidth()*0.7)) + "x" + str(int(window.winfo_screenheight()*0.7)))

tk.Label(window, text = "Log in", font = ("Arial", 80, 'bold')).grid(row = 0, column = 1)
tk.Label(window, text = "Enter your information to access your Twitter account", font = ("Arial", 20, 'bold')).grid(row = 1, column = 1)

tk.Label(window, text = "API Key:", font = ("Arial", 20, 'bold'), anchor="w").grid(row = 2, column = 0)
tk.Label(window, text = "API Secret Key:", font = ("Arial", 20, 'bold')).grid(row = 3, column = 0)
tk.Label(window, text = "Access Token:", font = ("Arial", 20, 'bold')).grid(row = 4, column = 0)
tk.Label(window, text = "Access Secret Token:", font = ("Arial", 20, 'bold')).grid(row = 5, column = 0)

window.mainloop()

