import re
import random
from collections import defaultdict, Counter
corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
def tokenize(sentence):
    return ["<s>", "<s>"] + re.findall(r"[a-z']+", sentence.lower()) + ["</s>"]
sentences = [tokenize(s) for s in corpus.strip().split("\n")]
bigram_model = defaultdict(Counter)
trigram_model = defaultdict(Counter)
for sent in sentences:
    for i in range(len(sent) - 1):
        bigram_model[(sent[i],)][sent[i+1]] += 1
    for i in range(len(sent) - 2):
        trigram_model[(sent[i], sent[i+1])][sent[i+2]] += 1
def generate_bigram(max_len=15):
    word = "<s>"
    result = []
    for _ in range(max_len):
        choices = bigram_model[(word,)]
        if not choices:
            break
        words, counts = zip(*choices.items())
        word = random.choices(words, weights=counts)[0]
        if word == "</s>":
            break
        result.append(word)
    return " ".join(result)
def generate_trigram(max_len=15):
    w1, w2 = "<s>", "<s>"
    result = []
    for _ in range(max_len):
        choices = trigram_model[(w1, w2)]
        if not choices:
            break
        words, counts = zip(*choices.items())
        w3 = random.choices(words, weights=counts)[0]
        if w3 == "</s>":
            break
        result.append(w3)
        w1, w2 = w2, w3
    return " ".join(result)
random.seed(42)
print("Bigram Generated Text:")
for i in range(3):
    print(generate_bigram())
print("\nTrigram Generated Text:")
for i in range(3):
    print(generate_trigram())