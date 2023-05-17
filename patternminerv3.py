# Code to gather all the frequently occuring patterns using nltk.

import codecs  # Encoding
import collections  # Collection Objects in Python used for counting

# Importing the libraries
import numpy as np
import pandas as pd
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import WordPunctTokenizer
import matplotlib

# Reading the text file
with codecs.open("log.txt", "r", encoding="utf-8") as f:
    text1 = f.read()


# Tockeninzing the words in the file
def total_tokens(text):
    n = WordPunctTokenizer().tokenize(text)
    return collections.Counter(n), len(n)


text1_counter, text1_size = total_tokens(
    text1)  # Running Fuction on logfile text
keywords = list(text1_counter.keys())
word_vals = list(text1_counter.values())

data = {
    'Most Common Tokens': keywords,
    'Frequency': word_vals
}

res_df = pd.DataFrame(data)
res_df.to_csv("Output2.csv")
print(res_df.columns.to_list())

# Writing to a text file to use as a Brute Force Dictionary
with open('res_dict.txt', 'w') as f:
    for word in keywords:
        f.write(f"{word}\n")
