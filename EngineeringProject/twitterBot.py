# !/usr/bin/env python
from __future__ import unicode_literals
from __future__ import division
from nltk.corpus import stopwords
import numpy as np

from math import *

from itertools import zip_longest
from numpy import dot
from numpy.linalg import linalg

import tweepy
from tweepy.streaming import StreamListener, json
from tweepy import OAuthHandler
from tweepy import Stream
from pymongo import MongoClient

L = 10
threshold1 = 0.50
threshold2 = 0.75
tweet_words = []
n = 0
track_words = ['4you', '2me', 'ABD']
follow_acc = ['1005498924']  # all username converted to user ids
auths = OAuthHandler("K2hS7zJsH7mUSzVuqoeooMKjw", "drHNLYHunQKMQchJrjXV5QCvP43AhRR4p5azXx471m4C9LqAe0")
auths.set_access_token("3908562977-JAVzr681Uiv0mxRInqk1jgS7rnK8OpeNN6oyYZw", "Ygv8LwLqygj40Aa4mC6zCLA5e6XoRIZVJEXiilJfrKS0k")
api = tweepy.API(auths)

class listener(StreamListener):

    def on_data(self, raw_data):
        #print (raw_data)

        global n
        try:
            json_load = json.loads(raw_data)
            tweet_text = json_load['text']
          #  coded = texts.encode('utf-8')
           # s = str(tweet_text)
           # print(s)
            #tweet_text = raw_data.lower().split('"text":"')[1].split('","source":"')[0].replace(",", "")
            screen_name = raw_data.lower().split('"screen_name":"')[1].split('","location"')[0].replace(",", "")
            tweet_cid = raw_data.split('"id":')[1].split('"id_str":')[0].replace(",", "")
            print(tweet_text)
            n = 0
            del tweet_words[:]

            for key in orderedkeys:
                  tweet_words.append(0)
                 # print(key)
                 # print(n)
                  TweetTokenization3.tweetToken(tweet_text, key)
                  #print(tweet_words)
                 # m += tweet_words[n]
                #  print(m)
                  n += 1

            print(tweet_words)
            #print(len(tweet_words))
            print(orderedvalues)
            #print(len(orderedvalues))
            #myvalues = np.asarray(values)
            #mytweet_words = np.asarray(tweet_words)
            #print(myvalues)
            #print(mytweet_words)
            print (cosine_similarity(tweet_words,orderedvalues))
            #cos_sim = dot(mytweet_words, myvalues.T) / linalg.norm(mytweet_words) / linalg.norm(myvalues)
            #
            # print(cos_sim)


            accs = ['twitter', 'twittersupport']  # banned account screen name goes in here
            words = ['hate', 'derp']  # banned words goes in here


            if not any(acc in screen_name.lower() for acc in accs):
                if not any(word in tweet_text.lower() for word in words):
                    # call what u want to do here
                    # tweet(tweet_cid)
                    # unfav(tweet_cid)
                    # retweet(tweet_cid)
                    # if (cos_sim > threshold2):
                       #  fav(tweet_cid)
                       #  retweet(tweet_cid)
                         print("favorites and retweet")
                    #     # syntax need to be fixed here
                         return True
                    #
                   #  if (cos_sim > threshold1):
                       #  retweet(tweet_cid)
                      #   print("retweet")
                    #     # syntax need to be fixed here
                       #  return True


        except Exception as e:
            print("tugba")
            print(str(e))  # prints the error msg, if u dont want it comment it out
            pass


    def on_error(self, status_code):
        try:
            print("error" + status_code)
        except Exception as e:
            print("tgb1")
            print(str(e))
            pass

def retweet(tweet_cid):
    try:
        api.retweet(tweet_cid)
    except Exception as e:
        print("tgb2")
        print(str(e))
        pass


def fav(tweet_cid):
    try:
        api.create_favorite(tweet_cid)
    except Exception as e:
        print("tgb3")
        print(str(e))
        pass


def unfav(tweet_cid):
    try:
        api.destroy_favorite(tweet_cid)
    except Exception as e:
        print("tgb4")
        print(str(e))
        pass

def tweet(myinput):
    try:
        api.update_status(status=myinput)
    except Exception as e:
        print("tgb5")
        print(str(e))
        pass


def square_rooted(x):
    return round(sqrt(sum([a * a for a in x])), 3)

def cosine_similarity(x, y):
    numerator = sum(a * b for a, b in zip(x, y))
    denominator = square_rooted(x) * square_rooted(y)
    return round(numerator / float(denominator), 3)

def only_letters(tested_string):
    for letter in tested_string:
        if not letter in "abcdefghjklmnopqrstuvwxyz":
            return False
    return True

class TweetTokenization():
    def tweetToken(tweet):
        import re

        emoticons_str = r"""
               (?:
                   [:=;] # Eyes
                   [oO\-]? # Nose (optional)
                   [D\)\]\(\]/\\OpP] # Mouth
               )"""

        regex_str = [
            emoticons_str,
            r'<[^>]+>',  # HTML tags
            r'(?:@[\w_]+)',  # @-mentions
            r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
            r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs

            r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
            r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
            r'(?:[\w_]+)',  # other words
            r'(?:\S)'  # anything else
        ]

        tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)
        emoticon_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)

        def tokenize(s):
            return tokens_re.findall(s)

        def preprocess(s, lowercase=False):
            tokens = tokenize(s)
            if lowercase:
                tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
            return tokens

        #tweet = 'RT @marcobonzanini: just an example! :D http://example.com #NLP'
        arry = preprocess(tweet)
       # print(arry)
        for twt in arry:
            twt = twt.lower()

          #  print(twt[0:5])
            if twt.startswith('#') or twt.startswith('@'):
                twt = twt[1:]
                if not twt in dictionary and re.search('[a-zA-Z]', twt) and twt not in stopwords.words('english') and twt!='rt' and not twt[0:5]=="https" :# problemliiii????????
                    #print(twt)
                    dictionary.append(twt)
            else:
                if not twt in dictionary and re.search('[a-zA-Z]', twt) and twt not in stopwords.words('english') and twt!='rt' and not twt[0:5]=="https"  :
                   # print(twt[:1])
                   # print(twt)
                    dictionary.append(twt)
class TweetTokenization2():
    def tweetToken(tweet,term):
        import re

        emoticons_str = r"""
               (?:
                   [:=;] # Eyes
                   [oO\-]? # Nose (optional)
                   [D\)\]\(\]/\\OpP] # Mouth
               )"""

        regex_str = [
            emoticons_str,
            r'<[^>]+>',  # HTML tags
            r'(?:@[\w_]+)',  # @-mentions
            r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
            r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs

            r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
            r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
            r'(?:[\w_]+)',  # other words
            r'(?:\S)'  # anything else
        ]

        tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)
        emoticon_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)

        def tokenize(s):
            return tokens_re.findall(s)

        def preprocess(s, lowercase=False):
            tokens = tokenize(s)
            if lowercase:
                tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
            return tokens

        #tweet = 'RT @marcobonzanini: just an example! :D http://example.com #NLP'
        arry = preprocess(tweet)
        #print(arry)
        for twt in arry:
            twt = twt.lower()
           # print(twt)
            if twt.startswith('#') or twt.startswith('@'):
                twt = twt[1:]
                if twt.lower() == term.lower():
                    matrix[i][j] = 1
            else:
                if twt.lower() == term.lower():
                   matrix[i][j] = 1



        # ['RT', '@marcobonzanini', ':', 'just', 'an', 'example', '!', ':D', 'http://example.com', '#NLP']
class TweetTokenization3():
    def tweetToken(tweet_text,keyterm):
        import re

        emoticons_str = r"""
               (?:
                   [:=;] # Eyes
                   [oO\-]? # Nose (optional)
                   [D\)\]\(\]/\\OpP] # Mouth
               )"""

        regex_str = [
            emoticons_str,
            r'<[^>]+>',  # HTML tags
            r'(?:@[\w_]+)',  # @-mentions
            r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
            r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs

            r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
            r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
            r'(?:[\w_]+)',  # other words
            r'(?:\S)'  # anything else
        ]

        tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)
        emoticon_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)

        def tokenize(s):
            return tokens_re.findall(s)

        def preprocess(s, lowercase=False):
            tokens = tokenize(s)
            if lowercase:
                tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
            return tokens

        #tweet = 'RT @marcobonzanini: just an example! :D http://example.com #NLP'
        arry = preprocess(tweet_text)
        #print(arry)
        for twt in arry:
            twt = twt.lower()
           # print(twt)
            if twt.startswith('#') or twt.startswith('@'):
                twt = twt[1:]
                if twt.lower() == keyterm.lower():
                    #print(twt)
                    #print(n)
                    tweet_words[n] = 1
            else:
                if twt.lower() == keyterm.lower():
                    #print(twt)
                    #print(n)
                    tweet_words[n] = 1



        # ['RT', '@marcobonzanini', ':', 'just', 'an', 'example', '!', ':D', 'http://example.com', '#NLP']


if __name__ == '__main__':
    client = MongoClient('localhost', 27017)
    db=client['BIGDATA']
    collection=db['BIGDaTA_Lab']
    cursor = collection.find()
    dictionary = []
    count=0
    for document in cursor:
        if count==5:
            break
        tweet=document.get('text')+"\n"
        #print(tweet)
        TweetTokenization.tweetToken(tweet.lower())
        count+=1
    #dictionary.sort()
    #print(dictionary)
    #print(len(dictionary))

    #print(track_words)
    matrix=[]
    # matrix.append([])
    # matrix[0].append('aa1')
    # matrix.append([])
    # matrix[0].append('aa2')
    # print(matrix[0][1])
    i = 0
    j = 0
    #k = 0
    cursor = collection.find()
   # print("---------------begin---------------")
    for document in cursor:
        if i==5:
           break
        matrix.append([])
        for term in dictionary:
            matrix[i].append(0)
           # print(matrix[i][j])
            #print("---------------begin---------------")
            tweet = document.get('text') + "\n"
           # print(tweet)
           # print(term)
            TweetTokenization2.tweetToken(tweet,term)
           # k += matrix[i][j]
           # print(k)
            j += 1
        j = 0
      #  k = 0
        i += 1
#    print("----------end-----------------------")
    #print(matrix)
    #print(len(matrix))

    dcentex = [sum(x) for x in zip(*matrix)]
    dcent= [x / len(matrix) for x in dcentex]
    dcentdic=dict(zip_longest(dictionary,dcent))
    #print(dcentdic)
    dordered = [ (v,k) for k,v in dcentdic.items() ]
    dordered.sort(reverse=True) # natively sort tuples by first element
    for v,k in dordered:
        print("%s: %f" % (k,v))

    firstLpairs = dordered[:L]
    print(firstLpairs)
    orderedkeys = [i[1] for i in dordered]
    orderedvalues=[i[0] for i in dordered]
    print(orderedkeys)
    print(orderedvalues)
    keys=[i[1] for i in firstLpairs]
    values=[i[0] for i in firstLpairs]
    print(keys)
    print(values)

    while True:
          try:
              twt = Stream(auths, listener())
              twt.filter(track=keys)# follow=follow_acc
          except (KeyboardInterrupt, EOFError, SystemExit):
              print("tgb6")
              break