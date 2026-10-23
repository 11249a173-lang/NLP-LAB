import nltk
from nltk import word_tokenize
from nltk.tag import RegexpTagger
# Download required NLTK data
nltk.download('punkt')
nltk.download('punkt_tab')
# Hand-written rules (pattern, tag) applied in order
patterns = [
    (r'.*ing$', 'VBG'),       # Gerunds: running
    (r'.*ed$', 'VBD'),        # Past tense: jumped
    (r'.*es$', 'VBZ'),        # Third-person singular: goes
    (r'.*ould$', 'MD'),       # Modals: would, could
    (r".*'s$", 'NN$'),        # Possessive nouns
    (r'.*s$', 'NNS'),         # Plural nouns
    (r'^-?[0-9]+(\.[0-9]+)?$', 'CD'),  # Numbers
    (r'(The|the|A|a|An|an)$', 'DT'),    # Determiners
    (r'(in|on|at|of|for|with)$', 'IN'), # Prepositions
    (r'.*ly$', 'RB'),         # Adverbs
    (r'.*', 'NN')             # Default: noun
]
# Create the rule-based tagger
rule_based_tagger = RegexpTagger(patterns)
# Input a sentence
sentence = input("Enter a sentence: ")
# Tokenization
tokens = word_tokenize(sentence)
# Rule-based PoS tagging
tagged_output = rule_based_tagger.tag(tokens)
# Display the result
print("\nWord\t\tPoS Tag (Rule-Based)")
print("-" * 35)
for word, tag in tagged_output:
    print(f"{word}\t\t{tag}")