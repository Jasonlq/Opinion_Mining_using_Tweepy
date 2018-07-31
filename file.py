import tweepy
from textblob import TextBlob
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth)

# Using the API object to get tweets from your timeline, and storing it in a variable called public_tweets
api = tweepy.API(auth)

# The Twitter user who we want to get tweets from
name = "realDonaldTrump"
# Number of tweets to pull
tweetCount = 20

# Calling the user_timeline function with our parameters
results = api.user_timeline(id=name, count=tweetCount)
c=1
# foreach through all tweets pulled
for tweet in results:
   wiki=TextBlob(tweet.text)

   # printing the text stored inside the tweet object
   print(c," ",tweet.text)
   c+=1
   print("\tSentiment",wiki.sentiment)
   print("\n")
