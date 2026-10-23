import re
from collections import Counter
import matplotlib.pyplot as plt
corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
tokens = re.findall(r"[a-z']+", corpus.lower())
counts = Counter(tokens)
top10 = counts.most_common(10)
words = [x[0] for x in top10]
frequencies = [x[1] for x in top10]
plt.figure(figsize=(10, 6))
plt.bar(words, frequencies, color="skyblue")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Top 10 Unigrams")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()