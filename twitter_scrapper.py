#Imports
import tweepy
import configparser
import pandas as pd

#Read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['API_Key']
api_key_secret = config['twitter']['API_Key_Secret']

access_token = config['twitter']['Access_Token']
access_token_secret = config['twitter']['Access_Token_Secret']

#Authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Policitians id
ids = ['Statsmin','JakobEllemann','PiaOlsen', 'sofiecn', 'MaiVilladsen', 'SorenPape', 'MrMesserschmidt', 
        'PernilleVermund', 'AlexVanopslagh', 'SikandaSIDDIQUE', 'FranciskaRosenk', 'IsabellaArendt']

#Number of tweets
num_tweets = 100

#Get tweet

tweets = []

for id in range(len(ids)):
    for i in tweepy.Cursor(api.user_timeline, id=ids[id], tweet_mode='extended').items(num_tweets):
        tweets.append(i.full_text)

df = pd.DataFrame({'Tweets':tweets})
df.to_csv('tweet.csv', index=False)