#!/usr/bin/python

import requests
import feedparser
import time
from subprocess import check_output
from tinydb import TinyDB, Query
import sys

#feed_name = 'TRIBUNE'
#url = 'http://chicagotribune.feedsportal.com/c/34253/f/622872/index.rss'

#feed_name = sys.argv[1]
#url = sys.argv[2]

#feed_name = 'TRIBUNE'
#url = 'http://chicagotribune.feedsportal.com/c/34253/f/622872/index.rss'

feed_name = ''
url='https://cryptocurrencynews.com/feed/'

api_price_url='https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD'

#test
print("testrun")

#db = '/var/www/radio/data/feeds.db'
feed_db = './feeds.db'

#json db
json_db = TinyDB('./json_db/db.json')

limit = 12 * 3600 * 1000

#
# function to get the current time
#
current_time_millis = lambda: int(round(time.time() * 1000))
current_timestamp = current_time_millis()

def post_is_in_db(title):
    with open(feed_db, 'r') as database:
        for line in database:
            if title in line:
                return True
    return False

##get USD price for BTC
r = requests.get(api_price_url)
print(r.text)


#read titles and insert if not there

#read in feed
feed = feedparser.parse(url)

#open output stream
f = open(feed_db, 'a')

for post in feed.entries:

    if not post_is_in_db(post.title):
        f.write(post.content + "|" + str(current_timestamp) + "\n")

f.close


#insert test for json db
json_db.insert({'int': 1, 'char': 'a'})