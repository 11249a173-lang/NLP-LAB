import nltk
from nltk import word_tokenize
from nltk.tag import RegexpTagger
nltk.download('punkt')
nltk.download('punkt_tab')
patterns = [
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),
    (r'.*ly$', 'RB'),
    (r'.*es$', 'VBZ'),
    (r'.*s$', 'NNS'),
    (r'(The|the|A|a|An|an)$', 'DT'),
    (r'.*', 'NN'),
]
tagger = RegexpTagger(patterns)
paragraph = "The little girl quickly finished her homework. The boys are running and jumping happily."
tokens = word_tokenize(paragraph)
print(tagger.tag(tokens))