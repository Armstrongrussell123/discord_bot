import feedparser
from random import randrange


def reddit_url(subreddit):
    BASE = 'http://www.reddit.com/'
    SUFFIX = '.rss'
    if subreddit is None:
        url = BASE + SUFFIX
    else:
        url = "{}r/{}/{}".format(BASE,subreddit,SUFFIX)
    return url

def get_rss(url):
    return feedparser.parse(url)

def get_entries(feed,start=0,end=5):
    ceil = len(feed.entries) - 1
    if end > ceil:
        end = ceil
    print("IM GETTING {}".format(end))
    for i in range(start,end):
        yield feed.entries[i]['link']

def get_random_entry(feed):
    index = randrange(0, len(feed.entries))
    print("IM GETTING {}".format(index))
    return feed.entries[index]['link']
