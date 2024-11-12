# Simple text-based prediction to mimic pattern recognition without understanding
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Example text data
sentences = ["I love programming", "I dislike bugs", "I enjoy learning new languages", "I hate syntax errors"]
labels = ["positive", "negative", "positive", "negative"]

# Vectorize text data
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(sentences)

# Train a simple Naive Bayes model
model = MultinomialNB()
model.fit(X, labels)

# Test prediction
test_sentence = ["I love debugging"]
test_vector = vectorizer.transform(test_sentence)
prediction = model.predict(test_vector)

print(f"Prediction for '{test_sentence[0]}': {prediction[0]}")
