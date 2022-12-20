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

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

def postTweet(status):
    try:
        tweet = api.update_status(status)
        return tweet
    except Exception as e:
        print(sys.exc_info())

def search(q, sd, ed):
    tw_all, tw_tweet, tw_retweet = [], [], []
    for i, page in enumerate(tweepy.Cursor(api.search_tweets, q=q, count=100).pages(), 1):
        for tweet in page:
            un = tweet.user.screen_name
            id = tweet.id_str
            t = tweet.text
            c = tweet.created_at
            d = [un, t, c, f'https://twitter.com/{un}/status/{id}']
            if c < ed and c > sd:
                tw_all.append(d)
                if (not tweet.retweeted) and ('RT @' not in t):
                    tw_tweet.append(d)
                else:
                    tw_retweet.append(d)
    return tw_all, tw_tweet, tw_retweet
