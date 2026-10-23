import nltk
sentences = [
    "The student reads in the library.",
    "The professor teaches the class.",
    "Students play on the ground.",
    "The researcher works in the laboratory.",
    "The teacher explains the lesson in the classroom."
]
grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
    VP: {<MD>?<VB.*>+}
    PP: {<IN><NP>}
"""
parser = nltk.RegexpParser(grammar)
for sentence in sentences:
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    result = parser.parse(tagged)
    print("\nSentence:", sentence)
    print("Chunked Output:")
    print(result)