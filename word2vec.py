import neurolab as nl
import csv
import numpy as np
import scipy as sp
from nltk.corpus import stopwords
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfTransformer
from collections import Counter
from stop_words import get_stop_words
import enchant
import re
import nltk.data
from bs4 import BeautifulSoup

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
tempStr=""
with open('new_corpus.txt', 'r') as f:
	tempStr=f.read()
    
        
listOfWords = []
def review_to_sentences( review, tokenizer, remove_stopwords=False ):
    # Function to split a review into parsed sentences. Returns a 
    # list of sentences, where each sentence is a list of words
    #
    # 1. Use the NLTK tokenizer to split the paragraph into sentences
    #print review
    raw_sentences = tokenizer.tokenize(review.strip())
    #
    # 2. Loop over each sentence
    sentences = []
    for raw_sentence in raw_sentences:
        # If a sentence is empty, skip it
        if len(raw_sentence) > 0:
            # Otherwise, call review_to_wordlist to get a list of words
            sentences.append( review_to_wordlist( raw_sentence, \
              remove_stopwords ))
    #
    # Return the list of sentences (each sentence is a list of words,
    # so this returns a list of lists
    return sentences

sen = []
def review_to_wordlist( review, remove_stopwords=False ):
    # Function to convert a document to a sequence of words,
    # optionally removing stop words.  Returns a list of words.
    #
    # 1. Remove HTML
    review_text = BeautifulSoup(review).get_text()
    #  
    # 2. Remove non-letters
    review_text = re.sub("[^a-zA-Z]"," ", review_text)
    #
    # 3. Convert words to lower case and split them
    words = review_text.lower().split()
    #
    # 4. Optionally remove stop words (false by default)
    if remove_stopwords:
        stops = set(stopwords.words("english"))
        words = [w for w in words if not w in stops]
    #
    # 5. Return a list of words
    return(words)

sentences = []  # Initialize an empty list of sentences

print("Parsing sentences from training set")
sentences += review_to_sentences(tempStr, tokenizer)

# list of sentences, which is further a list of words
#print(sentences)
#exit(0)
##########################################################################################################################################

# Import the built-in logging module and configure it so that Word2Vec 
# creates nice output messages
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',\
    level=logging.INFO)


#print sentences[:20]
#exit(0)
# Set values for various parameters
num_features = 20    # Word vector dimensionality                      
min_word_count = 2   # Minimum word count                        
num_workers = 4       # Number of threads to run in parallel
context = 3          # Context window size                                                                                    
downsampling = 1e-3   # Downsample setting for frequent words

# Initialize and train the model (this will take some time)
from gensim.models import word2vec
print("Training model...")
model = word2vec.Word2Vec(sentences, workers=num_workers, \
            size=num_features, min_count = min_word_count, \
            window = context, sample = downsampling)

# If you don't plan to train the model any further, calling 
# init_sims will make the model much more memory-efficient.
model.init_sims(replace=True)

# It can be helpful to create a meaningful model name and 
# save the model for later use. You can load it later using Word2Vec.load()
model_name = "word2vec"
model.save(model_name)
#print(model[model.index2word[0]])
#print( model.most_similar("the"))
#print(model[first.split()[2]])
#print(model.vocab)
#print(type(model))
#print(len(first.split()))
#print(model['Writing'])
temp = []
for i in model.vocab:
	temp.append(i)
#print(temp)

# to get all the vectors...

'''for i in temp:
	print(model[i])
	print(len(temp))
	print(i)
	exit(0)'''
vecForSen = [[]]
#print(sentences[0])
'''for i in sentences[1]:
	if i in temp:
		vecForSen.append(model[i])
print(vecForSen)
print(len(vecForSen))
print(len(vecForSen[0]))	
print(len(sentences[1]))'''	
index = 0
for i in sentences:
	for each in i:
		if each in temp:
			vecForSen[index].append(model[each])
print(len(vecForSen))
print(len(vecForSen[0]))
#print(len(vecForSen[1]))

