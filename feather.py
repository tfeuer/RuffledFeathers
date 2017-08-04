from twython import Twython
import Tweet
import pprint
import pickle

PRINTER = pprint.PrettyPrinter(indent=4)

APP_KEY = ""
APP_SECRET = ""

twitter = Twython(APP_KEY, APP_SECRET)

TWITTER_USER_ID = 25073877

ALL_TWEETS = []

def most_recent_tweet_id():
    timeline = twitter.get_user_timeline(user_id=TWITTER_USER_ID, count=1)
    tweet_id = timeline[0]["id"]
    return tweet_id

def get_next_max_tweet_id():
    last = len(ALL_TWEETS) - 1
    last_id = ALL_TWEETS[last].tweet_id
    return last_id

def append_next_set(max_tweet_id):
    user_timeline = twitter.get_user_timeline(user_id=TWITTER_USER_ID, count=200, max_id=max_tweet_id, trim_user=True, exclude_replies=True, include_rts=False)

    for item in user_timeline:
        tweet_id = item["id"]
        tweet_status = item["text"]
        tweet_date = item["created_at"]
        rt_count = item["retweet_count"]
        fav_count = item["favorite_count"]

        next_tweet = Tweet.Tweet(tweet_id, tweet_status, tweet_date, rt_count, fav_count)

        if (len(ALL_TWEETS) == 0) or (tweet_id != ALL_TWEETS[len(ALL_TWEETS) - 1].tweet_id):
            ALL_TWEETS.append(next_tweet)

def collect_all():
    first_tweet = most_recent_tweet_id()
    append_next_set(first_tweet)

    for x in range(0, 15):
        next_max = get_next_max_tweet_id()
        append_next_set(next_max)

def persist_pickled():
    pickle.dump(ALL_TWEETS, open("tweetdata.p", "wb"))
    print "Succesfully pickled tweet data"

def load_pickled():
    data_load = pickle.load(open("tweetdata.p", "rb"))
    print "Succesfully unpickled tweet data"
    return data_load
