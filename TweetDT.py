from nltk.corpus import stopwords, words as en_dict
import numpy as np
import numpy.linalg as LA
import csv, re, string, collections
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')
en_vocab = set(w.lower() for w in en_dict.words())
re_retweet = r'RT [@]?\w*:'
re_hashtag = r'#\w*'
#re_hyperlink = r'http://[\/\w\.]*'
re_hyperlink = r'http\S+'
re_tweethandle = r'@\w*'

N = 83488  # size of raw-data
raw_data = None
training_data = None
test_data = None
vocab = set()


def get_raw_data(fpath):
    raw_data = []
    f = open(fpath)
    for line in f.readlines():
        raw_data.append(line)

    return raw_data


def clean_data(data):
    cdata = []
    for row in data:
        tokens = tokenizer.tokenize(  # tokenize to remove punctuations
            re.sub(
                re_tweethandle,'',  # remove twitter handles
                re.sub(
                    re_hyperlink,'',  # remove hyperlinks
                    re.sub(
                        re_hashtag,'',  # remove hashtags
                        re.sub(
                            re_retweet, '', row  # remove retweets
                        )
                    )
                )
            )
        )
        #print "len: ",len(tokens)
        print "t: ",tokens

        tokens = [word.lower() for word in tokens]
        for word in tokens:
            if word in stopwords.words('english') or word not in en_vocab:
                tokens.remove(word)  # remove stopwords and non-english words
            else:
                if word not in vocab: vocab.add(word)
        cdata.append((set(tokens)))  # membership test is faster in set
    return cdata


raw_data = clean_data(get_raw_data(r'tweets.txt'))
training_data = raw_data[:int(0.8 * N)]
test_data = raw_data[int(0.8 * N):]
