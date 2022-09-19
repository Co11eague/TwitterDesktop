import tweepy
file = "TwitterKeys"
def getKeys(fileName):
    all_keys = open(fileName, 'r').read().splitlines()
    api_key = all_keys[0]
    api_key_secret = all_keys[1]
    bearer_token = all_keys[2]
    return api_key, api_key_secret, bearer_token

AK, AKS, BT = getKeys(file)