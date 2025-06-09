import nltk

nltk.download("punkt_tab")
from nltk.tokenize import word_tokenize

sample_text = 'what is the best programming language for highest paying job'
tokens = word_tokenize(sample_text)

print('Tokens:', tokens)