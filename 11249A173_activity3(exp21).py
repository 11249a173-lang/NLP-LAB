import nltk
sentence = "The young researcher develops an AI model."
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)
grammar = r"NP: {<DT>?<JJ.*>*<NN.*>+}"
parser = nltk.RegexpParser(grammar)
result = parser.parse(tagged)
print("POS Tagged Sequence:")
print(tagged)
print("\nNoun Phrases:")
print(result)