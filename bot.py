import tweepy
import time
import os
from os import environ

from tweepy.auth import OAuthHandler

def Main():
    print("Cigarette Spaghetti BOT started")

    CONSUMER_KEY = environ['CONSUMER_KEY']
    CONSUMER_SECRET = environ['CONSUMER_SECRET']
    ACCESS_KEY = environ['ACCESS_KEY']
    ACCESS_SECRET = environ['ACCESS_SECRET']

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit=True)

    query = 'cigarro OR audiovisual'
    max_tweets = 100

    results = __search_for_tweets(api,query,max_tweets)

    if results != None and len(results) > 0:
        for result in results:
            print("ID::::: ", result.id)
            print("TEXT::::: " + result.text)
            print("USER::::: ", result.user.name)
            time.sleep(2)
            __fav_tweet(api,result.id)
            __retweet(api, result.id)

            firstMessage = 'Olá, meus queridxs. Venho através deste bot, para apresentar pra vocês. Este curta experimental colaborativo que dirigimos e produzimos em meio a quarentena.'
            secondMessage = ' Espero que gostem e se possível, compartilhem. Vamos fortalecer o cenário do audiovisual independente e a cultura.\n\n https://youtu.be/qcRar3JnNOI'

            firstReply = __reply_tweet(api,firstMessage,result.id)

            if firstReply != None:
                secondReply = __reply_tweet(api,secondMessage,firstReply.id)

            print("Flow completed successfully")
            time.sleep(5)

    else:
        print("There is no tweets to reply")

def __search_for_tweets(api,query,max_tweets):
    try:
        print("trying to search tweets")
        return api.search(q=query, count=max_tweets,result_type="recent",locale="pt-br")
    except:
        err = sys.exc_info()[0]
        print(err)
        print("Could not search for new tweets")

def __fav_tweet(api,tweetId):
    try:
        print("trying to fav tweet")
        api.create_favorite(tweetId)
    except:
        err = sys.exc_info()[0]
        print(err)
        print("Could not fav this tweet")


def __reply_tweet(api,reply_message, id):
    try:
        print("trying to reply tweet")
        return api.update_status(reply_message, in_reply_to_status_id=id, auto_populate_reply_metadata=True)
    except:
        err = sys.exc_info()[0]
        print(err)
        print("Could not reply this tweet")

def __retweet(api,id):
    try:
        print("trying to rt tweet")
        api.retweet(id)
    except:
        err = sys.exc_info()[0]
        print(err)
        print("Could not retweet this tweet")

while True:
    Main()
    time.sleep(600)
