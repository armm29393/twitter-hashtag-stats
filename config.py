import json
import sys
import tweepy

f = open('config.json')
config = json.load(f)
f.close()

consumerKey = config['twitter']['api_key']
consumerSecret = config['twitter']['api_key_secret']
accessToken = config['twitter']['access_token']
accessTokenSecret = config['twitter']['access_token_secret']
bearerToken = config['twitter']['bearer_token']

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)
client = tweepy.Client(bearerToken)

def postTweet(status):
    try:
        tweet = api.update_status(status)
        return tweet
    except Exception as e:
        print(sys.exc_info())

def search(q, sd, ed):
    tw_all, tw_tweet, tw_retweet = 0, 0, 0
    tw_all = client.get_recent_tweets_count(q, start_time=sd, end_time=ed)
    tw_tweet = client.get_recent_tweets_count(f'{q} -is:retweet', start_time=sd, end_time=ed)
    tw_retweet = client.get_recent_tweets_count(f'{q} is:retweet', start_time=sd, end_time=ed)
    return tw_all.meta['total_tweet_count'], tw_tweet.meta['total_tweet_count'], tw_retweet.meta['total_tweet_count']
