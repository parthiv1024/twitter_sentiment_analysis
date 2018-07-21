import tweepy
from textblob import TextBlob
import csv

# Step 1 - Authenticate
consumer_key = 'YOUR CONSUMER KEY'
consumer_secret = 'YOUR CONSUMER SECRET'

access_token = 'YOUR ACCESS TOKEN'
access_token_secret = 'YOUR ACCESS TOKEN SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Step 2 - Retrieve Tweets
public_tweets = api.search('Trump')

# Step 3 - Store them in a CSV file
for tweet in public_tweets:
	with open('tweets.csv', 'a') as dataset:
		wr = csv.writer(dataset, delimiter=',', quoting=csv.QUOTE_MINIMAL)
		wr.writerow([tweet.text, 'Positive' if TextBlob(tweet.text).sentiment.polarity >= 0.0 else 'Negative'])
