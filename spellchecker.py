
import pre_processor as PickleManager
from pre_processor import *

PickleManager.initialize()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def edits1(word):
   splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
   deletes    = [a + b[1:] for a, b in splits if b]
   transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
   replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
   inserts    = [a + c + b     for a, b in splits for c in alphabet]
   return set(deletes + transposes + replaces + inserts)

def known_edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in PickleManager.NWORDS)

def known(words): return set(w for w in words if w in PickleManager.NWORDS)

def correct(sentence,word):
    word = word.lower()
    candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
    result = tuple(candidates)[0]

    t = PickleManager.our_list_of_words

    if len(candidates)!=1:
        max = 0
        s = PickleManager.words(sentence)
        for k in candidates:
            uu = 0
            for w in s:
                if (w in t) & (k in t):
                  uu += PickleManager.a[PickleManager.all_words_dic[k]][PickleManager.all_words_dic[w]]
            print uu
            print '##'
            if uu > max:
                max = uu
                result = k
        if max == 0:
            for k in candidates:
                uu = PickleManager.count_our_words[k]
                if uu > max:
                    max = uu
                    result = k
                    print max
                    print result

    return result
    #return max(candidates, key=NWORDS.get)


def check_now(sentence):
    w = sentence.split(' ')
    for k in w:
        if k != ' ':
            t = correct(sentence,k)
            print t

PickleManager.initialize()
check_now('This is done through bnk process')
