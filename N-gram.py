# Creation of N-grams using NLTK

from nltk import ngrams

# Input sentence
sentence = input("Enter a sentence: ")
n = int(input("Enter the value of n: "))

print("\n--- Word N-grams ---")

# Split sentence into words
words = sentence.split()

# Generate word n-grams
word_ngrams = ngrams(words, n)

# Print word n-grams
for gram in word_ngrams:
    print(gram)


print("\n--- Character N-grams ---")

# Generate character n-grams
char_ngrams = ngrams(sentence, n)

# Print character n-grams
for gram in char_ngrams:
    print("".join(gram))
