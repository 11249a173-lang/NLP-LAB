import nltk
from nltk.corpus import brown
from nltk import UnigramTagger, word_tokenize
from nltk.tag import brill, brill_trainer
# Download required NLTK datasets
nltk.download('brown')
nltk.download('punkt')
nltk.download('punkt_tab')
# Step 1: Load tagged sentences from the Brown corpus
tagged_sentences = brown.tagged_sents(categories='news')
# Step 2: Split into training and testing data (90% / 10%)
size = int(len(tagged_sentences) * 0.9)
train_data = tagged_sentences[:size]
test_data = tagged_sentences[size:]
# Step 3: Create the initial baseline tagger
baseline_tagger = UnigramTagger(train_data)
print(
    f"Baseline (Unigram) Accuracy: "
    f"{baseline_tagger.accuracy(test_data) * 100:.2f}%"
)
# Step 4: Define transformation rule templates
templates = brill.brill24()
# Step 5: Train the Brill tagger
trainer = brill_trainer.BrillTaggerTrainer(
    baseline_tagger,
    templates,
    trace=3
)
brill_tagger = trainer.train(
    train_data,
    max_rules=20
)
# Step 6: Evaluate the Brill tagger
print(
    f"\nBrill Tagger Accuracy: "
    f"{brill_tagger.accuracy(test_data) * 100:.2f}%"
)
# Step 7: Tag a new sentence
sentence = input("\nEnter a sentence: ")
tokens = word_tokenize(sentence)
tagged_output = brill_tagger.tag(tokens)
# Display the tagged output
print("\nWord\t\tPoS Tag (Brill)")
print("-" * 35)
for word, tag in tagged_output:
    print(f"{word}\t\t{tag}")