import nltk
sentences = [
    "The tall boy runs fast.",
    "A beautiful flower blooms.",
    "The computer science student studies NLP."
]
grammar = r"NP: {<DT>?<JJ.*>*<NN.*>+}"
parser = nltk.RegexpParser(grammar)
for sentence in sentences:
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    result = parser.parse(tagged)
    print("\nSentence:", sentence)
    print(result)