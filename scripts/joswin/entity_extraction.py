
# from corenlp import StanfordCoreNLP
import nltk
from nltk.tag.stanford import StanfordNERTagger

def sent_tokenize_withnewline(text):
    '''default tokenizer do not consider new line as sentence delimiter.
     In our case, it makes sense to do so. '''
    sentences = [] 
    for para in text.split('\n'): 
        sentences.extend(nltk.sent_tokenize(par