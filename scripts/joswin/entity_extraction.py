
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
        self.st = StanfordNERTagger('intent_class_models/stanford-jars/english.all.3class.distsim.crf.ser.gz' ,
            "intent_class_models/stanford-jars/stanford-ner.jar" )
        # self.st = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz' ,
        #     'stanford-ner.jar' )

    def tag_text_single(self,text):
        '''
        :param text:
        :return:
        '''
        # assert type(text) == str
        sents = self.st.tag(nltk.word_tokenize(text))
        return sents

    def identify_NER_tags_single(self,text_tag,tag_to_find):
        '''
        :param text_tag: Tagged text
        :param tag_to_find:
        :return:
       