# Preprocessing – Stop Word Removal and Lemmatization

# Step 1: Import required libraries
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Step 2: Download necessary NLTK resources (run once)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Step 3: Define input text
text = "Stopword removal and lemmatization are important preprocessing steps in Natural Language Processing"

# Step 4: Tokenize the text
tokens = word_tokenize(text)

# Step 5: Convert tokens to lowercase
tokens = [word.lower() for word in tokens]

# Step 6: Load English stopwords
stop_words = set(stopwords.words('english'))

# Step 7: Remove stopwords
filtered_tokens = [word for word in tokens if word not in stop_words]

# Step 8: Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Step 9: Apply lemmatization
lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]

# Step 10: Display outputs
print("Original Text:")
print(text)

print("\nTokens after Stopword Removal:")
print(filtered_tokens)

print("\nTokens after Lemmatization:")
print(lemmatized_tokens)
