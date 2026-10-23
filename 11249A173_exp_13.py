def perplexity(prob, n):
    return prob ** (-1 / n) if prob > 0 else float("inf")

test_sentence = "the fox runs away"
n = len(test_sentence.split())

uni_p = 0.0009
bi_p = 0.00021
tri_p = 0.00007

print(f"{'Model':<12}{'Sentence Probability':<23}{'Perplexity':<12}")
print("-" * 47)

print(f"{'Unigram':<12}{uni_p:<23.6f}{perplexity(uni_p, n):<12.2f}")
print(f"{'Bigram':<12}{bi_p:<23.6f}{perplexity(bi_p, n):<12.2f}")
print(f"{'Trigram':<12}{tri_p:<23.6f}{perplexity(tri_p, n):<12.2f}")