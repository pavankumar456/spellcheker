import re, collections
import numpy
import cPickle as pickle

def fileExist(fn):
    try:
        open(fn, "rb")
        return True
    except IOError as e:
        print "\n Error: ", e, "File named < ", fn, "> does not appear to exist. "
        return False


def extractPythonObjectFromPickleFile(filePath):
    file_o = open(filePath, "rb")
    py_obj = pickle.load(file_o)
    file_o.close()
    return py_obj


def dumpPythonObjectToPickleFile(pyObj, filePath):
    file_o = open(filePath, "wb")
    pickle.dump(pyObj, file_o)
    file_o.close()

STOP_WORDS = ['i',
 'me',
 'my',
 'myself',
 'no',
 'we',
 'our',
 'ours',
 'ourselves',
 'yo',
 'your',
 'yours',
 'yourself',
 'yourselves',
 'he',
 'him',
 'his',
 'himself',
 'she',
 'her',
 'hers',
 'herself',
 'it',
 'its',
 'itself',
 'they',
 'them',
 'their',
 'theirs',
 'themselves',
 'what',
 'which',
 'who',
 'whom',
 'this',
 'that',
 'these',
 'those',
 'am',
 'is',
 'are',
 'was',
 'were',
 'be',
 'been',
 'being',
 'have',
 'has',
 'had',
 'having',
 'do',
 'does',
 'did',
 'doing',
 'a',
 'an',
 'the',
 'and',
 'but',
 'if',
 'or',
 'because',
 'as',
 'until',
 'while',
 'of',
 'at',
 'by',
 'for',
 'with',
 'about',
 'against',
 'between',
 'into',
 'through',
 'during',
 'before',
 'after',
 'above',
 'below',
 'to',
 'from',
 'up',
 'down',
 'in',
 'out',
 'on',
 'off',
 'over',
 'under',
 'again',
 'further',
 'then',
 'once',
 'here',
 'there',
 'when',
 'where',
 'why',
 'how',
 'all',
 'any',
 'both',
 'each',
 'few',
 'more',
 'most',
 'other',
 'some',
 'such',
 'nor',
 'only',
 'own',
 'same',
 'so',
 'than',
 'too',
 'very',
 's',
 't',
 'can',
 'will',
 'just',
 'don',
 'should',
 'now',
 'd',
 'll',
 'm',
 'o',
 're',
 've',
 'y',
 'ain',
 'aren',
 'couldn',
 'didn',
 'doesn',
 'hadn',
 'hasn',
 'haven',
 'isn',
 'ma',
 'mightn',
 'mustn',
 'needn',
 'shan',
 'shouldn',
 'wasn',
 'weren',
 'won',
 'wouldn']


def words(text): return re.findall('[a-z]+', text.lower())

def train(features):
    model = {}
    for f in features:
        try:
            model[f] += 1
        except KeyError:
            model[f] = 1
    return model


# class PickleManager(object):
#     our_list_of_words = {}
#     all_words_dic = {}
#     NWORDS = {}
#     count_our_words = {}
#     a = numpy.zeros((len(all_words_dic) + 1, len(all_words_dic) + 1))
#
#     def __init__(self, arg):
#         super(PickleManager, self).__init__()
#         self.arg = arg
#
#     #ours
#     @classmethod
#     def give_count_our_words(features):
#         global STOP_WORDS
#         features = [word for word in features if word not in STOP_WORDS]
#         count_our_words = collections.defaultdict(lambda: 0)
#         for f in features:
#             count_our_words[f] += 1
#         return count_our_words
#
#     #ours
#     @classmethod
#     def give_all_words_dic(cls,features):
#         global STOP_WORDS
#         all_words_dic = {}
#         features = [word for word in features if word not in STOP_WORDS]
#         count = 1
#         for f in set(features):
#             all_words_dic[f] = count
#             count += 1
#         cls.a = numpy.zeros((len(all_words_dic) + 1, len(all_words_dic) + 1))
#         return all_words_dic
#
#
#     @classmethod
#     def create_array(cls):
#         a = numpy.zeros((len(cls.all_words_dic) + 1, len(cls.all_words_dic) + 1))
#         global sentences
#         sentence_list = sentences.split('.')
#         for sentence in sentence_list:
#             w = words(sentence)
#             w = [word for word in w if word not in STOP_WORDS]
#             for wr in w:
#                 for kr in w:
#                     a[cls.all_words_dic[wr]][cls.all_words_dic[kr]] += 1
#             for wr in w:
#                 a[cls.all_words_dic[wr]][cls.all_words_dic[wr]] -= 1
#         return a
#
#     @classmethod
#     def iii(cls):
#         cls.NWORDS = train(words(open('big.txt').read()))
#         cls.all_words_dic = cls.give_all_words_dic(words(open('big2.txt').read()))
#         cls.count_our_words = cls.give_count_our_words(words(open('big2.txt').read()))
#         cls.a = cls.create_array()
#         t = words(open('big2.txt').read())
#         t = [word for word in t if word not in STOP_WORDS]
#         cls.our_list_of_words = t
#
#     @classmethod
#     def initialize(cls):
#         if fileExist('NWORDS.pickle'):
#             cls.NWORDS = extractPythonObjectFromPickleFile('NWORDS.pickle')
#         else:
#             cls.NWORDS = train(words(open('big.txt').read()))
#             dumpPythonObjectToPickleFile(cls.NWORDS,'NWORDS.pickle')
#
#         if fileExist('all_words_dic.pickle'):
#             cls.all_words_dic = extractPythonObjectFromPickleFile('all_words_dic.pickle')
#         else:
#             cls.all_words_dic = cls.give_all_words_dic(words(open('big2.txt').read()))
#             dumpPythonObjectToPickleFile(cls.all_words_dic,'all_words_dic.pickle')
#
#         if fileExist('count.pickle'):
#             cls.count_our_words = extractPythonObjectFromPickleFile('count.pickle')
#         else:
#             cls.count_our_words = cls.give_count_our_words(words(open('big2.txt').read()))
#             dumpPythonObjectToPickleFile(cls.count_our_words,'count.pickle')
#
#         if fileExist('a.pickle'):
#             cls.a = extractPythonObjectFromPickleFile('a.pickle')
#         else:
#             cls.a = cls.create_array()
#             dumpPythonObjectToPickleFile(cls.a,'a.pickle')
#
#         if fileExist('our_list.pickle'):
#             cls.our_list_of_words = extractPythonObjectFromPickleFile('our_list.pickle')
#         else:
#             t = words(open('big2.txt').read())
#             t = [word for word in t if word not in STOP_WORDS]
#             cls.our_list_of_words = t
#             dumpPythonObjectToPickleFile(cls.our_list_of_words,'our_list.pickle')


our_list_of_words = {}
all_words_dic = {}
NWORDS = {}
count_our_words = {}
a = numpy.zeros((len(all_words_dic) + 1, len(all_words_dic) + 1))
sentences = open('big2.txt').read()

def give_count_our_words(features):
    global STOP_WORDS
    features = [word for word in features if word not in STOP_WORDS]
    count_our_words = {}
    for f in features:
        try:
            count_our_words[f] += 1
        except KeyError:
            count_our_words[f] = 0
    return count_our_words


def give_all_words_dic(features):
    global STOP_WORDS
    all_words_dic = {}
    features = [word for word in features if word not in STOP_WORDS]
    count = 1
    for f in set(features):
        all_words_dic[f] = count
        count += 1
    global a
    a = numpy.zeros((len(all_words_dic) + 1, len(all_words_dic) + 1))
    return all_words_dic


def create_array():
    global a
    global all_words_dic
    a = numpy.zeros((len(all_words_dic) + 1, len(all_words_dic) + 1))
    global sentences
    sentence_list = sentences.split('.')
    for sentence in sentence_list:
        w = words(sentence)
        w = [word for word in w if word not in STOP_WORDS]
        for wr in w:
            for kr in w:
                a[all_words_dic[wr]][all_words_dic[kr]] += 1
        for wr in w:
            a[all_words_dic[wr]][all_words_dic[wr]] -= 1
    return a


def initialize():
    global NWORDS
    global all_words_dic
    global count_our_words
    global a
    global our_list_of_words

    if fileExist('NWORDS.pickle'):
        NWORDS = extractPythonObjectFromPickleFile('NWORDS.pickle')
    else:
        NWORDS = train(words(open('big.txt').read()))
        dumpPythonObjectToPickleFile(NWORDS, 'NWORDS.pickle')

    if fileExist('all_words_dic.pickle'):
        all_words_dic = extractPythonObjectFromPickleFile('all_words_dic.pickle')
    else:
        all_words_dic = give_all_words_dic(words(open('big2.txt').read()))
        dumpPythonObjectToPickleFile(all_words_dic, 'all_words_dic.pickle')

    if fileExist('count.pickle'):
        count_our_words = extractPythonObjectFromPickleFile('count.pickle')
    else:
        count_our_words = give_count_our_words(words(open('big2.txt').read()))
        dumpPythonObjectToPickleFile(count_our_words, 'count.pickle')

    if fileExist('a.pickle'):
        a = extractPythonObjectFromPickleFile('a.pickle')
    else:
        a = create_array()
        dumpPythonObjectToPickleFile(a, 'a.pickle')

    if fileExist('our_list.pickle'):
        our_list_of_words = extractPythonObjectFromPickleFile('our_list.pickle')
    else:
        t = words(open('big2.txt').read())
        t = [word for word in t if word not in STOP_WORDS]
        our_list_of_words = t
        dumpPythonObjectToPickleFile(our_list_of_words, 'our_list.pickle')
