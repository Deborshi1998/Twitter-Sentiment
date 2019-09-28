import tweepy
from textblob import TextBlob
from tweepy import OAuthHandler


ckey="xxxxxxxxxxxxx"
csecret="xxxxxxxxxx"
access_token="xxxxxxxxxxxxxxxxx"
access_token_secret="xxxxxxxxxxx"


auth=OAuthHandler(ckey,csecret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)
public_tweets=api.search("xxxxx")

for tweets in public_tweets:
    print(tweets.text)
    analysis=TextBlob(tweets.text)
    print(analysis.sentiment)
