from nltk.corpus import stopwords,words as en_dict
import numpy as np
import numpy.linalg as LA
import csv, re, string, collections
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')
en_vocab = set(w.lower() for w in en_dict.words())
re_retweet = r'RT [@]?\w*:'
re_hashtag = r'#\w*'
re_hyperlink_s = r'http\S+'
re_hyperlink_2 = r'http \S+'
#re_hyperlink = r'http://[\/\w\.]*'
re_tweethandle = r'@\w*'

N = 83488 #size of raw-data
raw_data = None
training_data = None
test_data = None
vocab = set()

def get_raw_data(fpath):
	raw_data = []
	f = open(fpath,'r')
	#with open(fpath,'rt') as f:
		#reader = csv.reader(csvfile)
	for row in f.readlines():
		raw_data.append(row)
	#print raw_data[10:]
	return raw_data

def clean_data(data):
	cdata = []
	for row in data:	
		row1 = re.sub(re_hyperlink_s,'',row)
		nrow = re.sub(re_hyperlink_2,'',row1) #remove retweets)
		
			
		nrow = re.sub('http','',nrow)
		if 'http' in nrow:
			print nrow
		tokens = tokenizer.tokenize( #tokenize to remove punctuations
				re.sub(
					re_tweethandle, '', #remove twitter handles
						re.sub(
							re_hyperlink_s,'', #remove hyperlinks
							re.sub(
								re_hashtag, '', #remove hashtags
								re.sub(
									re_retweet,'',row #remove retweets
							)
						)	
						
					)
				)
			)
		#print tokens
		tokens = [word.lower() for word in tokens]
		
		for word in tokens: 
			#print word
			if word not in en_vocab: tokens.remove(word) #remove stopwords and non-english words
			else:
				if word not in vocab: vocab.add(word)
		cdata.append(" ".join(list(set(tokens)))) #membership test is faster in set
		
	return cdata

raw_data = clean_data(get_raw_data(r'tweets.txt'))
f = open("output.txt","w")
for i in raw_data:
	f.write(str(i))
	f.write("\n")
#training_data = raw_data[:int(0.8*N)]
#test_data = raw_data[int(0.8*N):]
#f = open("output.txt","r")
#for row in f.readlines():
	
