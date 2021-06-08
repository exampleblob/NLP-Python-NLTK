#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'joswin'

import nltk,re

def tree_travel(tree_obj,stopwords=[]):
        ''' Travel through a tree object
        :param tree_obj:
        :param stopwords:
        :return:
        '''
        tree_data = []
        for e in list(tree_obj):
            if isinstance(e,nltk.tree.Tree):
                # try:
                    tree_data.extend(tree_travel(e,stopwords))
                # except:
                #     continue
            else:
                if e[0] not in stopwords:
                    tree_data+=[e[0]]
        return tree_data

class PhraseExtractor(object):
    def __init__(self):
        pass

    def extract_phrase_treeinput(self,tr,labels,stopwords=[]):
        '''
        :param tr: tree object
        :param labels: list of label to extract phrase
        :param stopwords: stopwords list
    