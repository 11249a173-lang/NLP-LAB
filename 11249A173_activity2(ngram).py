import re
from collections import Counter, defaultdict
corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
def tokenize(sentence):
    return re.findall(r"[a-z']+", sentence.lower())
sentences = [tokenize(s) for s in corpus.strip().split("\n")]
unigram_counts = Counter()
bigram_counts = Counter()
matrix = defaultdict(dict)
for sent in sentences:
    unigram_counts.update(sent)
    for i in range(len(sent) - 1):
        bigram_counts[(sent[i], sent[i + 1])] += 1
vocab = sorted(unigram_counts.keys())
for w1 in vocab:
    for w2 in vocab:
        matrix[w1][w2] = bigram_counts[(w1, w2)] / unigram_counts[w1]
print(f"{'Word':<12}", end="")
for word in vocab:
    print(f"{word:<8}", end="")
print()
print("-" * (12 + 8 * len(vocab)))
for w1 in vocab:
    print(f"{w1:<12}", end="")
    for w2 in vocab:
        print(f"{matrix[w1][w2]:<8.2f}", end="")
    print()