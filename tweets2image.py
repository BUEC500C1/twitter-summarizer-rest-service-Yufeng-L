# Get tweets and then insert into images
import os
import tweepy
import re
import configparser
from PIL import Image, ImageDraw, ImageFont

# insert your key
# consumer_key = ''
# consumer_secret = ''
# access_token = ''
# access_token_secret = ''
config = configparser.ConfigParser()
config.read("keys")

consumer_key = config.get('auth', 'consumer_key').strip()
consumer_secret = config.get('auth', 'consumer_secret').strip()
access_token = config.get('auth', 'access_token').strip()
access_token_secret = config.get('auth', 'access_token_secret').strip()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)   
api = tweepy.API(auth)

#Get Tweets based on keywords
def getTweets(keyword):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    # Default Count = 20
    search_results = api.user_timeline(keyword)
    # Background Image for insert
    count = 0
    Ignore = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    # parentdir = os.getcwd()
    # directory = keyword
    # path = os.path.join(parentdir,directory)
    # os.mkdir(path)
    print("Start Inserting")
    for tweet in search_results:
        gap = '\n'
        tweet_list = list(tweet.text)
        list_num = 0
        for i in range(len(tweet_list)):
	        if (i % 50) == 0:
		        tweet_list.insert(i,gap)
        tweet.text = ''.join(tweet_list)
        image = Image.open('background.png')
        count += 1
        fnt = ImageFont.truetype('Arial.ttf', 50)
        draw = ImageDraw.Draw(image)
        draw.text((100,200), tweet.text, font=fnt, fill= "black")
        filename = "tweets/img" + keyword + str(count) + ".png"
        image.save(filename)