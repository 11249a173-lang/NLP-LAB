import nltk
sentence = "The boy plays in the garden."
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)
print("POS Tagged Output:")
print(tagged)
grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
    VP: {<MD>?<VB.*>+}
    PP: {<IN><NP>}
"""
parser = nltk.RegexpParser(grammar)
result = parser.parse(tagged)
print("\nChunked Output:")
print(result)