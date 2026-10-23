import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("cars"))      # car
print(lemmatizer.lemmatize("running", pos='v'))  # run