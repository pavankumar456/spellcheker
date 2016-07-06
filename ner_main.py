import nltk

s = 'IMIMOBILE is a great company'
company = ['company','organisation']
location = ['village','city','municipality','corporation']
stoplist = {}

def makearray():
    for i in company:
        stoplist[i] = 'Organisation'
    for i in location:
        stoplist[i] = 'GPE'

def processstatement():
    tokens = nltk.word_tokenize(s)
    pos_tag = nltk.pos_tag(tokens)
    req_tokens = []
    print pos_tag
    for tag in pos_tag:
        if tag[1].startswith('N'):
            req_tokens.append(tag)
    for tag in req_tokens:
        w = tag[0].lower()

        w = tag[0].upper()

    print req_tokens


processstatement()
