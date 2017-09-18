import feather

class TwitterUser:
    def __init__(self, user_id):
        self.user_id = user_id
        self.available_tweets = []

    def most_recent_tweet(self):
        return feather.most_recent_tweet_foruser(self.user_id)

    def get_available_tweets(self):
        if len(self.available_tweets) == 0:
            self.available_tweets = feather.available_tweets_foruser(self.user_id, get_retweets=True)

        return self.available_tweets

    # TODO: - def fetch_user_APICALL(): ?
    # for potentially some json user object given by twitter?
    # more data there possibly
