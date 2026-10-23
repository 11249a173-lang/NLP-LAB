import nltk
sentence = "The boy plays in the garden."
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)
grammar1 = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
"""
grammar2 = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
    VP: {<MD>?<VB.*>+}
    PP: {<IN><NP>}
"""
parser1 = nltk.RegexpParser(grammar1)
parser2 = nltk.RegexpParser(grammar2)
print("NP Only:")
print(parser1.parse(tagged))
print("\nNP + VP + PP:")
print(parser2.parse(tagged))