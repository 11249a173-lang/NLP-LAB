import nltk
sentence = "The young scientist is developing a new application."
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)
grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
    VP: {<MD>?<VB.*>+}
    PP: {<IN><NP>}
"""
parser = nltk.RegexpParser(grammar)
result = parser.parse(tagged)
print("POS Tags:", tagged)
print("\nChunked Output:")
print(result)