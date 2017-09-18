import TwitterUser

donnie = TwitterUser.TwitterUser(25073877)

print donnie.most_recent_tweet().tweet_text
donnietweets = donnie.get_available_tweets()

print(len(donnietweets))
