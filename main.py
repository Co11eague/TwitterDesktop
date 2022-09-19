import tweepy
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
