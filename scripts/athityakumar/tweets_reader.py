__author__ = 'athityakumar'
#!/usr/bin/python
# -*- coding: utf-8 -*-

from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
import numpy as np
import MySQLdb
import string
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF
import tweets_database as td

def database_login() :
  return MySQLdb.connect(td.host(),td.user(),td.password(),td.database()) 
  
def database_read(table_name) :
  cur = database_login().cursor()
  cur.execute("SELECT * FROM "+table_name)
  return cur.fetchall()

def database_end() :
  database_login().close()

def remove_link(tweet) :
  while tweet.find("https://t.co/") != -1 :
    link = tweet[tweet.find("https://t.co/"):tweet.find("https://t.co/")+23]