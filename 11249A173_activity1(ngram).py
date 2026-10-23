import re
from nltk import FreqDist
corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
tokens = re.findall(r"[a-z']+", corpus.lower())
fdist = FreqDist(tokens)
N = len(tokens)
print("Total tokens:", N)
print(f"{'Word':<12}{'Count':<8}{'P(word)':<10}")
print("-" * 30)
for word, count in fdist.most_common():
    print(f"{word:<12}{count:<8}{count/N:<10.4f}")
word = "fox"
print(f"\nP('{word}') =", round(fdist[word] / N, 4))