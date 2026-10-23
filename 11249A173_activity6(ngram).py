import re
from collections import Counter
corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
def tokenize(sentence):
    return re.findall(r"[a-z']+", sentence.lower())
tokens = tokenize(corpus)
unigram_counts = Counter(tokens)
bigram_counts = Counter()
for i in range(len(tokens) - 1):
    bigram_counts[(tokens[i], tokens[i+1])] += 1
V = len(unigram_counts)
def bigram_probability(w1, w2, k):
    return (bigram_counts[(w1, w2)] + k) / (unigram_counts[w1] + k * V)
def sentence_probability(sentence, k):
    words = tokenize(sentence)
    prob = 1.0
    for i in range(len(words) - 1):
        prob *= bigram_probability(words[i], words[i+1], k)
    return prob
test = "the fox runs away"
print(f"{'k':<8}{'Sentence Probability':<25}")
print("-" * 35)
for k in [0.01, 0.1, 0.5, 1.0, 2.0]:
    prob = sentence_probability(test, k)
    print(f"{k:<8}{prob:<25.10f}")