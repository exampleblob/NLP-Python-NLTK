
# from corenlp import StanfordCoreNLP
import nltk
from nltk.tag.stanford import StanfordNERTagger

def sent_tokenize_withnewline(text):
    '''default tokenizer do not consider new line as sentence delimiter.
     In our case, it makes sense to do so. '''
    sentences = [] 
    for para in text.split('\n'): 
        sentences.extend(nltk.sent_tokenize(para))
    return sentences 

class StanfordNERTaggerExtractor(object):
    """docstring for ClassName"""
    def __init__(self):
        self.st = StanfordNERTagger('intent_class_models/stanford-jars/english.all.3