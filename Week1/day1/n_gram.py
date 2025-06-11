import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

sentence = "I am learning AI"
tokens = word_tokenize(sentence)
bigrams = list(ngrams(tokens, 2)) # Bigram
trigrams = list(ngrams(tokens, 3)) # Trigram
print("Tokens:", tokens)
print("Bigrams:", bigrams)
print("Trigrams:", trigrams)