import os
import yaml
from datetime import datetime

import tweepy

from query import query

def _connect_to_twitter(config = os.path.expanduser("~/.twitter.yml")):
    conf = yaml.safe_load(open(config))
    auth = tweepy.OAuthHandler(conf['consumer_key'], conf['consumer_secret'])
    auth.set_access_token(conf['access_token'], conf['access_token_secret'])
    api = tweepy.API(auth)
    return api

def tweet(tweet_text_func):
    '''
    A decorator to make a function Tweet

    Parameters

    - `tweet_text_func` is a function that takes no parameters and returns a tweetable string

    For example::

        @tweet
        def total_deposits_this_week():
            # ...

        @tweet
        def not_an_interesting_tweet():
            return 'This tweet is not data-driven.'
    '''
    def tweet_func():
        api = _connect_to_twitter()
        tweet = tweet_text_func()
        print "Tweeting: %s" % tweet
        api.update_status(tweet)
        return tweet

    return tweet_func
