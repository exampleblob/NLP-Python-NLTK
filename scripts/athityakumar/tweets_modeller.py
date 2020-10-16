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
import tweets_reader as tr

def clean(model,index) :
  index = index + 1
  dirty = ["+",".","*"]
  while model.find("0.") != -1 :
    prob = model[model.find("0."):model.find("0.")+6]
    model = string.replace(model,prob,"")
  for element in dirty :    
    model = string.replace(model,element,"")
  model = "Topic #"+str(index)+": "+model
  return model

all_tweets = tr.get_all_tweets()  
doc_set = []
count = 0
for index in all_tweets :
  doc_set.append(all_tweets[index]["clean_tweet"])
  count = count + 1

to