import feather
import re
from collections import OrderedDict

ALL_TWEETS = feather.load_pickled()

KEYWORDS = []

def load_keywords():
    with open("keywords") as f:
        for line in f:
            KEYWORDS.append(line)

    for item in KEYWORDS:
        print item

def filter_tweets_with_keywords(tweets, keywords):
    keyword_match = []
    keyword_missing = []

    for tweet in tweets:
        if any(word in tweet.tweet_text.lower() for word in keywords):
            keyword_match.append(tweet)
        else:
            keyword_missing.append(tweet)

    return (keyword_match, keyword_missing)

def heat_mapping(tweets):
    heatmap = {}

    for tweet in tweets:
        tweet_word_set = set(remove_nonalphas(tweet.tweet_text.lower().split()))
        for item in tweet_word_set:
            if (str(item) in heatmap) == False and "http" not in str(item) and "amp" not in str(item):
                heatmap[str(item)] = 1
            elif str(item) != '' and "http" not in str(item) and "amp" not in str(item):
                heatmap[str(item)] += 1

    return heatmap

def keyword_heat_mapping(tweets):
    heatmap = {}

    for tweet in tweets:
        tweet_word_set = set(remove_nonalphas(tweet.tweet_text.lower().split()))
        keyword_set = set(KEYWORDS)

        commonalities = keyword_set & tweet_word_set

        for item in commonalities:
            if (str(item) in heatmap) == False:
                heatmap[str(item)] = 1
            else:
                heatmap[str(item)] += 1
    return heatmap

def remove_nonalphas(wordlist):
    alpha_only = []
    regex = re.compile('[^a-zA-Z]')

    for word in wordlist:
        encoded = word.encode('utf-8')
        alpha = regex.sub('', encoded)
        alpha_only.append(alpha)

    return alpha_only

def avg_favs_for(tweets):
    fav_sum = 0
    for tweet in tweets:
        fav_sum += tweet.fav_count

    return float(fav_sum / len(tweets))

def avg_rts_for(tweets):
    rt_sum = 0
    for tweet in tweets:
        rt_sum += tweet.rt_count

    return float(rt_sum / len(tweets))

def print_heat_frequencies(tweets=None, keywordFree=False):
    if tweets == None:
        heatmap = heat_mapping(ALL_TWEETS)
    elif keywordFree == True:
        heatmap = heat_mapping(tweets)
    else:
        heatmap = keyword_heat_mapping(tweets)

    heatmap_sorted = OrderedDict(sorted(heatmap.items(), key=lambda x: x[1], reverse=True))

    rank = 1
    f = open('word_frequencies.txt', 'w')
    for word, count in heatmap_sorted.items():
        # print "%10s %30s %14s" % (rank, word, count)
        f.write("%10s %30s %14s \n" % (rank, word, count))
        rank += 1
