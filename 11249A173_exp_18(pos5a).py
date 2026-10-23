import nltk
from nltk.corpus import brown
from nltk.tag import hmm
# Download the Brown corpus
nltk.download('brown')
# Step 1: Load tagged sentences
tagged_sentences = brown.tagged_sents(categories='news')
# Step 2: Split into training and testing data
size = int(len(tagged_sentences) * 0.9)
train_data = tagged_sentences[:size]
test_data = tagged_sentences[size:]
# Step 3: Train HMM using supervised learning
trainer = hmm.HiddenMarkovModelTrainer()
# Use LaplaceProbDist for smoothing
hmm_tagger = trainer.train_supervised(
    train_data,
    estimator=lambda fd, bins: nltk.probability.LaplaceProbDist(fd, bins)
)
# Step 4: Evaluate accuracy
accuracy = hmm_tagger.accuracy(test_data)
print(f"HMM Tagger Accuracy: {accuracy * 100:.2f}%")
# Step 5: Tag a sentence
sentence = "They refuse to permit the strike".split()
tagged_output = hmm_tagger.tag(sentence)
# Display output
print("\nWord\t\tPoS Tag (HMM)")
print("-" * 35)
for word, tag in tagged_output:
    print(f"{word}\t\t{tag}")