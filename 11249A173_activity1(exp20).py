import nltk
sentence = "Ravi plays cricket every evening."
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)
print("POS Tags:", tagged)