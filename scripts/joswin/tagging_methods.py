__author__ = 'joswin'
#!/usr/bin/python
# -*- coding: utf-8 -*-

import nltk

def get_postag_listinput(text_list):
        '''
        This method tries to tag a list of sentences. Doing it separately is slow. So, here this method
        combines all the sentences, and tag them together, then split the sentences back.
        text_list is a list of sentences
        '''
        list_split_code