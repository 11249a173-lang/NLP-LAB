import re
corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
def tokenize(text):
    return re.findall(r"[a-z']+", text.lower())
training_tokens = tokenize(corpus)
training_vocab = set(training_tokens)
def oov_rate(test_sentence):
    test_tokens = tokenize(test_sentence)
    oov_words = [word for word in test_tokens if word not in training_vocab]
    if len(test_tokens) == 0:
        return 0
    return len(oov_words) / len(test_tokens)
test_sentence = "the fast brown cat runs away"
rate = oov_rate(test_sentence)
print("Test sentence:", test_sentence)
print("OOV Rate:", round(rate * 100, 2), "%")