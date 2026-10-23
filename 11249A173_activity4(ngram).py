import nltk
import re
from collections import Counter
from nltk.corpus import gutenberg
tokens = [
    word.lower()
    for word in gutenberg.words("austen-emma.txt")
    if re.fullmatch(r"[a-zA-Z']+", word)
]
unigram_counts = Counter(tokens)
N = len(tokens)
print("Total tokens:", N)
print(f"{'Word':<15}{'Count':<10}{'P(word)':<10}")
print("-" * 35)
for word, count in unigram_counts.most_common(20):
    print(f"{word:<15}{count:<10}{count/N:<10.6f}")
bigram_counts = Counter()
for i in range(len(tokens) - 1):
    bigram_counts[(tokens[i], tokens[i+1])] += 1
print("\nTop 10 Bigrams")
for bigram, count in bigram_counts.most_common(10):
    print(bigram, count)