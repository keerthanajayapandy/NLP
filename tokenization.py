import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

text = "I love Natural Language Processing"
tokens = word_tokenize(text)

print(tokens)
