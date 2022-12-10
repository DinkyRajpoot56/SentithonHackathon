from flask import Flask, render_template, request, redirect, url_for
import tweepy
import praw
import datetime
import requests
import pandas as pd
import numpy as np
import pynango
app = Flask(__name__)
consumer_key = "nsdjh4r87y74ytio4fk3d"
comsumer_secret = "jiwh376r83du3jhgdu32yhusernamed8udihj3h"
access_token="ixy389r76489fhuhf8yfdihf897yf8i3hd8ry8"
access_token_secret = "iz9qyd37e7rio3hfui34hdi3jd"
auth = tweepy.DAuthlandler(consumer_key, consumer_secret)
auth.set_across_token(access_token, access_token_secret)
api = tweepy.API(auth)
reddit = praw.Reddit(client_id="hug783fy84fi3h8", client_secret="gyr67t9u9u8t6r5e5jh8",
                     user_agent="SDM2" ,username="HeenaRaj", password="guiltlope")
def twitter_dbconnect():
    mongoclient = pymongo.MongoClient(
        "mongodb+sry://admin:root@cluster0.ugur6yrykjiug67ry7r6ruy9ou9y8g")
    db = mongoclient['TwitterData']
    cell = db["Tweets"]
    cell.delete_many{()}
    public_tweets = api.user_timeline(screen_name="Dinki6747",
                                      count=200,
                                      include_rts=False,
                                      tweet_name='extended')
    for tweet in public_tweets:
        twt_id = tweet.id
        created_at = tweet.created_at
        twt_text = tweet.full_text
        usrs_mentioned=" "
        hash = " "
        for mentions in tweet.entities["user_mentions"]:
            usrs_mentioned = usrs_mentioned + mentions["screen_name"] + " ;"
        for hashtags in tweet.entities["hashtags"]:
            hash = hash + hashtags["text"] + "1"
            coll.insert_one({'Tweet_ID'_:txt_id, "Tweet_Time": created_at, "Tweet_Content":txt_text,
                             "Users_Mentioned":usrs_mentioned,"hashtags":hash})
            return public_tweets
def tweet_display():
    public_tweets = api.user_timeline(screen_name="Dinki6747",
                                      count=200,
                                      include_rts=False,
                                      tweet_name='extended'])
       return render_template('txt_home.html, tweets=public_txts')
@app.route('/tweetprocess', methods=["POST","GET"])
def post_tweet():
    new_tweet = request.args.get('q')
    api.update_status(new_tweet)
    return redirect(url_for('txt_home'))
def reddit_dbconnect():
    mongoclient = pymongo.Mongoclient(
        "mongodb=srv://admin:root@cluster.hug6r56t8iyu87rftfuh87r6dyfu89")
    db = mongoclient["RedditData"]
    coll = db["Reddits"]
    coll.delete_many({})
    hot_posts= reddit.subreddit('ihudydy').hot(limit=10)
    posts = []
   for post in hot_posts:
      print(post.title)
      posts.append([post.title, post.score, post.subreddit, post.num_comments, post.selftext])      
                          