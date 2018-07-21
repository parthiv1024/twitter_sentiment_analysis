import tweepy
from textblob import TextBlob
import csv

# Step 1 - Authenticate
consumer_key = '5jFdQPbGtWkz31vXl0HQW4WPk'
consumer_secret = 'w8JFsbFsvl4K0hh5xXqssAu8S87wTe0SNEVq1r9RPfP0VUNmhS'

access_token = '971375935940386816-adY0Y2rwvfdMwh4YvbrZsDA0Jz3HFp1'
access_token_secret = 'mIZrzhggUbmuGCE656QCHOqY6PpnqO6Nf0ChwjjDTyHfR'

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
