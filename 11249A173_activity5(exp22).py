import nltk
sentence = "The student is reading a very useful book."
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)
grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
    VP: {<MD>?<VB.*>+}
"""
parser = nltk.RegexpParser(grammar)
result = parser.parse(tagged)
print("POS Tags:", tagged)
print("\nChunked Output:")
print(result)
improved_grammar = r"""
    NP: {<DT>?<RB.*>*<JJ.*>*<NN.*>+}
    VP: {<MD>?<VB.*>+}
"""
improved_parser = nltk.RegexpParser(improved_grammar)
print("\nImproved Chunked Output:")
print(improved_parser.parse(tagged))