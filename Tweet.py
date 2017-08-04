class Tweet:

    def __init__(self, tweet_id, tweet_text, tweet_date, rt_count, fav_count):
        self.tweet_id = tweet_id
        self.tweet_text = tweet_text
        self.tweet_date = tweet_date
        self.rt_count = rt_count
        self.fav_count = fav_count

    def tweeted_after_inauguration(self):
        date = self.tweet_date.encode('utf-8').split()
        month = date[1]
        day = date[2]
        year = date[5]

        if year == "2016":
            return False

        if year == "2017" and month != "Jan":
            return True

        if int(day) < 20:
            return False

        return True
