import nltk
import re
import time
from nltk.corpus import wordnet as wn

contentArray = ['GOOGLE is a good company']


def processLanguage():
    for synset in wn.synsets('savings'):
        for lemma in synset.lemmas():
            print lemma.name()
    try:
        for item in contentArray:
            tokenized = nltk.word_tokenize(item)
            tagged = nltk.pos_tag(tokenized)
            print tagged
            namedEnt = nltk.ne_chunk(tagged)
            ##namedEnt.draw()
            print namedEnt


    except Exception, e:
        print str(e)


processLanguage()