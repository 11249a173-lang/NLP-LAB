import nltk
from nltk import word_tokenize, pos_tag
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')
sentence = "The little girl quickly finished her homework before dinner."
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)
for word, tag in tagged:
    print(word, "->", tag)