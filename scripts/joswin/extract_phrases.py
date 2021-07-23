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
        :return:
        '''
        temp_list=[]
        for subtree in tr.subtrees():
            if subtree.label() in labels:
                tree_data = tree_travel(subtree,stopwords)
                temp_list+=[' '.join((e for e in list(tree_data)))]
        return temp_list

    def extract_phrase_treelistinput(self,ltrees,labels,stopwords=[]):
        '''
        :param ltrees: list of tree objects
        :param label: list of labels to extract phrase
        :param stopwords:
        :return:
        '''
        outlist = []
        for tr in ltrees:
            outlist.append(self.extract_phrase_treeinput(tr,labels,stopwords))
        return outlist

class PhraseRemover(object):
    """docstring for PhraseRemover"""
    def __init__(self):
        pass
    
    def remove_phrase_treeinput(self,tr,labels=None,stopwords=[]):
        '''
        :param tr: tree object
        