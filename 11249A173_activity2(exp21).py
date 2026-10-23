import nltk
sentence = "The teacher explains the lesson in the classroom."
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)
grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
    PP: {<IN><DT>?<NN.*>+}
"""
parser = nltk.RegexpParser(grammar)
result = parser.parse(tagged)
print("POS Tags:", tagged)
print("\nChunked Output:")
print(result)