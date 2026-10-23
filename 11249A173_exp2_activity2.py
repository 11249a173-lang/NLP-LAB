from collections import Counter
text = "I love NLP I love Python"
words = text.split()
unigram = Counter(words)
print("Unigram Probability:")
for word, count in unigram.items():
    print(word, "=", count / len(words))
bigram = Counter()
for i in range(len(words) - 1):
    pair = words[i] + " " + words[i+1]
    bigram[pair] += 1
print("\nBigram Probability:")
for pair, count in bigram.items():
    print(pair, "=", count / (len(words) - 1))