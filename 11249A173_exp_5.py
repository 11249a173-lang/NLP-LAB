from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
print(stemmer.stem("running"))   # run
print(stemmer.stem("studies"))   # studi