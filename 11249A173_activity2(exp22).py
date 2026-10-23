import nltk
sentence = "The students read their textbooks."
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)
grammar = r"""
    NP: {<DT|PRP\$>?<JJ.*>*<NN.*>+}
"""
parser = nltk.RegexpParser(grammar)
result = parser.parse(tagged)
print("POS Tags:", tagged)
print("\nUpdated Grammar Output:")
print(result)